"""
Simple test to verify Flask app is working correctly
"""
import sys
print("=" * 60)
print("Testing RevenueIQ Flask Application")
print("=" * 60)

try:
    print("\n1. Importing Flask app...")
    from app import app
    print("   ✓ Flask app imported successfully")
    
    print("\n2. Checking configuration...")
    print(f"   Debug mode: {app.config['DEBUG']}")
    print(f"   Database: {app.config['DATABASE_URL']}")
    print("   ✓ Configuration loaded")
    
    print("\n3. Checking routes...")
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(str(rule))
    print(f"   Found {len(routes)} routes")
    print("   ✓ Routes configured")
    
    print("\n4. Testing database connection...")
    from services.database import Database
    db = Database(app.config['DATABASE_URL'])
    stats = db.get_dashboard_stats()
    print(f"   Total calls: {stats.get('total_calls', 0)}")
    print(f"   Total meetings: {stats.get('total_meetings', 0)}")
    print("   ✓ Database connection working")
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - Application is ready!")
    print("=" * 60)
    print("\nStarting Flask server...")
    print("\nOnce started, open your browser to:")
    print("  → http://localhost:5000")
    print("  → http://127.0.0.1:5000")
    print("\nPress CTRL+C to stop the server\n")
    print("=" * 60)
    
    # Start the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    print("\nPlease check:")
    print("  1. All dependencies installed: python -m pip install -r requirements.txt")
    print("  2. Database initialized: python init_db.py")
    print("  3. Sample data loaded: python load_sample_data.py")
    sys.exit(1)
