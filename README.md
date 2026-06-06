# SpacedNeetCode v1.0 🚀

> Master NeetCode problems using spaced repetition. NeetCode auto-commits your solutions to GitHub, and SpacedNeetCode optimizes your review schedule for long-term retention.

A local-first, lightweight web application that helps you retain coding patterns long-term through intelligent scheduling.

---

## What is SpacedNeetCode?

**The Problem:** You solve coding problems, feel confident, then forget the patterns weeks later. When you see a similar problem, you're back to square one.

**The Solution:** SpacedNeetCode uses **spaced repetition** (SM-2 algorithm) to review problems at scientifically-optimal intervals, building genuine intuition and pattern recognition.

### How It Works

1. **Solve on [NeetCode.io](https://neetcode.io)** — Access curated problems with video explanations
2. **NeetCode auto-commits to GitHub** — Every submission is automatically pushed to your GitHub repo
3. **SpacedNeetCode scans your repo** — Extracts all solved problems and creates a review schedule
4. **You review on schedule** — Problems are due for review when your brain is ready to re-learn them
5. **Rate your attempt** — Your feedback adjusts future review intervals automatically

**Result:** You build deep, lasting coding intuition instead of memorizing and forgetting.

---

## ✨ Key Features

- **Auto-Sync from NeetCode** — Automatically scans your GitHub repo (populated by NeetCode's auto-commit feature) and extracts solved problems
- **SM-2 Spaced Repetition** — Intelligently schedules reviews based on your difficulty rating (Easy, Medium, Hard)
- **Confidence Tracking** — Monitor your confidence percentage for each problem over time
- **Manual Add Form** — Quickly add problems by name and GitHub URL if needed
- **Due Reviews Queue** — See all problems due for review today, sorted by date
- **Problem Reset** — Reset individual problems or wipe all progress to start fresh
- **Double-Click Launch** — Start the app instantly by clicking `launch.vbs` (no terminal needed!)
- **Secure & Local** — All data stored locally; `.gitignore` keeps your database and config private

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python, Flask, SQLite3 |
| **Frontend** | HTML5, Vanilla CSS, Vanilla JavaScript |
| **Database** | SQLite (local, no internet required) |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** installed on your system
- **Git** installed
- **NeetCode.io GitHub Integration** set up ([see instructions](https://neetcode.io/profile/github))

### Step 1: Clone SpacedNeetCode

```bash
git clone https://github.com/ZahinDaiyan/SpacedNeetCode.git
cd SpacedNeetCode
```

### Step 2: Set Up Your Environment

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Run the App

#### **Option A: Silent Background Mode (Recommended)** ⭐

Double-click the **`launch.vbs`** file in the project root.

- The app launches invisibly in the background
- Your browser automatically opens to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**
- To shut down safely: Go to **Settings** → **Shutdown Application**

#### **Option B: Interactive Terminal Mode**

Double-click the **`run.bat`** file in the project root.

- The app runs in a visible terminal window
- You can see logs and debug messages
- Close the terminal or press `Ctrl+C` to stop

---

## 📖 Configuration & Usage

### 1. Configure Your NeetCode GitHub Repository

1. First, [set up NeetCode's GitHub Integration](https://neetcode.io/profile/github) if you haven't already
   - This enables auto-commits of your solutions to GitHub
2. Open SpacedNeetCode and click **Settings** (top-right)
3. Enter your GitHub repository in `owner/repo` format
   - Example: `ZahinDaiyan/neetcode-submissions`
4. (Optional) Enter a **GitHub Personal Access Token (PAT)**
   - Use this if your repo is private or to bypass API rate limits
   - [Create a PAT here](https://github.com/settings/tokens)
5. Click **Save Settings**

### 2. Sync Your NeetCode Solutions

1. On the home screen, click **Sync Repository**
2. SpacedNeetCode scans your GitHub repo and imports problems you've solved
3. Each problem is automatically scheduled for review **tomorrow**
4. You'll see a success message with the count of new problems added

### 3. Review & Build Intuition

1. Problems appear in the **Due Today** queue when they're ready to review
2. Click a problem to open the review page
3. **Re-solve it on NeetCode** (or on paper/whiteboard)
4. Come back and rate your attempt:
   - **Easy** → You got it quickly → Interval multiplied by 2.5 (space it out longer)
   - **Medium** → You got it with some thought → Interval multiplied by 1.8
   - **Hard** → You struggled → Interval multiplied by 0.7 (review sooner)
5. Your next review date is automatically calculated
6. Repeat! Each review deepens your intuition

### 4. Reset Progress

**For individual problems:**
- Open the problem, scroll to the bottom, click **Reset Progress**

**For all problems:**
- Go to **Settings**, click **Reset All Review Progress**, confirm

---

## 📊 Dashboard Overview

| Section | What It Shows |
|---------|---------------|
| **Stats** | Total problems, due today count, average confidence |
| **Due Today** | Problems scheduled for review (sorted by date) |
| **All Problems** | Complete list of every problem you've synced |

---

## 🔧 Troubleshooting

### Issue: "`.venv` folder not found" or Python import errors

**Solution:** Reinstall dependencies
```bash
.venv\Scripts\pip install -r requirements.txt
```

### Issue: Browser doesn't open automatically

**Solution:** Manually open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser

### Issue: "Repository not found" or sync fails

**Check:**
- Your GitHub repo name is correct (`owner/repo` format)
- Your repo was created by NeetCode's GitHub Integration (contains solved problems)
- If private, you've provided a valid GitHub PAT with repo access
- Your internet connection is active

### Issue: "Port 5000 is already in use"

**Solution:** Another app is using the port. Either:
- Close the other app or
- Edit `app.py` line 208 and change `port=5000` to a different number

### Issue: App crashes on macOS/Linux

**Ensure you:**
- Activated the virtual environment: `source .venv/bin/activate`
- Are using Python 3.8+: `python3 --version`

---

## 📁 Project Structure

```
SpacedNeetCode/
├── app.py                 # Main Flask application
├── database.py            # SQLite database operations
├── scheduler.py           # SM-2 spaced repetition logic
├── github_sync.py         # GitHub integration
├── requirements.txt       # Python dependencies
├── launch.vbs             # Double-click launcher (Windows)
├── run.bat                # Terminal launcher (Windows)
├── templates/             # HTML pages (Jinja2)
├── static/                # CSS, JavaScript, assets
├── data/                  # Local database (git-ignored)
└── README.md              # This file
```

---

## 🧠 How Spaced Repetition Works

SpacedNeetCode uses the **SM-2 algorithm**, the same technique used by medical students, language learners, and other high-achievers:

1. **First review** → After 1 day
2. **If you rate Easy** → Next review in 2-3 weeks
3. **If you rate Hard** → Next review in a few days
4. **Pattern:** Each successful review spaces out the next one further

**Why this works:**
- You review problems **before you forget them** (not after)
- Each review strengthens the memory and deepens pattern recognition
- You spend more time on hard problems and less on easy ones
- Over time, you build genuine **coding intuition** instead of shallow memorization

---

## 🔐 Privacy & Security

- **All data is stored locally** in `data/` folder (git-ignored)
- Your GitHub Personal Access Token is saved in `data/config.json` (git-ignored)
- No analytics, no tracking, no data sent anywhere
- Your review history never leaves your computer

---

## 🐛 Found a Bug?

If you encounter issues:
1. Check the [Troubleshooting](#-troubleshooting) section above
2. Open an [issue on GitHub](https://github.com/ZahinDaiyan/SpacedNeetCode/issues)
3. Include:
   - What you were doing
   - The exact error message
   - Your Python version and OS

---

## 🚧 Roadmap (Future Versions)

Planned features for future releases:
- [ ] Dark mode toggle
- [ ] Difficulty filtering (show only Hard/Medium problems)
- [ ] Problem tagging by topic (Arrays, Trees, DP, etc.)
- [ ] Export progress as CSV
- [ ] Cloud sync (optional)
- [ ] Mobile companion app
- [ ] Custom spaced repetition settings

---

## 📝 License

This project is open source. Feel free to fork, modify, and use it!

---

## 💡 Pro Tips

- **Sync regularly** (daily/weekly) to keep your problem list fresh as you solve on NeetCode
- **Rate honestly** — The SM-2 algorithm works best with accurate difficulty ratings; don't shortcut this
- **Review consistently** — Set a time each day to review your due problems (morning or evening)
- **Watch NeetCode videos** — Before your review, rewatch the problem's video explanation if needed
- **Use the confidence score** — Problems where your confidence drops should get extra attention
- **Reset if overwhelmed** — If you have too many due problems, reset some harder ones to spread out the load

---

**Happy coding and learning! 🎉**

Build the patterns. Master the problems. Retain forever.
