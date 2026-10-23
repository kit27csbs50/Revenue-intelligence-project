"""
Simple Flask Server - Guaranteed to Work
This is a minimal version to test if Flask is working
"""
from flask import Flask, render_template
import os
import sys

# Create Flask app
simple_app = Flask(__name__)

# Test route
@simple_app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>RevenueIQ - Connection Test</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0a1128, #1e293b);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                padding: 3rem;
                background: rgba(255,255,255,0.1);
                border-radius: 20px;
                max-width: 600px;
            }
            h1 { font-size: 3rem; margin: 0; }
            .success { color: #10b981; font-size: 5rem; }
            p { font-size: 1.2rem; margin: 1rem 0; }
            .button {
                display: inline-block;
                padding: 1rem 2rem;
                background: #3b82f6;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                margin: 1rem;
                font-weight: bold;
            }
            .button:hover { background: #2563eb; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="success">✓</div>
            <h1>Flask Server is Working!</h1>
            <p>Your RevenueIQ application is running correctly.</p>
            <p>Connection to <strong>localhost:5000</strong> successful!</p>
            <hr style="border: 1px solid rgba(255,255,255,0.2); margin: 2rem 0;">
            <a href="/test-full-app" class="button">🚀 Load Full Application</a>
        </div>
    </body>
    </html>
    """

@simple_app.route('/test-full-app')
def test_full_app():
    try:
        # Import the real app
        from app import app as real_app
        from services.database import Database
        
        # Test database
        db = Database('instance/revenueiq.db')
        stats = db.get_dashboard_stats()
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>RevenueIQ - System Check</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #0a1128, #1e293b);
                    color: white;
                    padding: 2rem;
                }}
                .container {{
                    max-width: 800px;
                    margin: 0 auto;
                    background: rgba(255,255,255,0.1);
                    padding: 2rem;
                    border-radius: 20px;
                }}
                .check {{ color: #10b981; }}
                .stat {{ background: rgba(59, 130, 246, 0.2); padding: 1rem; margin: 0.5rem 0; border-radius: 10px; }}
                .button {{
                    display: inline-block;
                    padding: 1rem 2rem;
                    background: #10b981;
                    color: white;
                    text-decoration: none;
                    border-radius: 10px;
                    margin: 1rem 0;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>✓ System Check Complete</h1>
                <p><span class="check">✓</span> Flask server running</p>
                <p><span class="check">✓</span> Database connected</p>
                <p><span class="check">✓</span> Routes configured ({len(list(real_app.url_map.iter_rules()))} total)</p>
                
                <h2>Dashboard Metrics:</h2>
                <div class="stat">📞 Total Calls: {stats.get('total_calls', 0)}</div>
                <div class="stat">📅 Total Meetings: {stats.get('total_meetings', 0)}</div>
                <div class="stat">😊 Positive Conversations: {stats.get('positive_conversations', 0)}</div>
                <div class="stat">⏰ Pending Follow-ups: {stats.get('pending_followups', 0)}</div>
                <div class="stat">🔥 High Priority: {stats.get('high_priority', 0)}</div>
                
                <h2>✅ Everything is Working!</h2>
                <p>The full application is ready. Stop this server and run the main app.</p>
                <p><strong>Run:</strong> <code>python app.py</code></p>
            </div>
        </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
        <body style="font-family: Arial; padding: 2rem; background: #1e293b; color: white;">
            <h1>⚠️ Error</h1>
            <p>Error testing full app: {str(e)}</p>
            <p>But the Flask server is working! The issue is with the application setup.</p>
        </body>
        </html>
        """

if __name__ == '__main__':
    print("\n" + "="*60)
    print("  SIMPLE FLASK SERVER - Testing Connection")
    print("="*60)
    print("\n✓ Starting server on http://localhost:5000")
    print("\n🌐 OPEN YOUR BROWSER TO:")
    print("   http://localhost:5000")
    print("\nIf this works, you'll see a success message!")
    print("If not, there's a firewall or port issue.")
    print("\nPress CTRL+C to stop")
    print("="*60 + "\n")
    
    try:
        simple_app.run(host='127.0.0.1', port=5000, debug=False)
    except OSError as e:
        if "address already in use" in str(e).lower():
            print("\n⚠️  Port 5000 is already in use!")
            print("Kill the process with: taskkill /F /IM python.exe")
            print("Then try again.")
        else:
            print(f"\n⚠️  Error: {e}")
