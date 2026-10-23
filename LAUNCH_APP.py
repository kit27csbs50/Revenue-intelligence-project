"""
REVENUEIQ APPLICATION LAUNCHER
This script ensures the Flask app runs correctly without directory listing issues
"""
import os
import sys

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          ✅ RevenueIQ - FINAL LAUNCHER ✅                ║
║                                                          ║
║     Turn Every Conversation Into Your Next Decision     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

print("🔧 Configuring application...")

# Import Flask app
try:
    from app import app
    print("✓ Application loaded\n")
except ImportError as e:
    print(f"❌ Error importing app: {e}")
    print("\nPlease run: python -m pip install -r requirements.txt")
    input("\nPress Enter to exit...")
    sys.exit(1)

# Ensure database exists
try:
    from services.database import Database
    db = Database('instance/revenueiq.db')
    stats = db.get_dashboard_stats()
    print(f"✓ Database connected ({stats.get('total_calls', 0) + stats.get('total_meetings', 0)} conversations loaded)\n")
except Exception as e:
    print(f"⚠️  Database warning: {e}")
    print("   Run: python init_db.py && python load_sample_data.py\n")

# Display launch information
print("="*60)
print("🚀 STARTING REVENUEIQ APPLICATION")
print("="*60)
print("\n📍 The application will open on:\n")
print("   👉 http://localhost:5000 👈")
print("   👉 http://127.0.0.1:5000 👈\n")
print("="*60)
print("\n📱 WHAT YOU'LL SEE:")
print("   • Professional dark navy dashboard")
print("   • 5 KPI cards with real metrics")
print("   • 4 interactive Chart.js visualizations")
print("   • Sidebar navigation menu")
print("   • Recent activity feed\n")
print("="*60)
print("\n🎯 PAGES TO EXPLORE:")
print("   1. Dashboard (Overview)")
print("   2. Conversations (List all)")
print("   3. Routing Center (Smart routing)")
print("   4. Import & Sync (CSV upload)")
print("   5. Reports & Exports (Download data)")
print("   6. Activity History (Audit trail)\n")
print("="*60)
print("\n🛑 TO STOP: Press CTRL+C in this window\n")
print("="*60)
print("\nStarting Flask development server...\n")

# Run the application
if __name__ == '__main__':
    try:
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=True,
            use_reloader=False  # Prevent double startup
        )
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped gracefully")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        input("\nPress Enter to exit...")
