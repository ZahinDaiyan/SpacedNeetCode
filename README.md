# SpacedNeetCode v1.0 🚀

> Master NeetCode problems using spaced repetition. NeetCode auto-commits your solutions to GitHub, and SpacedNeetCode optimizes your review schedule for long-term retention.

---

## What is SpacedNeetCode?

**The Problem:** You solve coding problems, feel confident, then forget the patterns weeks later. When you see a similar problem, you're back to square one.

**The Solution:** SpacedNeetCode uses **spaced repetition** to review problems at the perfect time—before you forget them—building genuine coding intuition.

### How It Works

1. **Solve on [NeetCode.io](https://neetcode.io)** → NeetCode auto-commits to GitHub
2. **SpacedNeetCode scans your repo** → Extracts solved problems
3. **You review on schedule** → Problems appear when your brain is ready to re-learn
4. **Rate your attempt** → Easy/Medium/Hard adjusts future review dates
5. **Repeat** → Build lasting intuition

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- [NeetCode GitHub Integration set up](https://neetcode.io/profile/github)

### Setup (3 steps)

**1. Clone the repo:**
```bash
git clone https://github.com/ZahinDaiyan/SpacedNeetCode.git
cd SpacedNeetCode
```

**2. Install dependencies:**
```bash
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

**3. Run the app:**
Double-click **`launch.vbs`** in the project root. Browser opens automatically to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📖 How to Use

### 1. Configure Your Repository
- Click **Settings** (top-right)
- Enter your GitHub repo: `owner/repo` (e.g., `username/neetcode-submissions`)
- (Optional) Add a GitHub PAT if your repo is private
- Click **Save**

### 2. Sync Your Solutions
- Click **Sync Repository** on home screen
- Your NeetCode problems are imported and scheduled for tomorrow

### 3. Review Problems
- Click a problem in **Due Today** queue
- Re-solve it on NeetCode
- Rate your attempt: **Easy** / **Medium** / **Hard**
- Your next review date auto-updates

---

## 💡 Pro Tips

- Sync regularly (daily/weekly) as you solve on NeetCode
- Rate honestly—Easy means space it out longer, Hard means review sooner
- Review consistently (morning or evening) to build the habit
- Watch NeetCode videos before reviews if you're stuck
- Reset progress if overwhelmed

---

## 🔧 Troubleshooting

**Browser doesn't open?** → Manually go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

**Sync fails?** → Check repo name is correct (`owner/repo` format) and NeetCode Integration is set up

**Port 5000 in use?** → Edit `app.py` line 208, change `port=5000` to another number

**Import error?** → Reinstall: `.venv\Scripts\pip install -r requirements.txt`

---

## 📚 Technical Details

### Architecture

| Component | Tech |
|-----------|------|
| Backend | Python, Flask |
| Database | SQLite3 (local, `.gitignore`'d) |
| Frontend | HTML5, Vanilla CSS, Vanilla JS |
| Algorithm | SM-2 Spaced Repetition |

### Project Structure

```
SpacedNeetCode/
├── app.py                 # Flask app
├── database.py            # SQLite operations
├── scheduler.py           # SM-2 algorithm
├── github_sync.py         # GitHub API integration
├── launch.vbs             # Windows launcher
├── run.bat                # Terminal launcher
├── templates/             # HTML (Jinja2)
├── static/                # CSS, JS
├── data/                  # Local DB (git-ignored)
└── requirements.txt
```

### SM-2 Algorithm

Each problem tracks:
- `review_count` — How many times reviewed
- `interval_days` — Days until next review
- `ease_factor` — Difficulty multiplier (2.5 default)

**Rating adjustments:**
- **Easy** → interval × 2.5 (space it out)
- **Medium** → interval × 1.8
- **Hard** → interval × 0.7 (review sooner)

### Security

- All data stored locally in `data/` (git-ignored)
- GitHub tokens saved in `data/config.json` (git-ignored)
- No cloud sync, no tracking, no external data

---

## 🐛 Issues?

Open an issue on [GitHub](https://github.com/ZahinDaiyan/SpacedNeetCode/issues) with:
- What you were doing
- Error message
- Python version & OS

---

## 🚧 Roadmap

- [ ] Dark mode
- [ ] Problem filtering (by difficulty/topic)
- [ ] Export progress
- [ ] Custom spaced repetition settings

---

**Build patterns. Master problems. Retain forever.** 🧠
