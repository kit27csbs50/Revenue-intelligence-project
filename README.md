# Revenue Intelligence Inbox (RevenueIQ)

**Turn Every Conversation Into Your Next Smart Decision**

A professional web application for Lazy Blooms that analyzes customer conversations, provides intelligent routing recommendations, tracks sentiment, and manages follow-ups with a premium enterprise SaaS design.

---

## 🎯 Project Overview

RevenueIQ helps businesses:
- **Analyze Conversations**: Automatically identify sentiment, purchase intent, technical issues, and urgent requests
- **Smart Routing**: Recommend appropriate teams and employees based on conversation context
- **Import & Sync**: Upload CSV files with duplicate prevention and smart update detection
- **Track Activity**: Maintain audit history of all imports, updates, and routing decisions
- **Export Reports**: Download conversation data in CSV and JSON formats with manifests

---

## 📋 Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)

---

## 🚀 Installation Instructions

### Step 1: Clone or Download the Project

```bash
cd Revenue_intelligence_project_volopay
```

### Step 2: Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

```bash
copy .env.example .env
```

Edit `.env` and configure:
- `SECRET_KEY`: Generate a secure random key
- `FLASK_ENV`: Set to `development` for testing, `production` for deployment
- `DATABASE_URL`: SQLite database path (default: `instance/revenueiq.db`)

### Step 5: Initialize the Database

```bash
python init_db.py
```

This creates all necessary tables with proper indexes and constraints.

### Step 6: Load Sample Data (Optional)

```bash
python load_sample_data.py
```

This loads synthetic sample conversations for demonstration purposes.

---

## ▶️ Running the Application

### Development Mode

```bash
python app.py
```

The application will start at: **http://localhost:5000**

### Production Mode

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📊 Using the Application

### Dashboard
- View KPI cards: Total calls, meetings, positive conversations, pending follow-ups, high-priority customers
- Interactive charts: Calls/meetings over time, sentiment distribution, follow-up status, employee activity
- All metrics calculated from actual database records

### Conversations Page
- Search, filter, sort, and paginate conversations
- View conversation details, transcripts, sentiment, and priority
- Edit conversation properties (sentiment, priority, team, employee, status)
- Manual corrections are preserved during future imports

### Smart Routing Center
- View recommended teams and employees based on conversation analysis
- See routing reasons and supporting evidence
- Manually reassign conversations with audit trail

### Import & Sync
- Upload CSV files with automatic column mapping
- Preview data before import
- Duplicate prevention: Skip records with existing IDs
- Update detection: Update records when imported data changes
- Row-level error reporting with downloadable error reports
- Import history with accurate totals

### Reports & Exports
- Export conversations to CSV or JSON
- Apply filters before export
- Download manifest.json with export metadata
- Activity history tracks all exports

### Activity History
- View all imports, updates, manual corrections, and exports
- Filter by action type and date range
- Track who made changes and when

---

## 🔄 Import & Sync Behavior

### CSV Import Rules

1. **Duplicate Prevention**: Records with existing IDs are skipped (unchanged)
2. **Update Detection**: Records are updated only if imported values differ
3. **Validation**: Invalid records are rejected with detailed error messages
4. **Transaction Safety**: Entire import rolls back on critical failures
5. **Manual Corrections**: Manager edits are preserved during imports unless explicitly overwritten

### Required CSV Columns

- `conversation_id` or `id`: Unique identifier
- `customer_name`: Customer's name
- `conversation_type`: "Call" or "Meeting"
- `timestamp` or `date`: ISO format (YYYY-MM-DD HH:MM:SS)
- `transcript` or `summary`: Conversation content

### Optional CSV Columns

- `employee_name`: Assigned employee
- `sentiment`: Positive, Neutral, or Negative
- `priority`: Low, Medium, High, Urgent
- `status`: Open, In Progress, Completed
- `assigned_team`: Team name
- `phone_number`, `email`, `company`, etc.

### Testing Duplicate Prevention

1. Import a CSV file
2. Import the same file again
3. Verify: 0 new records created, all marked as "unchanged"

### Testing Update Synchronization

1. Import a CSV file
2. Modify values in the CSV (change sentiment, priority, etc.)
3. Import the modified file
4. Verify: Changed records are updated with new values

### Testing Manual Correction Preservation

1. Import a CSV file
2. Edit a conversation manually (change sentiment, assign team)
3. Import the original CSV again
4. Verify: Manual changes are preserved (not overwritten)

---

## 🧪 Running Automated Tests

```bash
pytest tests/ -v
```

### Test Coverage

- Application startup and configuration
- Dashboard metric calculations
- CSV import with duplicate prevention
- Update detection and synchronization
- Invalid row handling
- Duplicate IDs within single upload
- Manual correction persistence
- Dashboard refresh after changes
- CSV and JSON export accuracy
- Manifest generation
- Activity history recording
- Routing recommendation logic
- Transaction rollback on errors

---

## 🏗️ Project Structure

```
Revenue_intelligence_project_volopay/
├── app.py                      # Main Flask application
├── config.py                   # Configuration management
├── init_db.py                  # Database initialization
├── load_sample_data.py         # Sample data loader
├── requirements.txt            # Python dependencies
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── Procfile                    # Deployment configuration
├── README.md                   # This file
├── data_profile.md             # Dataset analysis
├── architecture.md             # System architecture
├── deployment.md               # Deployment guide
├── presentation.pptx           # Interview presentation
├── recording_script.md         # Demo narration script
├── instance/
│   └── revenueiq.db           # SQLite database
├── uploads/                    # CSV upload storage
├── exports/                    # Report export storage
├── services/
│   ├── __init__.py
│   ├── database.py            # Database operations
│   ├── analysis.py            # Conversation analysis
│   ├── routing.py             # Smart routing logic
│   ├── import_service.py      # CSV import handling
│   └── export_service.py      # Report export handling
├── templates/
│   ├── base.html              # Base template
│   ├── dashboard.html         # Dashboard page
│   ├── conversations.html     # Conversations page
│   ├── routing.html           # Routing center
│   ├── import.html            # Import page
│   ├── reports.html           # Reports page
│   ├── activity.html          # Activity history
│   └── settings.html          # Settings page
├── static/
│   ├── css/
│   │   └── style.css          # Custom styles
│   └── js/
│       └── main.js            # JavaScript functions
└── tests/
    ├── __init__.py
    ├── conftest.py            # Pytest fixtures
    ├── test_app.py            # Application tests
    ├── test_import.py         # Import tests
    ├── test_export.py         # Export tests
    └── test_routing.py        # Routing tests
```

---

## 🌐 Deployment

### Preparation Checklist

- [ ] Set `FLASK_ENV=production` in `.env`
- [ ] Generate strong `SECRET_KEY`
- [ ] Configure production database (or use SQLite with persistent storage)
- [ ] Set up file storage for uploads and exports
- [ ] Configure HTTPS/SSL
- [ ] Set appropriate file upload size limits
- [ ] Enable security headers
- [ ] Test all features in production environment

### Deployment Platforms

**Heroku:**
```bash
heroku create your-app-name
heroku config:set SECRET_KEY=your-secret-key
heroku config:set FLASK_ENV=production
git push heroku main
```

**Railway:**
- Connect GitHub repository
- Set environment variables
- Deploy automatically

**Render:**
- Create new Web Service
- Connect repository
- Set environment variables
- Deploy

**DigitalOcean App Platform:**
- Create new app from GitHub
- Configure environment variables
- Deploy

See `deployment.md` for detailed instructions.

---

## 🔒 Security Considerations

- **Input Validation**: All user inputs are validated
- **SQL Injection Protection**: Parameterized queries throughout
- **File Upload Security**: Type and size validation
- **Environment Variables**: Sensitive data not hardcoded
- **CSRF Protection**: Flask-WTF integration recommended for production
- **Error Handling**: Safe error messages without exposing internals

---

## 🐛 Troubleshooting

### Database Locked Error
```bash
# Close all connections and restart
python init_db.py
```

### Import Fails with "Invalid CSV"
- Ensure CSV has required columns
- Check date format: YYYY-MM-DD HH:MM:SS
- Verify file encoding: UTF-8

### Charts Not Displaying
- Clear browser cache
- Check browser console for JavaScript errors
- Ensure Chart.js loaded correctly

### Tests Failing
- Ensure test database is clean: `pytest --create-db`
- Check Python version compatibility
- Verify all dependencies installed

---

## 📈 Limitations & Future Enhancements

### Current Limitations
- **Sample Data**: Uses synthetic data for demonstration
- **Sentiment Analysis**: Rule-based keyword matching (not ML)
- **No Real AI**: Analysis based on transparent business rules
- **Single User**: No authentication system implemented
- **Local Storage**: SQLite suitable for demo, consider PostgreSQL for production

### Potential Enhancements
- User authentication and role-based access
- Real-time notifications via WebSocket
- Advanced ML-based sentiment analysis
- Integration with CRM systems (Salesforce, HubSpot)
- Mobile app development
- Multi-language support
- Advanced analytics and forecasting

---

## 📝 Interview Assignment Verification

### Completed Requirements ✅

- [x] Professional SaaS design (deep navy, indigo, cyan, rounded cards)
- [x] Responsive layouts (desktop, tablet, mobile)
- [x] Functional dashboard with real KPI calculations
- [x] Interactive Chart.js visualizations from database
- [x] Searchable, filterable, sortable conversations
- [x] Transparent rule-based analysis (sentiment, signals)
- [x] Smart routing with recommendations and evidence
- [x] CSV import with duplicate prevention
- [x] Update detection and synchronization
- [x] Manual correction preservation
- [x] Row-level error reporting
- [x] Import history with accurate totals
- [x] Transaction rollback on failures
- [x] CSV and JSON exports
- [x] Manifest generation
- [x] Activity history audit trail
- [x] Persistent SQLite database
- [x] Automated pytest tests
- [x] Professional documentation
- [x] Interview presentation materials
- [x] Deployment preparation

### Test Results Summary
- See test execution output for detailed results
- All critical features tested and verified
- Edge cases handled appropriately

---

## 👨‍💻 Developer

**Project**: Revenue Intelligence Inbox (RevenueIQ)  
**Company**: Lazy Blooms  
**Purpose**: Interview Assignment  
**Technology Stack**: Python, Flask, SQLite, Pandas, HTML5, CSS3, Bootstrap 5, JavaScript, Chart.js, pytest

---

## 📄 License

This project is created for interview assignment purposes.

---

## 🤝 Support

For questions or issues, please refer to the documentation files:
- `architecture.md` - System design details
- `data_profile.md` - Dataset structure
- `deployment.md` - Deployment guide
- `recording_script.md` - Demo walkthrough

---

**Built with ❤️ for Lazy Blooms Interview Assignment**
