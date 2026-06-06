# Build a Personal LeetCode Spaced Repetition Tracker

## Goal

Build a local-first web application that helps me remember LeetCode problems using spaced repetition.

This is a personal tool and does NOT need authentication, cloud hosting, Docker, React, Next.js, Redis, Celery, or any complex infrastructure.

Use only:

* Python
* SQLite
* HTML
* CSS
* Vanilla JavaScript

The app should run locally using:

```bash
python app.py
```

and open in a browser.

---

# Core Idea

I solve LeetCode problems and store solutions in a GitHub repository.

The application should:

1. Read solved problems from my GitHub repository.
2. Store them in SQLite.
3. Calculate when each problem should be reviewed next.
4. Show today's review queue.
5. Let me review a problem.
6. Let me rate the review as:

   * Easy
   * Medium
   * Hard
7. Update the next review date based on the rating.
8. Send email reminders for due reviews.

The app is intended to help long-term retention of problem-solving patterns.

---

# GitHub Repository

Repository:

https://github.com/ZahinDaiyan/neetcode-submissions

The application should scan the repository and identify solved problems.

Assume each problem is represented by a folder.

Extract:

* Problem name
* GitHub folder URL
* Date first discovered

When syncing:

* Add new problems automatically.
* Do not create duplicates.
* Existing problems should remain unchanged.

Create a "Sync Repository" button.

---

# Database Design

Use SQLite.

Create a table:

problems

Fields:

* id
* name
* github_url
* first_discovered
* last_review_date
* next_review_date
* review_count
* interval_days
* ease_factor
* confidence_score

Default values:

review_count = 0

interval_days = 1

ease_factor = 2.5

confidence_score = 0

---

# Review Scheduling Logic

Implement a simplified spaced repetition algorithm.

When a problem is first added:

interval_days = 1

next_review_date = tomorrow

---

If review result is EASY:

review_count += 1

interval_days = interval_days * 2.5

ease_factor += 0.1

---

If review result is MEDIUM:

review_count += 1

interval_days = interval_days * 1.8

---

If review result is HARD:

review_count += 1

interval_days = max(1, interval_days * 0.7)

ease_factor = max(1.3, ease_factor - 0.1)

---

After updating interval:

next_review_date = today + interval_days

Store rounded interval values.

---

# Confidence Score

Generate a simple confidence score between 0 and 100.

Suggested formula:

confidence_score =
min(
100,
(review_count * 10) +
(interval_days * 2)
)

Store this value in database.

Display it prominently.

This does not need to be scientifically accurate.

---

# Dashboard

Homepage should show:

## Statistics

Total Problems

Problems Due Today

Average Confidence

Current Streak (optional)

---

## Today's Reviews

Display all problems where:

next_review_date <= today

For each problem show:

* Problem name
* GitHub link
* Confidence score
* Days since last review
* Next review date

Buttons:

Review

---

## All Problems

Search bar

Sortable table

Columns:

* Problem
* Confidence
* Last Review
* Next Review
* Review Count

---

# Review Page

When user clicks Review:

Show:

Problem Name

GitHub Link

Confidence Score

Last Reviewed

Review Count

---

User should attempt the problem on LeetCode independently.

After finishing:

Show buttons:

Easy

Medium

Hard

When clicked:

Update scheduling values.

Show:

"Next review scheduled in X days."

Return to dashboard.

---

# Calendar View

Create a simple page showing:

Today

Problems due today

Problems due tomorrow

Problems due this week

No need for a fancy calendar library.

Simple grouped lists are enough.

---

# Email Reminder

Create a Python script:

send_reminders.py

This script:

1. Checks database.
2. Finds all problems due today.
3. Sends an email reminder.

Email content:

Subject:
LeetCode Reviews Due Today

Body:

You have N problems due.

List each problem.

Include GitHub links.

Use Gmail SMTP.

Store credentials in a config file.

Do not hardcode credentials.

---

# UI Requirements

Simple and clean.

Dark mode.

Responsive.

No frameworks.

Use:

* HTML
* CSS
* Vanilla JS

Design should resemble:

A productivity dashboard.

Use cards.

Use progress bars for confidence.

Use colored badges:

Green = High confidence

Yellow = Medium confidence

Red = Low confidence

---

# File Structure

project/

app.py

database.py

scheduler.py

github_sync.py

email_service.py

send_reminders.py

requirements.txt

templates/

index.html

review.html

calendar.html

static/

style.css

script.js

data/

tracker.db

---

# Technical Requirements

Use Flask.

Use SQLite.

Use requests for GitHub API.

Use standard SMTP for email.

Use Jinja templates.

Keep code simple and readable.

Avoid unnecessary abstractions.

Avoid overengineering.

Prioritize maintainability.

---

# Nice-to-Have Features

Not required for v1.

* Topic tagging
* Heatmap
* Review streaks
* Export database
* Backup database
* Difficulty breakdown
* Weakest topics analysis

Implement only after the core system is working.

---

# Success Criteria

The application is successful if:

1. It can import solved LeetCode problems from the GitHub repository.
2. It stores them in SQLite.
3. It shows which problems are due today.
4. It allows rating reviews as Easy / Medium / Hard.
5. It automatically schedules future reviews.
6. It displays confidence scores.
7. It can send email reminders.
8. It runs entirely on a local machine with minimal setup.

# A repo structure readme is there in the directory for you to refer 

# Development Workflow (IMPORTANT)

Build the application in small, testable steps.

Do NOT generate the entire application at once.

After completing each step, ensure it works before moving to the next.

The goal is a working V1, not a perfect architecture.

---

## Step 1 - Project Setup

Create:

* Flask application
* Basic folder structure
* SQLite database initialization

Success criteria:

* Running `python app.py` starts the server.
* Visiting localhost shows a simple page.

Do not build any business logic yet.

---

## Step 2 - Database

Create the SQLite database.

Create the `problems` table.

Add helper functions:

* create_problem()
* get_all_problems()
* get_problem()
* update_problem()

Success criteria:

* Problems can be inserted and retrieved.

---

## Step 3 - GitHub Sync

Implement repository scanning.

Repository structure:

* Each problem has its own folder.
* A folder may contain multiple submission files.
* Multiple submissions still represent one problem.

Example:

two-sum/
submission0.py
submission1.py

This should create exactly one problem record.

Create a "Sync Repository" button.

Success criteria:

* Clicking sync imports problems from GitHub.
* Existing problems are not duplicated.

---

## Step 4 - Dashboard

Create the homepage.

Display:

* Total problems
* Due today count
* Problem table

Show:

* Problem name
* Confidence score
* Last review
* Next review
* Review count

Success criteria:

* Imported problems appear correctly.

---

## Step 5 - Review System

Create a review page.

Display:

* Problem name
* GitHub link
* Review history

Provide buttons:

* Easy
* Medium
* Hard

Success criteria:

* Clicking a button updates the database.

---

## Step 6 - Scheduling Algorithm

Implement spaced repetition.

Easy:

* interval *= 2.5

Medium:

* interval *= 1.8

Hard:

* interval *= 0.7

Update:

* interval_days
* review_count
* next_review_date

Success criteria:

* Reviews schedule future dates correctly.

---

## Step 7 - Confidence Score

Implement confidence score calculation.

Store score in database.

Display score on dashboard.

Success criteria:

* Confidence updates after reviews.

---

## Step 8 - Due Reviews

Show only problems where:

next_review_date <= today

Create a "Due Today" section.

Success criteria:

* Problems appear automatically when due.

---

## V1 Complete

The application is considered complete when:

1. GitHub sync works.
2. Problems are stored in SQLite.
3. Dashboard displays problems.
4. Reviews can be rated Easy / Medium / Hard.
5. Next review dates are calculated.
6. Due reviews appear automatically.

Do NOT implement:

* Authentication
* User accounts
* Email reminders
* Calendar view
* Heatmaps
* Streaks
* Topic analysis
* Cloud deployment
* Docker
* React
* REST APIs
* Background workers

Focus only on delivering a working local V1.
