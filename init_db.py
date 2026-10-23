"""
Database initialization script for RevenueIQ.
Creates all necessary tables, indexes, and constraints.
"""
from services.database import Database
from config import Config

def main():
    """Initialize the database."""
    print("Initializing RevenueIQ database...")
    print(f"Database path: {Config.DATABASE_URL}")
    
    db = Database(Config.DATABASE_URL)
    db.init_db()
    
    print("\n✓ Database initialization complete!")
    print("\nNext steps:")
    print("1. Run 'python load_sample_data.py' to load sample conversations")
    print("2. Run 'python app.py' to start the application")

if __name__ == '__main__':
    main()
