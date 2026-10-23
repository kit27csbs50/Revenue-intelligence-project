# RevenueIQ Quick Start Guide

**Get the application running in 5 minutes!**

---

## 🚀 Prerequisites

- Python 3.8 or higher installed
- Web browser (Chrome, Firefox, Safari, or Edge)
- Terminal/Command Prompt access

---

## ⚡ Quick Start (5 Steps)

### Step 1: Install Dependencies (2 minutes)

```bash
python -m pip install Flask pandas python-dotenv gunicorn pytest pytest-flask Werkzeug
```

### Step 2: Initialize Database (10 seconds)

```bash
python init_db.py
```

Expected output:
```
✓ Database initialized successfully
```

### Step 3: Load Sample Data (10 seconds)

```bash
python load_sample_data.py
```

Expected output:
```
✓ Successfully loaded 50 sample conversations
```

### Step 4: Start Application (5 seconds)

```bash
python app.py
```

Expected output:
```
 * Running on http://127.0.0.1:5000
```

### Step 5: Open Browser

Navigate to: **http://localhost:5000**

You should see the RevenueIQ dashboard! 🎉

---

## 🎯 What to Try First

### 1. Explore the Dashboard
- View KPI cards (calls, meetings, sentiment)
- Interact with Chart.js visualizations
- Scroll through recent activity

### 2. Browse Conversations
- Click "Conversations" in sidebar
- Use search and filters
- Click "View" on any conversation

### 3. See Smart Routing
- Click "Routing Center"
- Review evidence-based recommendations
- See routing alternatives

### 4. Test CSV Import
- Click "Import & Sync"
- Drag `sample_import.csv` to upload
- Watch import statistics
- Upload same file again to see duplicate prevention!

### 5. Export Data
- Click "Reports & Exports"
- Select "Both" format
- Click "Generate Export"
- Download CSV, JSON, and manifest files

---

## 🧪 Run Tests (Optional)

```bash
python -m pytest tests/ -v
```

Expected: 35-40 tests passing

---

## 🛑 Stop Application

Press `Ctrl+C` in the terminal running `python app.py`

---

## ❓ Troubleshooting

### Port Already in Use

If you see "Address already in use":

```bash
# Change port in app.py (last line)
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Module Not Found

If you see "ModuleNotFoundError":

```bash
# Reinstall dependencies
python -m pip install -r requirements.txt
```

### Database Error

If you see database errors:

```bash
# Reinitialize database
python init_db.py
python load_sample_data.py
```

---

## 📖 Next Steps

- Read **README.md** for full documentation
- Check **architecture.md** for technical details
- Review **deployment.md** for production deployment
- See **presentation_outline.md** for interview prep

---

## 🎬 Demo the Application

### For Interview/Presentation

1. **Dashboard** - Show real metrics from database
2. **Routing** - Pick a conversation, show evidence and reasoning
3. **Import Twice** - Upload sample_import.csv twice to prove duplicate prevention
4. **Export** - Generate and download reports

### Screen Recording

Follow the narration script in **recording_script.md** for a professional 3-minute demo.

---

## ✅ Success Checklist

- [ ] Dependencies installed
- [ ] Database initialized
- [ ] Sample data loaded
- [ ] Application running on localhost:5000
- [ ] Dashboard displays metrics
- [ ] Can browse conversations
- [ ] Can view routing recommendations
- [ ] Can import CSV file
- [ ] Can export reports
- [ ] Tests run successfully

---

**That's it! You're ready to explore RevenueIQ.** 🚀

For questions or issues, check the full README.md or troubleshooting section.
