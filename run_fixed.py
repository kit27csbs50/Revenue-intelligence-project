"""
Fixed launcher for RevenueIQ - Prevents directory listing issue
"""
import os
import sys

print("\n" + "="*70)
print("  🚀 RevenueIQ - Revenue Intelligence Inbox")
print("="*70 + "\n")

# Import the Flask app
try:
    from app import app, db
    print("✅ Application loaded successfully")
except ImportError as e:
    print(f"❌ Error loading application: {e}")
    print("\nPlease install dependencies:")
    print("  pip install -r requirements.txt\n")
    sys.exit(1)

# Verify database
try:
    stats = db.get_dashboard_stats()
    total = stats.get('total_calls', 0) + stats.get('total_meetings', 0)
    print(f"✅ Database connected ({total} conversations)\n")
except Exception as e:
    print(f"⚠️  Database warning: {e}\n")

# Additional configuration to prevent directory listing
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = False

print("="*70)
print("  🌐 ACCESS YOUR APPLICATION AT:")
print("="*70)
print("\n  👉  http://127.0.0.1:5000  👈")
print("  👉  http://localhost:5000  👈\n")
print("="*70)
print("\n  📺 TO VIEW IN VS CODE:")
print("     1. Press: Ctrl + Shift + P")
print("     2. Type: Simple Browser: Show")
print("     3. Enter: http://127.0.0.1:5000\n")
print("="*70)
print("\n  🎯 OR OPEN IN EXTERNAL BROWSER:")
print("     Copy URL above and paste in Chrome/Edge/Firefox\n")
print("="*70)
print("\n  ⚠️  IF YOU SEE FILE LISTING:")
print("     1. Clear browser cache (Ctrl+Shift+Delete)")
print("     2. Use incognito mode (Ctrl+Shift+N)")
print("     3. Hard refresh (Ctrl+F5)\n")
print("="*70)
print("\n  🛑 TO STOP: Press Ctrl+C\n")
print("="*70 + "\n")

print("Starting Flask server...\n")

if __name__ == '__main__':
    try:
        # Run with specific settings to prevent directory listing
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=True,
            use_reloader=False,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped successfully\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        sys.exit(1)
