# SpacedNeetCode v1.0 🚀

> Master LeetCode problems using spaced repetition. Solve on LeetCode, sync to GitHub, and let SpacedNeetCode optimize your review schedule.

A local-first, lightweight web application that helps you retain coding patterns long-term through intelligent scheduling.

---

## What is SpacedNeetCode?

You solve LeetCode problems and commit them to a GitHub repository (e.g., using [NeetCode.io's GitHub Integration](https://neetcode.io)). SpacedNeetCode then:

1. **Scans your GitHub repo** for new problem solutions
2. **Extracts unique problems** and initializes review schedules
3. **Schedules reviews** using the SM-2 spaced repetition algorithm
4. **Tracks confidence** for each problem to monitor your progress

The goal: **Master coding patterns by reviewing them at the optimal time intervals.**

---

## ✨ Key Features

- **Auto-Sync Solutions** — Automatically scans your GitHub repository and extracts solved problems
- **SM-2 Spaced Repetition** — Intelligently schedules reviews based on difficulty (Easy, Medium, Hard)
- **Confidence Tracking** — Monitor your confidence percentage for each problem
- **Manual Add Form** — Quickly add problems by name and GitHub URL
- **Due Reviews Queue** — See all problems due for review today, sorted by date
- **Problem Reset** — Reset individual problems or wipe all progress
- **Double-Click Launch** — Start the app by clicking `launch.vbs` (no terminal needed!)
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
- A **GitHub repository** with your LeetCode solutions (or use [NeetCode.io's sync](https://neetcode.io))

### Step 1: Clone the Repository

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

### 1. Configure Your GitHub Repository

1. Click **Settings** (top-right header)
2. Enter your GitHub repository in `owner/repo` format
   - Example: `ZahinDaiyan/neetcode-submissions`
3. (Optional) Enter a **GitHub Personal Access Token (PAT)**
   - Use this if your repo is private or to bypass API rate limits
   - [Create a PAT here](https://github.com/settings/tokens)
4. Click **Save Settings**

### 2. Sync Your Solutions

1. On the home screen, click **Sync Repository**
2. SpacedNeetCode scans your GitHub repo and imports new problems
3. Problems are automatically scheduled for review tomorrow
4. You'll see a success message with the count of new problems added

### 3. Log Your Reviews

1. Problems appear in the **Due Today** queue when they're ready to review
2. Click a problem to open the review page
3. Try solving it on LeetCode
4. Come back and rate your attempt:
   - **Easy** → Multiplies interval by 2.5 (space it out more)
   - **Medium** → Multiplies interval by 1.8
   - **Hard** → Multiplies interval by 0.7 (review sooner)
5. Your next review date is automatically calculated

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
| **All Problems** | Complete list of every problem you've added |

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
- [ ] Difficulty filtering (show only Hard problems)
- [ ] Problem tagging (Arrays, Trees, DP, etc.)
- [ ] Export progress as CSV
- [ ] Cloud sync (optional)
- [ ] Mobile companion app

---

## 📝 License

This project is open source. Feel free to fork, modify, and use it!

---

## 💡 Pro Tips

- **Sync regularly** (daily) to keep your problem list fresh
- **Rate honestly** — The SM-2 algorithm works best with accurate difficulty ratings
- **Use a consistent schedule** — Review your due problems every morning or evening
- **Reset if overwhelmed** — If you have too many due problems, consider resetting some harder ones

---

**Happy coding! 🎉**
