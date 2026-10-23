# RevenueIQ Deployment Guide

**Application**: Revenue Intelligence Inbox (RevenueIQ)  
**Version**: 1.0  
**Date**: October 23, 2026

---

## 🎯 Deployment Overview

This guide covers deploying RevenueIQ to production-ready hosting platforms. The application is designed to work with any Flask-compatible hosting service.

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure:

- [ ] All tests pass (`pytest tests/ -v`)
- [ ] Database is initialized and tested
- [ ] Environment variables are configured
- [ ] Sample data loaded (or real data imported)
- [ ] Application runs successfully locally
- [ ] Security configurations reviewed
- [ ] File upload/export directories configured
- [ ] Secret key generated for production

---

## 🔧 Environment Configuration

### Required Environment Variables

Create a `.env` file (never commit this to version control):

```bash
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-strong-secret-key-here

# Database Configuration
DATABASE_URL=instance/revenueiq.db

# Upload Configuration
MAX_UPLOAD_SIZE=16777216
UPLOAD_FOLDER=uploads

# Export Configuration
EXPORT_FOLDER=exports
```

### Generate Secret Key

```python
import secrets
print(secrets.token_hex(32))
```

---

## 🚀 Deployment Platforms

### Option 1: Heroku

**Step 1: Install Heroku CLI**
```bash
# Download from https://devcenter.heroku.com/articles/heroku-cli
```

**Step 2: Create Heroku App**
```bash
heroku login
heroku create your-revenueiq-app
```

**Step 3: Set Environment Variables**
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set FLASK_ENV=production
```

**Step 4: Deploy**
```bash
git init
git add .
git commit -m "Initial deployment"
git push heroku main
```

**Step 5: Initialize Database**
```bash
heroku run python init_db.py
heroku run python load_sample_data.py
```

**Step 6: Open Application**
```bash
heroku open
```

### Option 2: Railway

**Step 1: Install Railway CLI**
```bash
npm i -g @railway/cli
```

**Step 2: Login and Initialize**
```bash
railway login
railway init
```

**Step 3: Set Environment Variables**
```bash
railway variables set SECRET_KEY=your-secret-key
railway variables set FLASK_ENV=production
```

**Step 4: Deploy**
```bash
railway up
```

**Step 5: Open Application**
```bash
railway open
```

### Option 3: Render

**Step 1: Connect GitHub Repository**
1. Go to https://render.com
2. Sign in and click "New +"
3. Select "Web Service"
4. Connect your GitHub repository

**Step 2: Configure Service**
- **Name**: revenueiq
- **Environment**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Step 3: Set Environment Variables**
Add in Render dashboard:
- `SECRET_KEY`: your-secret-key
- `FLASK_ENV`: production
- `PYTHON_VERSION`: 3.11.0

**Step 4: Deploy**
Render will automatically deploy on git push.

### Option 4: DigitalOcean App Platform

**Step 1: Connect Repository**
1. Go to DigitalOcean dashboard
2. Click "Create" → "App"
3. Connect GitHub repository

**Step 2: Configure App**
- **Type**: Web Service
- **Build Command**: `pip install -r requirements.txt`
- **Run Command**: `gunicorn --bind 0.0.0.0:8080 app:app`

**Step 3: Set Environment Variables**
- `SECRET_KEY`
- `FLASK_ENV=production`

**Step 4: Deploy**
DigitalOcean will build and deploy automatically.

### Option 5: Traditional VPS (Ubuntu/Debian)

**Step 1: Update System**
```bash
sudo apt update
sudo apt upgrade -y
```

**Step 2: Install Dependencies**
```bash
sudo apt install python3 python3-pip python3-venv nginx -y
```

**Step 3: Clone Repository**
```bash
cd /var/www
sudo git clone your-repo-url revenueiq
cd revenueiq
```

**Step 4: Set Up Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Step 5: Configure Environment**
```bash
cp .env.example .env
nano .env  # Edit with production values
```

**Step 6: Initialize Database**
```bash
python init_db.py
python load_sample_data.py  # Optional
```

**Step 7: Set Up Systemd Service**
Create `/etc/systemd/system/revenueiq.service`:

```ini
[Unit]
Description=RevenueIQ Flask Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/revenueiq
Environment="PATH=/var/www/revenueiq/venv/bin"
ExecStart=/var/www/revenueiq/venv/bin/gunicorn --workers 4 --bind 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target
```

**Step 8: Enable and Start Service**
```bash
sudo systemctl enable revenueiq
sudo systemctl start revenueiq
sudo systemctl status revenueiq
```

**Step 9: Configure Nginx**
Create `/etc/nginx/sites-available/revenueiq`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /var/www/revenueiq/static;
        expires 30d;
    }

    client_max_body_size 20M;
}
```

**Step 10: Enable Site and Restart Nginx**
```bash
sudo ln -s /etc/nginx/sites-available/revenueiq /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

**Step 11: Set Up SSL (Optional but Recommended)**
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

---

## 🗄️ Database Considerations

### SQLite (Development/Demo)

**Advantages:**
- No external dependencies
- Simple setup
- Perfect for demos and small teams

**Limitations:**
- Single-writer limitation
- Not ideal for high concurrency
- File-based (needs persistent storage)

**Production Use:**
- Suitable for < 100 concurrent users
- Ensure database file is in persistent storage
- Regular backups recommended

### PostgreSQL (Production)

**When to Migrate:**
- Need for > 100 concurrent users
- Require better concurrency
- Need advanced features (full-text search, etc.)
- Multiple application servers

**Migration Steps:**

1. **Install PostgreSQL Adapter**
```bash
pip install psycopg2-binary
```

2. **Update config.py**
```python
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:pass@localhost/revenueiq')
```

3. **Modify database.py** to use SQLAlchemy or similar ORM

---

## 📦 File Storage

### Local File Storage (Default)

**Setup:**
```python
UPLOAD_FOLDER = 'uploads'
EXPORT_FOLDER = 'exports'
```

**Considerations:**
- Ensure folders are in persistent storage
- Set appropriate permissions
- Regular cleanup of old files

### Cloud Storage (Production Scale)

**AWS S3 Example:**

```bash
pip install boto3
```

```python
import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
)

# Upload file
s3_client.upload_file(local_path, 'bucket-name', 'path/in/s3')
```

**Azure Blob Storage Example:**

```bash
pip install azure-storage-blob
```

---

## 🔒 Security Hardening

### 1. Environment Variables

**Never commit:**
- `.env` files
- Secret keys
- Database credentials
- API keys

**Use:**
- Platform-specific secret management
- Environment variable injection
- Encrypted configuration

### 2. HTTPS/SSL

**Always use HTTPS in production:**
- Use Let's Encrypt for free SSL
- Configure reverse proxy (Nginx/Apache)
- Redirect HTTP to HTTPS

### 3. Security Headers

Add to `app.py`:

```python
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response
```

### 4. CSRF Protection

Install Flask-WTF:
```bash
pip install flask-wtf
```

Enable in production:
```python
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)
```

### 5. Rate Limiting

Install Flask-Limiter:
```bash
pip install flask-limiter
```

```python
from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/import/upload', methods=['POST'])
@limiter.limit("10 per hour")
def upload_csv():
    # ...
```

### 6. Input Validation

- All user inputs validated server-side
- File uploads restricted by type and size
- SQL injection prevented (parameterized queries)
- XSS prevented (template escaping)

---

## 📊 Monitoring & Logging

### Application Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('revenueiq.log'),
        logging.StreamHandler()
    ]
)
```

### Error Tracking

**Sentry Integration:**
```bash
pip install sentry-sdk[flask]
```

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)
```

### Performance Monitoring

**New Relic:**
```bash
pip install newrelic
newrelic-admin generate-config YOUR_LICENSE_KEY newrelic.ini
newrelic-admin run-program gunicorn app:app
```

---

## 🔄 Backup Strategy

### Database Backups

**SQLite:**
```bash
# Daily backup script
#!/bin/bash
cp instance/revenueiq.db backups/revenueiq_$(date +%Y%m%d).db
find backups/ -mtime +30 -delete  # Keep 30 days
```

**PostgreSQL:**
```bash
pg_dump revenueiq > backup_$(date +%Y%m%d).sql
```

### File Backups

```bash
# Backup uploads and exports
tar -czf backup_files_$(date +%Y%m%d).tar.gz uploads/ exports/
```

---

## 🧪 Post-Deployment Verification

### 1. Health Check

Visit: `https://your-domain.com/`

**Expected:**
- ✅ Dashboard loads successfully
- ✅ No error messages
- ✅ KPI cards display correctly
- ✅ Charts render properly

### 2. Functionality Tests

- [ ] Create a test conversation manually
- [ ] Import a small CSV file
- [ ] Export data to CSV and JSON
- [ ] Download manifest file
- [ ] View activity history
- [ ] Update a conversation
- [ ] Test routing center
- [ ] Verify search functionality

### 3. Performance Tests

```bash
# Using Apache Bench
ab -n 1000 -c 10 https://your-domain.com/

# Using wrk
wrk -t12 -c400 -d30s https://your-domain.com/
```

### 4. Security Scan

```bash
# SSL test
https://www.ssllabs.com/ssltest/

# Security headers
https://securityheaders.com/
```

---

## 🆘 Troubleshooting

### Issue: Database Not Found

**Solution:**
```bash
python init_db.py
```

### Issue: Permission Denied on Uploads

**Solution:**
```bash
chmod 755 uploads exports
chown www-data:www-data uploads exports
```

### Issue: Gunicorn Workers Timeout

**Solution:**
```bash
gunicorn --timeout 120 --workers 4 app:app
```

### Issue: Out of Memory

**Solution:**
- Reduce number of workers
- Increase server memory
- Optimize queries
- Add pagination to large datasets

### Issue: Slow Import Performance

**Solution:**
- Process imports in background (Celery)
- Increase worker timeout
- Optimize database indexes
- Batch insert operations

---

## 📈 Scaling Considerations

### Horizontal Scaling

**Load Balancer:**
```
[Load Balancer]
      |
      ├─── [App Server 1] ─┐
      ├─── [App Server 2] ─┼─── [Database]
      └─── [App Server 3] ─┘
```

**Requirements:**
- Shared database (PostgreSQL)
- Shared file storage (S3)
- Session management (Redis)

### Vertical Scaling

**Optimize Server Resources:**
- Increase RAM for database caching
- More CPU cores for worker processes
- SSD for faster database operations

### Caching

**Redis for Dashboard Metrics:**
```bash
pip install redis flask-caching
```

```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/')
@cache.cached(timeout=300)  # Cache for 5 minutes
def dashboard():
    # ...
```

---

## ✅ Production Checklist

- [ ] Environment variables set correctly
- [ ] Secret key is strong and unique
- [ ] Database initialized
- [ ] HTTPS/SSL configured
- [ ] Security headers enabled
- [ ] CSRF protection enabled
- [ ] Rate limiting configured
- [ ] Error logging set up
- [ ] Backup strategy implemented
- [ ] Monitoring configured
- [ ] Performance tested
- [ ] Security scan passed
- [ ] Documentation updated
- [ ] Team trained on system

---

## 📞 Support

For deployment issues:

1. Check application logs: `tail -f revenueiq.log`
2. Check system logs: `sudo journalctl -u revenueiq -f`
3. Review error messages in browser console
4. Verify environment variables
5. Test database connectivity
6. Check file permissions

---

**Document Version**: 1.0  
**Last Updated**: October 23, 2026  
**Maintained By**: RevenueIQ Development Team
