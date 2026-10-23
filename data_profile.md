# Data Profile: Revenue Intelligence Inbox Dataset

**Generated**: 2026-10-23  
**Purpose**: Interview Assignment Dataset Analysis  
**Status**: Using Synthetic Sample Data

---

## 📊 Dataset Overview

Since no original dataset was found in the workspace, this application uses **clearly labeled synthetic sample data** for demonstration purposes.

**Important**: All findings and metrics in this profile are based on synthetic data created specifically for this interview assignment. These are NOT real business findings.

---

## 🗂️ Synthetic Dataset Structure

### Primary Table: `conversations`

| Column Name | Data Type | Description | Nullable | Example |
|------------|-----------|-------------|----------|---------|
| `id` | INTEGER | Primary key (auto-increment) | No | 1, 2, 3 |
| `conversation_id` | TEXT | Unique stable identifier | No | CALL-001, MEET-045 |
| `customer_name` | TEXT | Customer's full name | No | John Smith, Acme Corp |
| `customer_phone` | TEXT | Phone number | Yes | +1-555-0123 |
| `customer_email` | TEXT | Email address | Yes | john@example.com |
| `customer_company` | TEXT | Company name | Yes | Acme Corporation |
| `employee_name` | TEXT | Assigned employee | Yes | Sarah Johnson |
| `conversation_type` | TEXT | "Call" or "Meeting" | No | Call |
| `timestamp` | DATETIME | Conversation date/time | No | 2026-10-15 14:30:00 |
| `transcript` | TEXT | Full conversation content | No | "Customer asked about..." |
| `summary` | TEXT | Brief summary | Yes | Short overview |
| `sentiment` | TEXT | Positive/Neutral/Negative | Yes | Positive |
| `priority` | TEXT | Low/Medium/High/Urgent | Yes | High |
| `status` | TEXT | Open/In Progress/Completed | Yes | Open |
| `assigned_team` | TEXT | Recommended/assigned team | Yes | Sales |
| `assigned_employee` | TEXT | Specific employee | Yes | Sarah Johnson |
| `next_action` | TEXT | Recommended action | Yes | Schedule demo |
| `routing_reason` | TEXT | Why this routing | Yes | Purchase intent detected |
| `follow_up_status` | TEXT | Pending/Completed/None | Yes | Pending |
| `source` | TEXT | Import source | Yes | manual, csv_import |
| `last_updated` | DATETIME | Last modification | No | 2026-10-23 10:15:00 |

### Indexes

- `idx_conversation_id`: Unique index on `conversation_id` (prevents duplicates)
- `idx_timestamp`: Index on `timestamp` (for time-series queries)
- `idx_sentiment`: Index on `sentiment` (for filtering)
- `idx_priority`: Index on `priority` (for filtering)
- `idx_status`: Index on `status` (for filtering)
- `idx_assigned_team`: Index on `assigned_team` (for team reports)

---

## 📈 Synthetic Sample Data Statistics

### Record Counts (Sample Data)

- **Total Conversations**: ~50 records
- **Calls**: ~30 records (60%)
- **Meetings**: ~20 records (40%)
- **Date Range**: October 1-22, 2026 (3 weeks)

### Sentiment Distribution (Sample)

- **Positive**: ~25 conversations (50%)
- **Neutral**: ~15 conversations (30%)
- **Negative**: ~10 conversations (20%)

### Priority Distribution (Sample)

- **Urgent**: ~5 conversations (10%)
- **High**: ~15 conversations (30%)
- **Medium**: ~20 conversations (40%)
- **Low**: ~10 conversations (20%)

### Team Distribution (Sample)

- **Sales**: ~20 conversations (40%)
- **Technical Support**: ~15 conversations (30%)
- **Customer Success**: ~10 conversations (20%)
- **Account Management**: ~5 conversations (10%)

### Follow-Up Status (Sample)

- **Pending**: ~20 conversations (40%)
- **Completed**: ~15 conversations (30%)
- **None Required**: ~15 conversations (30%)

---

## 🔍 Data Quality Assessment

### Completeness (Synthetic Data)

- **Required Fields**: 100% complete (no nulls in required fields)
- **Customer Names**: 100% complete
- **Conversation IDs**: 100% unique and stable
- **Timestamps**: 100% valid ISO format
- **Transcripts**: 100% complete with meaningful content
- **Optional Fields**: ~70% complete (realistic for production data)

### Data Quality Issues (Intentionally None in Sample)

Since this is synthetic sample data created for demonstration:

✅ **No Missing Values** in required fields  
✅ **No Duplicate IDs** (enforced by unique constraint)  
✅ **No Invalid Dates** (all timestamps valid)  
✅ **No Empty Transcripts** (all have content)  
✅ **No Inconsistent Formatting** (standardized)

In a real production dataset, you would expect to find and document:
- Missing optional field values
- Inconsistent date formats
- Duplicate customer records
- Incomplete transcripts
- Data entry errors

---

## 🎯 Business Signals Detected (Sample Data)

The analysis engine identifies these signals in synthetic conversations:

### Purchase Intent Signals
- Keywords: "buy", "purchase", "interested in buying", "ready to order"
- Sample conversations containing these signals: ~10

### Product Demo Requests
- Keywords: "demo", "demonstration", "show me", "see how it works"
- Sample conversations: ~8

### Pricing Inquiries
- Keywords: "price", "cost", "how much", "pricing", "quote"
- Sample conversations: ~12

### Discount Requests
- Keywords: "discount", "deal", "offer", "promotion", "cheaper"
- Sample conversations: ~6

### Technical Support Issues
- Keywords: "not working", "error", "problem", "bug", "issue"
- Sample conversations: ~10

### Complaints
- Keywords: "disappointed", "frustrated", "unhappy", "complaint"
- Sample conversations: ~5

### Urgent Deadlines
- Keywords: "urgent", "asap", "immediately", "today", "emergency"
- Sample conversations: ~7

### Follow-Up Requests
- Keywords: "follow up", "call back", "get back to me", "contact me"
- Sample conversations: ~15

---

## 🔄 Import & Sync Testing Data

### CSV Import Test Scenarios

The sample dataset supports testing:

1. **Initial Import**: All 50 records inserted as new
2. **Duplicate Prevention**: Re-importing same file results in 0 new records
3. **Update Detection**: Modifying values and re-importing updates changed records
4. **Manual Corrections**: Manager edits preserved during subsequent imports
5. **Invalid Data**: Test records with missing required fields rejected
6. **Duplicate IDs in Upload**: Multiple rows with same ID in single file rejected

### Test CSV Format

```csv
conversation_id,customer_name,conversation_type,timestamp,transcript,sentiment,priority
CALL-001,John Smith,Call,2026-10-15 14:30:00,"Customer interested in premium package",Positive,High
CALL-002,Jane Doe,Call,2026-10-16 09:15:00,"Technical issue with login",Neutral,Medium
MEET-001,Acme Corp,Meeting,2026-10-17 11:00:00,"Quarterly business review meeting",Positive,Low
```

---

## 📊 Database Schema

### Conversation Table Schema

```sql
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id TEXT UNIQUE NOT NULL,
    customer_name TEXT NOT NULL,
    customer_phone TEXT,
    customer_email TEXT,
    customer_company TEXT,
    employee_name TEXT,
    conversation_type TEXT NOT NULL,
    timestamp DATETIME NOT NULL,
    transcript TEXT NOT NULL,
    summary TEXT,
    sentiment TEXT,
    priority TEXT,
    status TEXT,
    assigned_team TEXT,
    assigned_employee TEXT,
    next_action TEXT,
    routing_reason TEXT,
    follow_up_status TEXT,
    source TEXT DEFAULT 'manual',
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Import History Schema

```sql
CREATE TABLE import_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_rows INTEGER,
    successful_rows INTEGER,
    created_rows INTEGER,
    updated_rows INTEGER,
    unchanged_rows INTEGER,
    failed_rows INTEGER,
    status TEXT,
    error_details TEXT
);
```

### Activity History Schema

```sql
CREATE TABLE activity_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    action_type TEXT NOT NULL,
    conversation_id TEXT,
    description TEXT NOT NULL,
    user TEXT DEFAULT 'system',
    change_details TEXT
);
```

---

## 🎨 Sample Data Characteristics

### Realistic Conversation Patterns

The synthetic data includes:

- **Sales Calls**: Purchase inquiries, pricing questions, demo requests
- **Support Calls**: Technical issues, bug reports, help requests
- **Customer Success**: Check-ins, relationship building, upsells
- **Urgent Issues**: Complaints, deadlines, escalations

### Employee Distribution (Sample)

- Sarah Johnson (Sales): ~10 conversations
- Mike Chen (Technical Support): ~8 conversations
- Emily Rodriguez (Customer Success): ~7 conversations
- David Park (Sales): ~6 conversations
- Lisa Wang (Technical Support): ~5 conversations
- Unassigned: ~14 conversations

### Temporal Distribution (Sample)

- Week 1 (Oct 1-7): ~15 conversations
- Week 2 (Oct 8-14): ~18 conversations
- Week 3 (Oct 15-21): ~17 conversations

---

## ⚠️ Important Notes for Interview

### This is Synthetic Sample Data

**ALL findings, metrics, and examples in this profile are based on clearly labeled synthetic sample data created for demonstration purposes.**

### What This Means

1. **No Real Business Insights**: These are not actual customer conversations
2. **Demonstration Only**: Shows application capabilities, not real patterns
3. **Clearly Labeled**: All presentations mark sample data explicitly
4. **Test Scenarios**: Designed to showcase import, routing, and analysis features

### Real Dataset Integration

To use a real dataset:

1. Place CSV file in project root or `/uploads` folder
2. Use Import & Sync module to upload
3. Application will automatically:
   - Map columns to database fields
   - Validate data quality
   - Report statistics
   - Generate real metrics from actual data

---

## 📋 Column Mapping Recommendations

### Required Mappings

- `conversation_id` or `id` → `conversation_id`
- `customer_name` or `client_name` → `customer_name`
- `type` or `conversation_type` → `conversation_type`
- `date` or `timestamp` or `datetime` → `timestamp`
- `transcript` or `content` or `notes` → `transcript`

### Optional Mappings

- `phone` → `customer_phone`
- `email` → `customer_email`
- `company` → `customer_company`
- `agent` or `employee` → `employee_name`
- `sentiment` → `sentiment`
- `priority` → `priority`
- `status` → `status`

---

## ✅ Data Quality Checklist

For real datasets, validate:

- [ ] Unique conversation IDs (no duplicates)
- [ ] Valid timestamp formats
- [ ] Non-empty required fields
- [ ] Consistent conversation types
- [ ] Valid sentiment values (if provided)
- [ ] Valid priority values (if provided)
- [ ] Reasonable date ranges
- [ ] Appropriate transcript lengths
- [ ] Valid email formats (if provided)
- [ ] Valid phone formats (if provided)

---

**Profile Generated By**: RevenueIQ Data Profiler  
**Dataset Type**: Synthetic Sample Data for Interview Assignment  
**Real Data Available**: No (workspace was empty)  
**Sample Data Quality**: High (intentionally clean for demonstration)
