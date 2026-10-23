# RevenueIQ Screen Recording Script

**Duration**: 3 minutes  
**Purpose**: Demonstrate key features for interview assignment  
**Date**: October 23, 2026

---

## 🎬 Recording Setup

**Before Recording:**
- [ ] Open application at http://localhost:5000
- [ ] Clear browser cache and cookies
- [ ] Zoom browser to 100%
- [ ] Close unnecessary tabs and applications
- [ ] Prepare CSV file for import demo
- [ ] Test microphone audio levels
- [ ] Have water nearby for smooth narration

**Recording Tools:**
- OBS Studio (free)
- Loom (simple)
- Camtasia (professional)
- Built-in screen recorder

---

## 📝 Full Narration Script

### SEGMENT 1: Introduction & Dashboard (0:00 - 0:45)

**[Open browser to dashboard]**

> "Hello! Welcome to RevenueIQ - Revenue Intelligence Inbox, my interview assignment submission for Lazy Blooms. This is a complete, functional web application built with Python, Flask, SQLite, and modern web technologies.

> Let's start with the dashboard. Here you can see real KPI cards calculated from actual database records - we have 30 calls, 20 meetings, 25 positive conversations, 20 pending follow-ups, and 20 high-priority customers. 

> Below that, we have interactive Chart.js visualizations showing calls and meetings over time, sentiment distribution, follow-up status, and employee activity. All of these metrics are dynamically calculated from the database - there are no hardcoded fake values.

> At the bottom, you can see our recent activity log tracking all system operations."

**[Scroll through dashboard slowly]**

---

### SEGMENT 2: Conversation Analysis & Routing (0:45 - 1:30)

**[Click on "Routing Center" in sidebar]**

> "Now let's look at the Smart Routing Center. This demonstrates our transparent, rule-based conversation analysis engine.

> Here's a conversation from John Smith who says: 'I am very interested in purchasing your premium package. Can you send me a quote?'

**[Scroll to show transcript]**

> The system automatically detected positive sentiment with keywords like 'interested' and 'premium'. It identified business signals including purchase intent and pricing inquiry.

**[Point to routing recommendation]**

> Based on this analysis, the system recommends routing to the Sales team with High priority. The reasoning is clear: 'Routed to Sales: Customer expressed interest in purchasing; Customer inquired about pricing.'

**[Scroll to alternatives section]**

> We also show alternative routing options that were considered but rejected. For example, this could have gone to Account Management as a general inquiry, but Sales is better equipped for purchase intent.

> This demonstrates honest, explainable AI - we're using keyword-based rules, not false claims of advanced machine learning."

---

### SEGMENT 3: Manual Correction (1:30 - 1:50)

**[Click "View Full Details" or navigate to a conversation]**

> "Let's view a conversation in detail and make a manual correction.

**[Scroll down to edit form]**

> Here I can edit any field - let me change the sentiment from Positive to Neutral, and the priority from High to Medium.

**[Make the changes and click Save]**

> And save. This manual correction is now preserved in the system. When we import CSV data later, these manual edits won't be overwritten - the system respects manager decisions."

---

### SEGMENT 4: CSV Import - Duplicate Prevention (1:50 - 2:20)

**[Navigate to Import & Sync page]**

> "Now for the most important feature: CSV import with duplicate prevention. 

**[Click or drag CSV file]**

> I'm uploading a CSV file with conversation data. The system validates the file, maps columns automatically, and processes each row.

**[Wait for import to complete]**

> Great! The first import created 50 new records. All successful.

**[Upload the same file again]**

> Now watch what happens when I import the exact same file again...

**[Wait for second import]**

> Perfect! Zero new records created, 50 unchanged records skipped. This proves our duplicate prevention works correctly - the system uses the conversation_id as a unique identifier and skips records that haven't changed."

---

### SEGMENT 5: Update Detection (2:20 - 2:35)

**[Upload modified CSV if prepared, or explain]**

> "If I were to modify values in that CSV - for example, changing a customer name or transcript - and import it again, the system would detect those changes and update only the modified records. This demonstrates our smart synchronization feature."

---

### SEGMENT 6: Export & Manifest (2:35 - 2:55)

**[Navigate to Reports & Exports]**

> "Finally, let's generate exports. I'll select 'Both' to export in CSV and JSON formats with a manifest file.

**[Click Generate Export and wait]**

> Excellent! The system generated three files: a CSV export, a JSON export, and a manifest.json file.

**[Click to download manifest.json]**

> The manifest contains accurate metadata about the exports - filenames, formats, record counts, generation timestamps, and any filters applied. Everything is based on real exported data, not fake numbers.

**[Show available exports list]**

> All export files are listed here with their sizes and creation dates, ready for download."

---

### SEGMENT 7: Conclusion (2:55 - 3:00)

**[Navigate back to dashboard or show activity history]**

> "That's RevenueIQ! A complete, professional revenue intelligence application with:
> - Real-time analytics from actual database records
> - Transparent rule-based conversation analysis
> - Evidence-based routing recommendations
> - Duplicate-safe CSV imports with update detection
> - Manual correction preservation
> - Professional export functionality with manifests
> - Complete audit trail in the activity history

> The application includes automated pytest tests, comprehensive documentation, deployment instructions, and is ready for production use.

> Thank you for watching, and thank you to Lazy Blooms for this opportunity!"

**[End recording]**

---

## 🎯 Key Points to Emphasize

1. **Real Data**: Everything calculated from database, no fake metrics
2. **Transparent Logic**: Rule-based analysis, not false AI claims
3. **Duplicate Prevention**: Proven with same-file import test
4. **Update Detection**: Smart synchronization of changed records
5. **Manual Corrections**: Preserved during imports
6. **Professional Design**: Clean, responsive, enterprise-quality UI
7. **Complete System**: Tests, documentation, deployment-ready
8. **Honest Approach**: No fake analytics, no invented features

---

## 🎤 Narration Tips

**Pace:**
- Speak clearly and not too fast
- Pause briefly between segments
- Allow UI to load before continuing

**Tone:**
- Professional but conversational
- Confident in the technical implementation
- Honest about what the system does and doesn't do

**Timing:**
- Keep total under 3 minutes
- Don't rush through important demonstrations
- Skip or abbreviate if running long

**Visual:**
- Cursor movements should be smooth
- Highlight important elements by hovering
- Scroll slowly enough for viewers to read

---

## 🔧 Backup Plan

**If import takes too long:**
> "The system is processing the import - in the interest of time, I'll move forward. The key point is that duplicate prevention uses unique IDs to skip unchanged records."

**If export takes too long:**
> "Exports are being generated. Let me show you the activity history while we wait..."

**If something doesn't work:**
> "Let me demonstrate this feature from a different angle..." [Navigate to activity history or another working feature]

---

## 📊 Alternative: Slide-Based Presentation

If live demo is problematic, prepare slides with screenshots:

1. **Title Slide**: RevenueIQ Overview
2. **Dashboard**: Screenshot of KPIs and charts
3. **Routing**: Screenshot showing analysis and evidence
4. **Import Test**: Side-by-side screenshots of first and second import
5. **Exports**: Screenshot of manifest.json content
6. **Architecture**: System diagram
7. **Conclusion**: Feature checklist

---

## ✅ Pre-Recording Checklist

- [ ] Database initialized with sample data
- [ ] Application running on http://localhost:5000
- [ ] CSV file prepared for import (and copy for duplicate test)
- [ ] Browser cleared of other tabs
- [ ] Screen recording software tested
- [ ] Microphone working properly
- [ ] Script practiced at least twice
- [ ] Timing verified (under 3 minutes)
- [ ] Backup plan prepared
- [ ] Water nearby for smooth speech

---

## 🎬 Post-Recording

- [ ] Review recording for audio quality
- [ ] Check that all demonstrations are visible
- [ ] Verify timing is appropriate
- [ ] Trim any dead space at start/end
- [ ] Export in high quality (1080p recommended)
- [ ] Upload to appropriate platform
- [ ] Test playback before submission

---

**Good luck with your recording! You've built something impressive - now show it off with confidence!** 🚀
