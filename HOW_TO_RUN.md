# 🚀 How to Run RevenueIQ

## ⚡ EASIEST METHOD - Double Click to Start

### For Windows Users:
1. **Double-click** `START_HERE.bat` in File Explorer
2. A window will open showing the server starting
3. **Open your browser** to: http://localhost:5000

---

## 🖥️ METHOD 2 - Using VS Code Terminal

### Step 1: Open Terminal in VS Code
- Press `` Ctrl + ` `` (backtick key)
- Or go to: **Terminal** → **New Terminal**

### Step 2: Run the Application
Type this command and press Enter:

```bash
python quick_start.py
```

### Step 3: Open Browser
Once you see "Starting Flask development server...", open your browser to:

**http://localhost:5000**

---

## 🌐 METHOD 3 - Run Directly

```bash
python app.py
```

Then open: http://localhost:5000

---

## 🎯 What You'll See

When you open http://localhost:5000, you should see:

### RevenueIQ Dashboard with:
- ✅ Navigation bar with logo
- ✅ Sidebar menu (Overview, Conversations, Routing, etc.)
- ✅ 5 KPI cards showing metrics
- ✅ 4 interactive charts
- ✅ Recent activity feed

---

## 🐛 Troubleshooting

### If you see a "directory listing" instead of the app:

1. **Stop any running Python processes**:
   ```bash
   taskkill /F /IM python.exe
   ```

2. **Clear browser cache**: Press `Ctrl + Shift + Delete`, clear cached files

3. **Try incognito mode**: Press `Ctrl + Shift + N` (Chrome/Edge)

4. **Restart the app**:
   ```bash
   python quick_start.py
   ```

### If you get "Module not found" errors:

```bash
python -m pip install Flask pandas python-dotenv pytest pytest-flask Werkzeug
```

### If you get "Database" errors:

```bash
python init_db.py
python load_sample_data.py
```

---

## 🛑 How to Stop the Server

- Press **`Ctrl + C`** in the terminal/command window
- Or close the command window

---

## 📱 Test the Features

Once the app is running, try:

1. **Dashboard** - View KPIs and charts
2. **Conversations** - Browse and search conversations
3. **Routing Center** - See smart routing recommendations
4. **Import & Sync** - Upload `sample_import.csv` twice to test duplicate prevention
5. **Reports & Exports** - Generate CSV, JSON, and manifest files

---

## ✅ Expected URLs

Your application should be accessible at:
- http://localhost:5000 ← **Use this**
- http://127.0.0.1:5000
- http://[your-ip]:5000

---

## 🆘 Still Having Issues?

Make sure you're in the correct directory:

```bash
cd "C:\Revenue intelligence project volopay"
```

Then run:

```bash
python quick_start.py
```

And open: **http://localhost:5000**

---

**The application MUST be running in the terminal for the browser to work!**

Keep the terminal window open while using the application.
