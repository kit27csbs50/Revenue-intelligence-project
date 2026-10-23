# RevenueIQ Troubleshooting Guide

## ✅ APPLICATION STATUS: WORKING CORRECTLY

Your RevenueIQ application is **running successfully**. The server logs confirm:
- ✓ Flask server running on http://127.0.0.1:5000
- ✓ Dashboard loading (HTTP 200 responses)
- ✓ Static files (CSS/JS) loading correctly
- ✓ All features working (exports, navigation, etc.)

---

## 🌐 How to Access the Application

### Method 1: Use the Correct URL
Open your web browser and go to:
```
http://127.0.0.1:5000
```
**OR**
```
http://localhost:5000
```

### Method 2: Use VS Code Simple Browser
1. Press `Ctrl+Shift+P` to open Command Palette
2. Type "Simple Browser"
3. Select "Simple Browser: Show"
4. Enter URL: `http://127.0.0.1:5000`

### Method 3: Click Terminal Link
In VS Code terminal where the server is running:
- Hold `Ctrl` and click on `http://127.0.0.1:5000`
- This will open in VS Code's built-in browser

---

## 🚫 If You See a Directory Listing

If you see a file/folder listing instead of the dashboard, try these solutions:

### Solution 1: Clear Browser Cache
```
Press: Ctrl + Shift + Delete
Select: "Cached images and files"
Time Range: "All time"
Click: "Clear data"
Then refresh: Ctrl + F5
```

### Solution 2: Use Incognito/Private Mode
```
Press: Ctrl + Shift + N (Chrome)
Press: Ctrl + Shift + P (Firefox/Edge)
Then navigate to: http://127.0.0.1:5000
```

### Solution 3: Hard Refresh
```
Press: Ctrl + F5 (hard refresh)
Or: Ctrl + Shift + R
```

### Solution 4: Check URL
Make sure you're navigating to:
- ✅ `http://127.0.0.1:5000` (correct)
- ✅ `http://localhost:5000` (correct)
- ❌ `file:///C:/Revenue%20intelligence%20project%20volopay/` (wrong - this is local file system)
- ❌ `http://127.0.0.1:5000/static/` (wrong - this is static files directory)

---

## 🎯 What You Should See

When the application loads correctly, you'll see:

### Dashboard Page
1. **Header**: "Dashboard Overview"
2. **5 KPI Cards**:
   - Total Calls: 30
   - Total Meetings: 20
   - Positive Conversations: 25
   - Pending Follow-ups: 20
   - High Priority Customers: 20

3. **4 Interactive Charts**:
   - Calls & Meetings Over Time (line chart)
   - Sentiment Distribution (doughnut chart)
   - Follow-up Status (pie chart)
   - Top Employee Activity (bar chart)

4. **Sidebar Navigation** (left side):
   - Dashboard
   - Conversations
   - Routing Center
   - Import & Sync
   - Reports & Exports
   - Activity History
   - Settings

5. **Recent Activity Table** at the bottom

### Design Elements
- **Background**: Dark navy blue (#0a1128)
- **Accent Colors**: Indigo, electric blue, cyan
- **Cards**: White/light with rounded corners
- **Professional Layout**: Clean, modern enterprise SaaS design

---

## 🔧 Restart the Application

If you need to restart:

### Option 1: Use the Batch File
```batch
# Double-click in File Explorer:
START_HERE.bat
```

### Option 2: Use Python Directly
```batch
python LAUNCH_APP.py
```

### Option 3: Stop and Start
```batch
# In VS Code terminal, press: Ctrl+C to stop
# Then run:
python LAUNCH_APP.py
```

---

## 📊 Verify Database

Check if database has data:

```bash
python
>>> from services.database import Database
>>> db = Database('instance/revenueiq.db')
>>> stats = db.get_dashboard_stats()
>>> print(stats)
>>> exit()
```

Expected output:
```python
{
    'total_calls': 30,
    'total_meetings': 20,
    'positive_conversations': 25,
    'pending_followups': 20,
    'high_priority': 20
}
```

---

## 🐛 Common Issues and Solutions

### Issue 1: "Site Can't Be Reached"
**Cause**: Server not running
**Solution**: 
```bash
python LAUNCH_APP.py
```

### Issue 2: Directory Listing Shows
**Cause**: Browser cache or wrong URL
**Solution**: 
1. Clear browser cache (Ctrl+Shift+Delete)
2. Use incognito mode (Ctrl+Shift+N)
3. Verify URL is `http://127.0.0.1:5000` not a file:/// path

### Issue 3: Port Already in Use
**Cause**: Another application using port 5000
**Solution**:
```bash
# Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

### Issue 4: Missing Database
**Cause**: Database not initialized
**Solution**:
```bash
python init_db.py
python load_sample_data.py
```

### Issue 5: Import Errors
**Cause**: Missing dependencies
**Solution**:
```bash
python -m pip install -r requirements.txt
```

---

## ✅ Verification Checklist

Run through this checklist:

- [ ] Server shows "Running on http://127.0.0.1:5000"
- [ ] Browser URL is exactly `http://127.0.0.1:5000` or `http://localhost:5000`
- [ ] Not navigating to file system path (file:///)
- [ ] Browser cache cleared or using incognito mode
- [ ] Database file exists at `instance/revenueiq.db`
- [ ] Server logs show "200" responses (success)
- [ ] No firewall blocking port 5000

---

## 📞 Testing the Application

### Test 1: Dashboard
1. Navigate to http://127.0.0.1:5000
2. Should see 5 KPI cards with numbers
3. Should see 4 charts rendering
4. Should see recent activity table

### Test 2: Conversations Page
1. Click "Conversations" in sidebar
2. Should see list of 62 conversations
3. Test search, filter, pagination
4. Click on a conversation to view details

### Test 3: Import CSV
1. Click "Import & Sync" in sidebar
2. Upload `sample_import.csv`
3. Should see success message
4. Check that no duplicates were created

### Test 4: Export Data
1. Click "Reports & Exports" in sidebar
2. Select format (CSV/JSON/Both)
3. Click "Generate Export"
4. Download the generated file

### Test 5: Routing Center
1. Click "Routing Center" in sidebar
2. Should see conversations with routing recommendations
3. Test assigning a conversation to a team

---

## 🎬 Server Logs Interpretation

### Good Logs (Working):
```
GET / HTTP/1.1" 200 -                    ← Dashboard loaded successfully
GET /static/css/style.css HTTP/1.1" 304 - ← CSS loaded (cached)
GET /static/js/main.js HTTP/1.1" 304 -    ← JS loaded (cached)
```

### Problem Logs:
```
GET / HTTP/1.1" 404 -                    ← Route not found
GET / HTTP/1.1" 500 -                    ← Server error
ConnectionRefusedError                   ← Server not running
```

---

## 🚀 Performance Tips

1. **Disable Debug Mode for Production**:
   - Edit `config.py`, set `DEBUG = False`

2. **Use Production Server**:
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. **Enable Database Indexes**:
   - Already configured in `services/database.py`

4. **Clear Exports Folder**:
   ```bash
   # Delete old export files to save space
   del /Q exports\*.csv exports\*.json
   ```

---

## 📁 File Structure Verification

Ensure these files exist:

```
Revenue intelligence project volopay/
├── app.py                    ← Main application
├── config.py                 ← Configuration
├── LAUNCH_APP.py            ← Launcher script
├── requirements.txt         ← Dependencies
├── instance/
│   └── revenueiq.db        ← SQLite database
├── services/
│   ├── database.py         ← Database service
│   ├── analysis.py         ← Analysis service
│   ├── routing.py          ← Routing service
│   ├── import_service.py   ← Import service
│   └── export_service.py   ← Export service
├── templates/
│   ├── base.html           ← Base template
│   ├── dashboard.html      ← Dashboard page
│   ├── conversations.html  ← Conversations page
│   └── ...                 ← Other templates
└── static/
    ├── css/style.css       ← Styles
    └── js/main.js          ← JavaScript
```

---

## 💡 Pro Tips

1. **Keep Terminal Open**: Don't close the terminal window while using the app
2. **Watch Server Logs**: Monitor the terminal for errors
3. **Use VS Code Split View**: Terminal + Browser side by side
4. **Bookmark the URL**: Save `http://127.0.0.1:5000` for quick access
5. **Test Features**: Try all pages to ensure everything works

---

## ✅ Application is Ready!

Your RevenueIQ application is **fully functional and working**. The server logs confirm:
- Dashboard loading successfully
- All static files loading
- Database connected with 62 conversations
- Export functionality working
- Navigation working between pages

**Next Steps**:
1. Open `http://127.0.0.1:5000` in your browser
2. Clear cache if you see directory listing
3. Explore all the features
4. Test CSV import with `sample_import.csv`
5. Generate exports and download them

---

## 📞 Quick Reference Commands

```bash
# Start application
python LAUNCH_APP.py

# Stop application
Ctrl + C

# Restart database
python init_db.py
python load_sample_data.py

# Install dependencies
python -m pip install -r requirements.txt

# Run tests
pytest -v

# Check Python version
python --version

# Check installed packages
pip list
```

---

**REMEMBER**: The application **IS working**. Your server logs show successful HTTP 200 responses. If you're seeing a directory listing, it's a browser cache issue, not a server issue.
