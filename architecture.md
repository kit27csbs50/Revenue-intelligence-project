# RevenueIQ Architecture Documentation

**Project**: Revenue Intelligence Inbox  
**Version**: 1.0  
**Date**: October 23, 2026

---

## 🏗️ System Architecture Overview

RevenueIQ follows a modular Flask application architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                        Web Browser                          │
│              (HTML5, CSS3, Bootstrap 5, Chart.js)           │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTPS
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Flask Application                        │
│                        (app.py)                             │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Routes     │  │  Templates   │  │   Static     │     │
│  │  Handlers    │  │   (Jinja2)   │  │   Assets     │     │
│  └──────┬───────┘  └──────────────┘  └──────────────┘     │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Service Layer                          │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  • database.py    - DB operations                   │   │
│  │  • analysis.py    - Conversation analysis           │   │
│  │  • routing.py     - Smart routing logic             │   │
│  │  • import_service.py - CSV import handling          │   │
│  │  • export_service.py - Report generation            │   │
│  └─────────────────────┬───────────────────────────────┘   │
└────────────────────────┼───────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   SQLite Database                           │
│                  (instance/revenueiq.db)                    │
├─────────────────────────────────────────────────────────────┤
│  • conversations        - Main conversation data            │
│  • import_history       - CSV import tracking               │
│  • activity_history     - Audit trail                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Directory Structure

```
Revenue_intelligence_project_volopay/
│
├── 📄 app.py                      # Main Flask application and routes
├── 📄 config.py                   # Configuration management
├── 📄 init_db.py                  # Database initialization script
├── 📄 load_sample_data.py         # Sample data loader
├── 📄 requirements.txt            # Python dependencies
├── 📄 .env.example                # Environment variable template
├── 📄 .gitignore                  # Git ignore rules
├── 📄 Procfile                    # Deployment configuration
│
├── 📁 instance/                   # SQLite database storage
│   └── revenueiq.db              # Main database file
│
├── 📁 uploads/                    # CSV file uploads
│   └── (user-uploaded CSVs)
│
├── 📁 exports/                    # Generated reports
│   ├── (CSV exports)
│   ├── (JSON exports)
│   └── manifest.json
│
├── 📁 services/                   # Business logic layer
│   ├── __init__.py
│   ├── database.py               # Database CRUD operations
│   ├── analysis.py               # Conversation analysis engine
│   ├── routing.py                # Smart routing recommendations
│   ├── import_service.py         # CSV import with duplicate handling
│   └── export_service.py         # CSV/JSON export generation
│
├── 📁 templates/                  # Jinja2 HTML templates
│   ├── base.html                 # Base template with navbar/sidebar
│   ├── dashboard.html            # Main dashboard
│   ├── conversations.html        # Conversation management
│   ├── routing.html              # Routing center
│   ├── import.html               # Import & sync page
│   ├── reports.html              # Export reports page
│   ├── activity.html             # Activity history
│   └── settings.html             # Settings page
│
├── 📁 static/                     # Static assets
│   ├── css/
│   │   └── style.css             # Custom CSS styles
│   └── js/
│       └── main.js               # JavaScript functions
│
└── 📁 tests/                      # Automated tests
    ├── __init__.py
    ├── conftest.py               # Pytest fixtures and configuration
    ├── test_app.py               # Application route tests
    ├── test_import.py            # Import functionality tests
    ├── test_export.py            # Export functionality tests
    └── test_routing.py           # Routing logic tests
```

---

## 🔧 Technology Stack

### Backend
- **Framework**: Flask 2.3.x
- **Language**: Python 3.8+
- **Database**: SQLite 3.x
- **Data Processing**: Pandas 2.x
- **Testing**: pytest 7.x

### Frontend
- **HTML**: HTML5 semantic markup
- **CSS**: CSS3 with custom properties
- **Framework**: Bootstrap 5.3.x
- **Icons**: Bootstrap Icons 1.11.x
- **Charts**: Chart.js 4.x
- **JavaScript**: ES6+ vanilla JavaScript

### Deployment
- **Server**: Gunicorn (production)
- **Platform**: Flask-compatible hosting (Heroku, Railway, Render, DigitalOcean)

---

## 📊 Database Schema

### Conversations Table

Primary table storing all customer conversation data.

```sql
CREATE TABLE conversations (
    -- Primary Key
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    -- Unique Stable Identifier
    conversation_id TEXT UNIQUE NOT NULL,
    
    -- Customer Information
    customer_name TEXT NOT NULL,
    customer_phone TEXT,
    customer_email TEXT,
    customer_company TEXT,
    
    -- Employee Assignment
    employee_name TEXT,
    
    -- Conversation Metadata
    conversation_type TEXT NOT NULL,  -- 'Call' or 'Meeting'
    timestamp DATETIME NOT NULL,
    
    -- Content
    transcript TEXT NOT NULL,
    summary TEXT,
    
    -- Analysis Results
    sentiment TEXT,              -- 'Positive', 'Neutral', 'Negative'
    priority TEXT,               -- 'Low', 'Medium', 'High', 'Urgent'
    status TEXT,                 -- 'Open', 'In Progress', 'Completed'
    
    -- Routing Information
    assigned_team TEXT,
    assigned_employee TEXT,
    next_action TEXT,
    routing_reason TEXT,
    follow_up_status TEXT,       -- 'Pending', 'Completed', 'None'
    
    -- Audit Fields
    source TEXT DEFAULT 'manual',
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for Performance
CREATE UNIQUE INDEX idx_conversation_id ON conversations(conversation_id);
CREATE INDEX idx_timestamp ON conversations(timestamp);
CREATE INDEX idx_sentiment ON conversations(sentiment);
CREATE INDEX idx_priority ON conversations(priority);
CREATE INDEX idx_status ON conversations(status);
CREATE INDEX idx_assigned_team ON conversations(assigned_team);
```

### Import History Table

Tracks all CSV import operations with detailed statistics.

```sql
CREATE TABLE import_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Import Statistics
    total_rows INTEGER,
    successful_rows INTEGER,
    created_rows INTEGER,      -- New records inserted
    updated_rows INTEGER,      -- Existing records updated
    unchanged_rows INTEGER,    -- Duplicates skipped
    failed_rows INTEGER,       -- Invalid records rejected
    
    -- Status
    status TEXT,               -- 'completed', 'partial', 'failed'
    error_details TEXT         -- JSON array of row-level errors
);
```

### Activity History Table

Audit trail for all system and user actions.

```sql
CREATE TABLE activity_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Action Information
    action_type TEXT NOT NULL, -- 'import', 'update', 'export', 'routing', etc.
    conversation_id TEXT,      -- Related conversation (if applicable)
    
    -- Description
    description TEXT NOT NULL,
    user TEXT DEFAULT 'system',
    change_details TEXT        -- JSON object with before/after values
);

CREATE INDEX idx_activity_timestamp ON activity_history(timestamp);
CREATE INDEX idx_activity_type ON activity_history(action_type);
```

---

## 🔄 Data Flow

### 1. CSV Import Flow

```
User uploads CSV
      ↓
File validation (size, type, encoding)
      ↓
Pandas reads CSV into DataFrame
      ↓
Column mapping (flexible field names)
      ↓
Row-by-row validation
      ↓
For each valid row:
  ├─ Check if conversation_id exists
  │  ├─ Exists + values unchanged → Skip (unchanged)
  │  ├─ Exists + values changed → Update (updated)
  │  └─ Not exists → Insert (created)
  └─ Record in import_history
      ↓
Generate error report for invalid rows
      ↓
Return import statistics
      ↓
Log activity in activity_history
```

### 2. Conversation Analysis Flow

```
Conversation data received
      ↓
Extract transcript text
      ↓
Analyze sentiment (keyword-based)
  ├─ Positive keywords: great, excellent, happy, satisfied
  ├─ Negative keywords: disappointed, frustrated, unhappy, problem
  └─ Default: Neutral
      ↓
Detect business signals
  ├─ Purchase intent: buy, purchase, order
  ├─ Demo request: demo, demonstration, show
  ├─ Pricing inquiry: price, cost, quote
  ├─ Technical issue: error, bug, not working
  ├─ Complaint: complaint, unhappy, frustrated
  ├─ Urgent: urgent, asap, immediately
  └─ Follow-up: follow up, call back, contact me
      ↓
Return analysis results with evidence
```

### 3. Smart Routing Flow

```
Conversation analysis results
      ↓
Prioritize signals by urgency
      ↓
Determine recommended team:
  ├─ Technical keywords → Technical Support
  ├─ Purchase/pricing keywords → Sales
  ├─ Complaint/escalation → Customer Success
  ├─ General inquiry → Account Management
  └─ Ambiguous → Default team based on priority
      ↓
Determine priority:
  ├─ Urgent keywords → Urgent
  ├─ Technical issue + negative → High
  ├─ Purchase intent → High
  ├─ Complaint → High
  ├─ Follow-up request → Medium
  └─ Default → Low/Medium based on context
      ↓
Generate routing reason with evidence
      ↓
Recommend next action
      ↓
Return routing recommendation
```

### 4. Report Export Flow

```
User selects export format (CSV/JSON)
      ↓
Apply filters (if any)
      ↓
Query database with filters
      ↓
Generate export file:
  ├─ CSV: Pandas DataFrame.to_csv()
  └─ JSON: Custom serialization with datetime handling
      ↓
Save file to exports/ directory
      ↓
Generate manifest.json with metadata
      ↓
Log export in activity_history
      ↓
Return download links
```

---

## 🔐 Security Architecture

### Input Validation
- **File Uploads**: Type validation, size limits (16MB default)
- **CSV Data**: Required field validation, type checking, format validation
- **User Inputs**: Server-side validation on all form submissions

### SQL Injection Protection
- **Parameterized Queries**: All SQL uses parameterized queries via SQLite connector
- **No String Interpolation**: No SQL built with f-strings or concatenation

### File Security
- **Upload Directory**: Restricted to uploads/ with validation
- **Export Directory**: Restricted to exports/ with controlled access
- **Path Traversal Protection**: Filename sanitization

### Environment Variables
- **Sensitive Data**: SECRET_KEY, database credentials in .env
- **Not Committed**: .env excluded via .gitignore
- **Template Provided**: .env.example for setup guidance

### Error Handling
- **User-Friendly Messages**: No stack traces or internal details exposed
- **Logging**: Errors logged server-side for debugging
- **Graceful Degradation**: Application continues on non-critical errors

---

## 📈 Performance Considerations

### Database Optimization
- **Indexes**: Key fields indexed for fast queries
- **Unique Constraints**: conversation_id prevents duplicates at DB level
- **Connection Pooling**: SQLite connection reuse

### Query Optimization
- **Selective Queries**: Only fetch required columns
- **Pagination**: Large datasets paginated (20 records per page)
- **Caching**: Dashboard metrics could be cached (future enhancement)

### File Handling
- **Streaming**: Large CSVs processed in chunks
- **Temporary Storage**: Files cleaned up after processing
- **Size Limits**: Configurable upload size limits

### Frontend Optimization
- **CDN Assets**: Bootstrap, Chart.js loaded from CDN
- **Lazy Loading**: Charts rendered only when visible
- **Minimal JavaScript**: Vanilla JS, no heavy frameworks

---

## 🧪 Testing Strategy

### Unit Tests
- **Service Layer**: Test analysis, routing, import logic in isolation
- **Database Operations**: Test CRUD operations with temporary databases

### Integration Tests
- **Import Flow**: Test complete CSV import with various scenarios
- **Export Flow**: Test CSV and JSON generation with filters
- **Routing Flow**: Test end-to-end routing recommendations

### Test Scenarios
- ✅ Initial CSV import (all new records)
- ✅ Duplicate prevention (same file twice)
- ✅ Update detection (modified values)
- ✅ Manual correction preservation
- ✅ Invalid row rejection
- ✅ Duplicate IDs in single upload
- ✅ Transaction rollback on failure
- ✅ Dashboard metric accuracy
- ✅ Export file correctness
- ✅ Manifest generation

### Test Database
- **Isolation**: Each test uses temporary database
- **Cleanup**: Database deleted after test completion
- **Fixtures**: Reusable test data via pytest fixtures

---

## 🚀 Deployment Architecture

### Development Environment
```
Local Machine
  ├─ Flask development server (port 5000)
  ├─ SQLite database (instance/revenueiq.db)
  ├─ File uploads (uploads/)
  └─ Debug mode enabled
```

### Production Environment
```
Cloud Platform (Heroku/Railway/Render)
  ├─ Gunicorn WSGI server (4 workers)
  ├─ Persistent SQLite or PostgreSQL
  ├─ Environment variables (SECRET_KEY, etc.)
  ├─ HTTPS/SSL enabled
  ├─ File storage (persistent volumes or S3)
  └─ Production mode (debug disabled)
```

### Scalability Considerations

**Current Architecture (Single Server)**
- Suitable for: 1-100 concurrent users
- Database: SQLite (sufficient for demos/small teams)
- File Storage: Local filesystem

**Future Scaling (If Needed)**
- **Database**: Migrate to PostgreSQL for better concurrency
- **File Storage**: Move to S3/Azure Blob Storage
- **Application**: Multiple Gunicorn workers or containers
- **Caching**: Redis for dashboard metrics
- **Queue**: Celery for background import processing
- **Load Balancer**: Multiple application servers

---

## 🔄 Conversation Analysis Engine

### Rule-Based Approach

The analysis engine uses **transparent business rules** rather than claiming advanced AI:

#### Sentiment Analysis
```python
# Positive indicators
positive_keywords = ['great', 'excellent', 'happy', 'satisfied', 'pleased', 
                     'wonderful', 'fantastic', 'amazing', 'perfect', 'thank you']

# Negative indicators
negative_keywords = ['disappointed', 'frustrated', 'unhappy', 'angry', 'upset',
                     'terrible', 'worst', 'horrible', 'complaint', 'refund']

# Scoring approach
positive_score = count_keyword_matches(text, positive_keywords)
negative_score = count_keyword_matches(text, negative_keywords)

if positive_score > negative_score:
    sentiment = 'Positive'
elif negative_score > positive_score:
    sentiment = 'Negative'
else:
    sentiment = 'Neutral'
```

#### Business Signal Detection
```python
signals = {
    'purchase_intent': ['buy', 'purchase', 'order', 'interested in buying'],
    'demo_request': ['demo', 'demonstration', 'show me', 'see how'],
    'pricing_inquiry': ['price', 'cost', 'how much', 'quote', 'pricing'],
    'discount_request': ['discount', 'deal', 'offer', 'promotion'],
    'technical_issue': ['error', 'bug', 'not working', 'problem', 'issue'],
    'complaint': ['complaint', 'disappointed', 'unhappy', 'frustrated'],
    'urgent': ['urgent', 'asap', 'immediately', 'emergency', 'critical'],
    'follow_up': ['follow up', 'call back', 'contact me', 'get back']
}

detected_signals = []
for signal_type, keywords in signals.items():
    if any(keyword in text.lower() for keyword in keywords):
        detected_signals.append(signal_type)
        # Extract evidence (sentence containing keyword)
```

### Why Rule-Based?

**Advantages:**
- ✅ Transparent and explainable
- ✅ No training data required
- ✅ Fast and deterministic
- ✅ Easy to customize and extend
- ✅ No model deployment complexity

**Limitations:**
- ⚠️ Limited to predefined patterns
- ⚠️ May miss nuanced language
- ⚠️ Requires manual rule updates

**For Interview Assignment:**
- Demonstrates understanding of business logic
- Shows honest technical approach
- Avoids false AI claims
- Suitable for prototype/demo

---

## 🎯 Design Decisions

### 1. SQLite vs PostgreSQL
**Decision**: SQLite  
**Rationale**: Sufficient for interview assignment, easy setup, no external dependencies  
**Future**: Migrate to PostgreSQL for production scale

### 2. Server-Side Rendering vs SPA
**Decision**: Server-side (Jinja2 templates)  
**Rationale**: Simpler architecture, better SEO, faster initial load  
**Trade-off**: Less dynamic UI than React/Vue

### 3. Rule-Based vs ML Analysis
**Decision**: Rule-based keyword matching  
**Rationale**: Transparent, explainable, no training data required  
**Trade-off**: Less sophisticated than ML models

### 4. Synchronous vs Asynchronous Import
**Decision**: Synchronous processing  
**Rationale**: Simpler implementation, acceptable for demo-sized datasets  
**Future**: Add Celery for large file processing

### 5. Local File Storage vs Cloud Storage
**Decision**: Local filesystem  
**Rationale**: Simpler for development and demo  
**Future**: S3/Azure Blob for production

---

## 📚 API Endpoints (Internal Routes)

### Dashboard
- `GET /` - Main dashboard with KPIs and charts

### Conversations
- `GET /conversations` - List conversations (with filters, pagination)
- `GET /conversation/<id>` - View single conversation details
- `POST /conversation/<id>/update` - Update conversation fields
- `POST /conversation/<id>/correct` - Manual correction (preserves changes)

### Routing
- `GET /routing` - Routing center with recommendations
- `POST /routing/<id>/assign` - Manually assign team/employee

### Import & Sync
- `GET /import` - Import page
- `POST /import/upload` - Upload and process CSV
- `GET /import/history` - View import history
- `GET /import/errors/<import_id>` - Download error report

### Reports & Exports
- `GET /reports` - Reports page
- `POST /reports/export` - Generate export (CSV/JSON)
- `GET /reports/download/<filename>` - Download export file
- `GET /reports/manifest` - Download manifest.json

### Activity History
- `GET /activity` - View activity history (with filters)

### Settings
- `GET /settings` - Application settings

---

## 🎨 Design System

### Color Palette
- **Background**: Deep Navy (#0a1128)
- **Primary**: Indigo (#4f46e5)
- **Accent**: Electric Blue (#3b82f6)
- **Highlight**: Cyan (#06b6d4)
- **Success**: Emerald (#10b981)
- **Warning**: Amber (#f59e0b)
- **Danger**: Rose (#ef4444)
- **Text**: White/Light Gray (#f1f5f9)

### Typography
- **Headings**: Inter (sans-serif)
- **Body**: System fonts optimized for readability
- **Code**: Monospace (for conversation IDs)

### Components
- **Cards**: Rounded corners (0.75rem), subtle shadows
- **Buttons**: Rounded, gradient hover effects
- **Forms**: Clean inputs with focus states
- **Charts**: Dark theme, color-blind friendly palette

### Responsive Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

---

## ✅ Architecture Validation

### Completed Requirements
- ✅ Modular service-oriented architecture
- ✅ Clear separation of concerns (routes, services, data)
- ✅ Persistent relational database with proper schema
- ✅ Indexed queries for performance
- ✅ Transaction-safe import operations
- ✅ Comprehensive error handling
- ✅ Security best practices (parameterized SQL, input validation)
- ✅ Testable design with dependency injection
- ✅ Scalable file handling
- ✅ Professional frontend architecture
- ✅ Responsive design system
- ✅ Documented API routes

### Future Enhancements
- Authentication and authorization
- WebSocket for real-time updates
- Background job processing (Celery)
- Caching layer (Redis)
- API versioning
- Rate limiting
- Comprehensive logging framework

---

**Document Maintained By**: RevenueIQ Development Team  
**Last Updated**: October 23, 2026  
**Version**: 1.0
