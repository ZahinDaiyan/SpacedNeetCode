# SpacedNeetCode 🚀

A local-first, lightweight web application that helps you master LeetCode problems using spaced repetition. 

You solve LeetCode problems, commit your solutions to a GitHub repository, and SpacedNeetCode schedules reviews to maximize long-term retention of coding patterns.

---

## Key Features

* **Auto-Sync Solutions**: Scans your GitHub submissions repository (e.g. populated via NeetCode's GitHub Integration), extracts solved problems, and creates unique entries.
* **SM-2 Spaced Repetition**: Schedules future reviews based on how easy or hard you rated the problem (Easy, Medium, Hard).
* **Confidence Scoring**: Shows a rough confidence percentage tracker for each problem.
* **Manual Add Form**: Fallback option to quickly add problems by name and URL.
* **Due Reviews Queue**: Sorts and lists what problems are due for review today.
* **High-Contrast Dark Theme**: Simple, readable dark dashboard.

---

## Technology Stack

* **Backend**: Python, Flask, SQLite3
* **Frontend**: HTML5, Vanilla CSS, Vanilla JavaScript (Zero bloated frameworks)

---

## Quick Start (How to Run Locally)

### 1. Clone the Repository
```bash
git clone https://github.com/ZahinDaiyan/SpacedNeetCode.git
cd SpacedNeetCode
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python -m venv .venv
```
* **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Application
```bash
python app.py
```

Open your browser and navigate to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## Configuration & Usage

1. **Configure Your Repository**:
   * Click **Settings** in the top-right header.
   * Input your own GitHub repository path in `owner/repo` format (e.g., `username/my-leetcode-submissions`).
   * (Optional) Input a GitHub Personal Access Token (PAT) if your repository is **private**, or to bypass API rate limits on public repositories.
   * Click **Save Settings**.
2. **Import Submissions**:
   * Click **Sync Repository** on the home screen.
   * The scanner will import your unique solved problems and initialize their next review dates for tomorrow.
3. **Log Reviews**:
   * When a problem appears in your **Due Today** queue, try solving it on LeetCode.
   * Navigate back to the review page and rate your attempt:
     * **Easy**: Multiplies interval by `2.5` and raises ease factor.
     * **Medium**: Multiplies interval by `1.8`.
     * **Hard**: Multiplies interval by `0.7` and drops ease factor (schedules it again sooner).
