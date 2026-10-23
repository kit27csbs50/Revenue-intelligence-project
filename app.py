"""
RevenueIQ - Revenue Intelligence Inbox
Main Flask application with routes and business logic.
"""
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime
from config import Config
from services.database import Database
from services.analysis import ConversationAnalyzer
from services.routing import SmartRouter
from services.import_service import ImportService
from services.export_service import ExportService

# Initialize Flask app with explicit configuration
app = Flask(__name__, 
            static_folder='static', 
            template_folder='templates',
            static_url_path='/static')
app.config.from_object(Config)
app.secret_key = app.config['SECRET_KEY']
Config.init_app(app)

# Disable Flask's automatic static file serving for root directory
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Disable directory listing
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Initialize services
db = Database(app.config['DATABASE_URL'])
analyzer = ConversationAnalyzer()
router = SmartRouter()
import_service = ImportService(db)
export_service = ExportService(db, app.config['EXPORT_FOLDER'])

# Template filters
@app.template_filter('datetime')
def format_datetime(value):
    """Format datetime for display."""
    if isinstance(value, str):
        try:
            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M')
        except:
            return value
    return value

@app.template_filter('date')
def format_date(value):
    """Format date for display."""
    if isinstance(value, str):
        try:
            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d')
        except:
            return value
    return value

# Routes

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/dashboard')
def dashboard():
    """Main dashboard with KPIs and charts."""
    try:
        # Get statistics from database
        stats = db.get_dashboard_stats()
        chart_data = db.get_chart_data()
        
        # Get recent activity
        recent_activity = db.get_activity_history(limit=10)
        
        return render_template('dashboard.html',
                             stats=stats,
                             chart_data=chart_data,
                             recent_activity=recent_activity,
                             current_date=datetime.now().strftime('%B %d, %Y'))
    except Exception as e:
        app.logger.error(f"Dashboard error: {e}")
        return render_template('dashboard.html',
                             stats={},
                             chart_data={},
                             recent_activity=[],
                             error=str(e))

@app.route('/conversations')
def conversations():
    """Conversations list with filters and pagination."""
    try:
        # Get filter parameters
        filters = {}
        if request.args.get('search'):
            filters['search'] = request.args.get('search')
        if request.args.get('sentiment'):
            filters['sentiment'] = request.args.get('sentiment')
        if request.args.get('priority'):
            filters['priority'] = request.args.get('priority')
        if request.args.get('status'):
            filters['status'] = request.args.get('status')
        if request.args.get('conversation_type'):
            filters['conversation_type'] = request.args.get('conversation_type')
        if request.args.get('assigned_team'):
            filters['assigned_team'] = request.args.get('assigned_team')
        
        # Get pagination parameters
        page = request.args.get('page', 1, type=int)
        per_page = app.config['ITEMS_PER_PAGE']
        
        # Get conversations
        conversations_list, total = db.get_all_conversations(filters=filters, page=page, per_page=per_page)
        
        # Calculate pagination
        total_pages = (total + per_page - 1) // per_page
        
        return render_template('conversations.html',
                             conversations=conversations_list,
                             page=page,
                             total_pages=total_pages,
                             total=total,
                             filters=filters)
    except Exception as e:
        app.logger.error(f"Conversations error: {e}")
        return render_template('conversations.html',
                             conversations=[],
                             page=1,
                             total_pages=1,
                             total=0,
                             filters={},
                             error=str(e))

@app.route('/conversation/<conversation_id>')
def conversation_detail(conversation_id):
    """View single conversation details."""
    try:
        conversation = db.get_conversation_by_id(conversation_id)
        
        if not conversation:
            flash('Conversation not found', 'error')
            return redirect(url_for('conversations'))
        
        # Get activity history for this conversation
        activity = db.get_activity_history(filters={'conversation_id': conversation_id}, limit=20)
        
        return render_template('conversation_detail.html',
                             conversation=conversation,
                             activity=activity)
    except Exception as e:
        app.logger.error(f"Conversation detail error: {e}")
        flash(f'Error loading conversation: {str(e)}', 'error')
        return redirect(url_for('conversations'))

@app.route('/conversation/<conversation_id>/update', methods=['POST'])
def update_conversation(conversation_id):
    """Update conversation fields."""
    try:
        update_data = {}
        
        # Get form data
        if request.form.get('sentiment'):
            update_data['sentiment'] = request.form.get('sentiment')
        if request.form.get('priority'):
            update_data['priority'] = request.form.get('priority')
        if request.form.get('status'):
            update_data['status'] = request.form.get('status')
        if request.form.get('assigned_team'):
            update_data['assigned_team'] = request.form.get('assigned_team')
        if request.form.get('assigned_employee'):
            update_data['assigned_employee'] = request.form.get('assigned_employee')
        if request.form.get('next_action'):
            update_data['next_action'] = request.form.get('next_action')
        if request.form.get('follow_up_status'):
            update_data['follow_up_status'] = request.form.get('follow_up_status')
        if request.form.get('summary'):
            update_data['summary'] = request.form.get('summary')
        
        # Update conversation
        if db.update_conversation(conversation_id, update_data):
            # Log activity
            db.add_activity(
                'manual_update',
                f"Manual update: {', '.join(update_data.keys())}",
                conversation_id,
                json.dumps(update_data)
            )
            
            flash('Conversation updated successfully', 'success')
        else:
            flash('Failed to update conversation', 'error')
        
        return redirect(url_for('conversation_detail', conversation_id=conversation_id))
    
    except Exception as e:
        app.logger.error(f"Update conversation error: {e}")
        flash(f'Error updating conversation: {str(e)}', 'error')
        return redirect(url_for('conversation_detail', conversation_id=conversation_id))

@app.route('/routing')
def routing_center():
    """Smart routing center with recommendations."""
    try:
        # Get conversations needing routing (Open status)
        conversations_list, total = db.get_all_conversations(
            filters={'status': 'Open'},
            page=1,
            per_page=50
        )
        
        # Analyze each conversation for routing
        routing_recommendations = []
        for conv in conversations_list:
            analysis = analyzer.analyze_conversation(conv['transcript'])
            routing_rec = router.route_conversation(analysis)
            
            routing_recommendations.append({
                'conversation': conv,
                'analysis': analysis,
                'routing': routing_rec,
                'alternatives': router.get_alternative_routing(analysis)
            })
        
        return render_template('routing.html',
                             routing_recommendations=routing_recommendations,
                             total=total)
    except Exception as e:
        app.logger.error(f"Routing center error: {e}")
        return render_template('routing.html',
                             routing_recommendations=[],
                             total=0,
                             error=str(e))

@app.route('/routing/<conversation_id>/assign', methods=['POST'])
def assign_routing(conversation_id):
    """Manually assign routing for conversation."""
    try:
        update_data = {
            'assigned_team': request.form.get('assigned_team'),
            'assigned_employee': request.form.get('assigned_employee'),
            'priority': request.form.get('priority'),
            'next_action': request.form.get('next_action'),
            'status': 'In Progress'
        }
        
        # Update conversation
        if db.update_conversation(conversation_id, update_data):
            # Log routing activity
            db.add_activity(
                'routing',
                f"Routed to {update_data['assigned_team']}",
                conversation_id,
                json.dumps(update_data)
            )
            
            flash('Conversation routed successfully', 'success')
        else:
            flash('Failed to route conversation', 'error')
        
        return redirect(url_for('routing_center'))
    
    except Exception as e:
        app.logger.error(f"Assign routing error: {e}")
        flash(f'Error assigning routing: {str(e)}', 'error')
        return redirect(url_for('routing_center'))

@app.route('/import')
def import_page():
    """CSV import and sync page."""
    try:
        # Get import history
        history = db.get_import_history(limit=20)
        
        return render_template('import.html', import_history=history)
    except Exception as e:
        app.logger.error(f"Import page error: {e}")
        return render_template('import.html', import_history=[], error=str(e))

@app.route('/import/upload', methods=['POST'])
def upload_csv():
    """Handle CSV file upload and import."""
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'success': False, 'error': 'File must be CSV format'}), 400
        
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Validate file
        is_valid, message = import_service.validate_file(filepath)
        if not is_valid:
            os.remove(filepath)
            return jsonify({'success': False, 'error': message}), 400
        
        # Import CSV
        stats = import_service.import_csv(filepath, filename)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'stats': stats
        })
    
    except Exception as e:
        app.logger.error(f"Upload CSV error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/reports')
def reports():
    """Reports and exports page."""
    try:
        # Get available export files
        export_files = export_service.get_export_files()
        
        return render_template('reports.html', export_files=export_files)
    except Exception as e:
        app.logger.error(f"Reports page error: {e}")
        return render_template('reports.html', export_files=[], error=str(e))

@app.route('/reports/export', methods=['POST'])
def export_report():
    """Generate and export report."""
    try:
        export_format = request.form.get('format', 'csv')
        
        # Get filters
        filters = {}
        if request.form.get('sentiment'):
            filters['sentiment'] = request.form.get('sentiment')
        if request.form.get('priority'):
            filters['priority'] = request.form.get('priority')
        if request.form.get('status'):
            filters['status'] = request.form.get('status')
        
        # Export based on format
        exports = []
        
        if export_format == 'csv':
            result = export_service.export_csv(filters)
            if result['success']:
                exports.append(result)
        
        elif export_format == 'json':
            result = export_service.export_json(filters)
            if result['success']:
                exports.append(result)
        
        elif export_format == 'both':
            csv_result = export_service.export_csv(filters)
            json_result = export_service.export_json(filters)
            
            if csv_result['success']:
                exports.append(csv_result)
            if json_result['success']:
                exports.append(json_result)
        
        # Generate manifest
        if exports:
            manifest_result = export_service.generate_manifest(exports)
            if manifest_result['success']:
                exports.append(manifest_result)
        
        return jsonify({
            'success': True,
            'exports': exports
        })
    
    except Exception as e:
        app.logger.error(f"Export report error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/reports/download/<filename>')
def download_report(filename):
    """Download export file."""
    try:
        filepath = os.path.join(app.config['EXPORT_FOLDER'], filename)
        
        if not os.path.exists(filepath):
            flash('File not found', 'error')
            return redirect(url_for('reports'))
        
        return send_file(filepath, as_attachment=True)
    
    except Exception as e:
        app.logger.error(f"Download report error: {e}")
        flash(f'Error downloading file: {str(e)}', 'error')
        return redirect(url_for('reports'))

@app.route('/activity')
def activity_history():
    """Activity history page."""
    try:
        # Get filter parameters
        filters = {}
        if request.args.get('action_type'):
            filters['action_type'] = request.args.get('action_type')
        if request.args.get('conversation_id'):
            filters['conversation_id'] = request.args.get('conversation_id')
        
        # Get activity history
        activity = db.get_activity_history(filters=filters, limit=100)
        
        return render_template('activity.html', activity=activity, filters=filters)
    except Exception as e:
        app.logger.error(f"Activity history error: {e}")
        return render_template('activity.html', activity=[], filters={}, error=str(e))

@app.route('/settings')
def settings():
    """Settings page."""
    return render_template('settings.html')

# API endpoints for AJAX requests

@app.route('/api/dashboard/stats')
def api_dashboard_stats():
    """Get dashboard statistics as JSON."""
    try:
        stats = db.get_dashboard_stats()
        return jsonify({'success': True, 'stats': stats})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/dashboard/charts')
def api_dashboard_charts():
    """Get chart data as JSON."""
    try:
        chart_data = db.get_chart_data()
        return jsonify({'success': True, 'data': chart_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/conversation/<conversation_id>/analyze')
def api_analyze_conversation(conversation_id):
    """Analyze conversation and return results."""
    try:
        conversation = db.get_conversation_by_id(conversation_id)
        
        if not conversation:
            return jsonify({'success': False, 'error': 'Conversation not found'}), 404
        
        analysis = analyzer.analyze_conversation(conversation['transcript'])
        routing_rec = router.route_conversation(analysis)
        
        return jsonify({
            'success': True,
            'analysis': analysis,
            'routing': routing_rec
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Error handlers

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Initialize database if it doesn't exist
    if not os.path.exists(app.config['DATABASE_URL']):
        print("Initializing database...")
        db.init_db()
        print("Database initialized. Run 'python load_sample_data.py' to load sample data.")
    
    # Run application
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)
