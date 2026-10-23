"""
Quick Start - RevenueIQ Application
Simple launcher with clear output
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          RevenueIQ - Revenue Intelligence Inbox         ║
║     Turn Every Conversation Into Your Next Decision     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

🚀 Starting application...
""")

try:
    # Import Flask app
    from app import app
    
    print("✓ Application loaded successfully!\n")
    print("📍 Server Information:")
    print("   • Running on: http://localhost:5000")
    print("   • Local IP:   http://127.0.0.1:5000")
    print("   • Debug mode: Enabled\n")
    
    print("🌐 OPEN YOUR BROWSER AND GO TO:")
    print("\n   👉 http://localhost:5000 👈\n")
    
    print("📱 What you'll see:")
    print("   • Dashboard with KPI cards")
    print("   • Interactive charts")
    print("   • Conversation management")
    print("   • Smart routing center")
    print("   • Import & Export features\n")
    
    print("🛑 To stop the server: Press CTRL+C\n")
    print("─" * 58)
    print("Starting Flask development server...\n")
    
    # Start Flask
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=False  # Disable reloader to avoid double startup
    )
    
except ImportError as e:
    print(f"\n❌ ERROR: Missing dependencies\n")
    print("Please run: python -m pip install -r requirements.txt\n")
    input("Press Enter to exit...")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}\n")
    print("Please check:")
    print("  1. Database initialized: python init_db.py")
    print("  2. Sample data loaded: python load_sample_data.py\n")
    input("Press Enter to exit...")
