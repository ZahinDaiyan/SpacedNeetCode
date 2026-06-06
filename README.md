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
* **Reset Functions**: Reset scheduling progress for an individual problem, or wipe progress globally for all problems.
* **Double-Click Launching**: Starts the local server and automatically opens your web browser.
* **Git Ignored Data**: Keep your personal databases and configuration secrets safe from public repository commits.

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

### 2. Set Up Your Environment
Create a virtual environment named `.venv` and install the required packages:
```bash
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

### 3. Run the App 🚀
* **Invisible Background Mode (Recommended)**: Double-click the **`launch.vbs`** script at the root folder of the project.
  This launches the Flask application invisibly in the background and automatically opens your browser to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.
  
  To shut down the app safely in this mode, go to **Settings** on the top right of the dashboard page and click the **Shutdown Application** button.
  
* **Interactive Terminal Mode**: Double-click the **`run.bat`** batch script at the root folder.
  This runs the application inside a visible command prompt terminal where you can see execution logs. Close the terminal window or press `Ctrl+C` to terminate the application.

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
4. **Reset Progress**:
   * **Individual Problem**: Open the problem details, click the **Reset Progress** button at the bottom of the card, and confirm.
   * **Global Reset**: Open the **Settings** page, click the **Reset All Review Progress** button, and confirm.
