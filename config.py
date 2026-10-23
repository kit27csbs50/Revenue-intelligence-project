"""
Configuration management for RevenueIQ application.
Loads settings from environment variables with sensible defaults.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration class."""
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'
    
    # Database Configuration
    DATABASE_URL = os.getenv('DATABASE_URL', 'instance/revenueiq.db')
    
    # Upload Configuration
    MAX_UPLOAD_SIZE = int(os.getenv('MAX_UPLOAD_SIZE', 16777216))  # 16MB default
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    ALLOWED_EXTENSIONS = {'csv'}
    
    # Export Configuration
    EXPORT_FOLDER = os.getenv('EXPORT_FOLDER', 'exports')
    
    # Pagination
    ITEMS_PER_PAGE = 20
    
    @staticmethod
    def init_app(app):
        """Initialize application with configuration."""
        # Create necessary directories
        os.makedirs('instance', exist_ok=True)
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(Config.EXPORT_FOLDER, exist_ok=True)
