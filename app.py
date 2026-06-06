# app.py
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
import database
import github_sync
import scheduler

app = Flask(__name__)
app.secret_key = "spaced_neetcode_secret_key"

# Ensure data directory and database are initialized
os.makedirs("data", exist_ok=True)
database.init_db()

@app.route("/")
def index():
    # Fetch real problems from the SQLite database
    all_problems = database.get_all_problems()
    
    today = datetime.now()
    today_str = today.strftime("%Y-%m-%d")
    
    # Calculate days since last review for all problems
    for p in all_problems:
        if p["last_review_date"]:
            try:
                last_dt = datetime.strptime(p["last_review_date"], "%Y-%m-%d")
                delta_days = (today - last_dt).days
                p["days_since_last_review"] = f"{delta_days} day(s)"
            except Exception:
                p["days_since_last_review"] = "N/A"
        else:
            p["days_since_last_review"] = "Never"
            
    # Filter and sort due problems by next_review_date ascending
    due_problems = [p for p in all_problems if p["next_review_date"] <= today_str]
    due_problems.sort(key=lambda x: x["next_review_date"])
    
    total_problems = len(all_problems)
    due_today_count = len(due_problems)
    
    if total_problems > 0:
        avg_confidence = round(sum(p["confidence_score"] for p in all_problems) / total_problems)
    else:
        avg_confidence = 0
        
    last_sync = github_sync.get_last_sync_time()
    
    stats = {
        "total_problems": total_problems,
        "due_today": due_today_count,
        "avg_confidence": avg_confidence,
        "last_sync_time": last_sync
    }
    
    return render_template(
        "index.html",
        stats=stats,
        due_problems=due_problems,
        all_problems=all_problems
    )

@app.route("/review/<int:problem_id>")
def review(problem_id):
    # Fetch problem details from database
    problem = database.get_problem(problem_id)
    if not problem:
        flash("Problem not found!")
        return redirect(url_for("index"))
    return render_template("review.html", problem=problem)

@app.route("/review/<int:problem_id>/submit", methods=["POST"])
def submit_review(problem_id):
    rating = request.form.get("rating")
    problem = database.get_problem(problem_id)
    if not problem:
        flash("Problem not found!")
        return redirect(url_for("index"))
        
    updated = scheduler.calculate_next_review(
        rating=rating,
        review_count=problem["review_count"],
        interval_days=problem["interval_days"],
        ease_factor=problem["ease_factor"]
    )
    
    database.update_problem(
        problem_id=problem_id,
        last_review_date=updated["last_review_date"],
        next_review_date=updated["next_review_date"],
        review_count=updated["review_count"],
        interval_days=updated["interval_days"],
        ease_factor=updated["ease_factor"],
        confidence_score=updated["confidence_score"]
    )
    
    flash(f"Next review scheduled in {updated['interval_days']} days.")
    return redirect(url_for("index"))

@app.route("/sync", methods=["POST"])
def sync_repository():
    # Perform the actual GitHub synchronization
    try:
        new_count, total_count = github_sync.sync_github_repository()
        if total_count > 0:
            flash(f"Sync complete! Found {new_count} new problem(s) out of {total_count} total in the repository.")
        else:
            flash("Sync failed or repository empty. Please check your network and repository access.")
    except Exception as e:
        flash(f"Sync failed with error: {str(e)}")
        
    return redirect(url_for("index"))

@app.route("/add", methods=["POST"])
def add_problem():
    name = request.form.get("name").strip()
    github_url = request.form.get("github_url").strip()
    
    if not name or not github_url:
        flash("Problem name and GitHub URL are required.")
        return redirect(url_for("index"))
        
    # Add problem to SQLite
    problem_id = database.create_problem(name, github_url)
    if problem_id:
        flash(f"Successfully added problem '{name}' manually!")
    else:
        flash(f"Problem '{name}' already exists or failed to add.")
        
    return redirect(url_for("index"))

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        github_repo = request.form.get("github_repo", "").strip()
        github_token = request.form.get("github_token", "").strip()
        
        # Save to config.json
        github_sync.save_config(github_repo, github_token)
        flash("Settings saved successfully!")
        return redirect(url_for("index"))
        
    config = github_sync.load_config()
    return render_template("settings.html", config=config)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
