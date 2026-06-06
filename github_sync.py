# github_sync.py
import os
import json
import urllib.parse
from datetime import datetime
import requests
import database

SYNC_INFO_PATH = os.path.join("data", "sync_info.json")
CONFIG_PATH = os.path.join("data", "config.json")
DEFAULT_REPO = "ZahinDaiyan/neetcode-submissions"

def load_config():
    """Loads GitHub repository configuration."""
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"github_repo": DEFAULT_REPO, "github_token": ""}

def save_config(github_repo, github_token):
    """Saves GitHub repository configuration."""
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump({
            "github_repo": github_repo.strip(),
            "github_token": github_token.strip()
        }, f)

def get_last_sync_time():
    """Retrieves the last sync time from metadata file."""
    if os.path.exists(SYNC_INFO_PATH):
        try:
            with open(SYNC_INFO_PATH, "r") as f:
                data = json.load(f)
                return data.get("last_sync_time")
        except Exception:
            return None
    return None

def update_last_sync_time():
    """Updates the last sync time to the current timestamp."""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(SYNC_INFO_PATH), exist_ok=True)
    with open(SYNC_INFO_PATH, "w") as f:
        json.dump({"last_sync_time": now_str}, f)
    return now_str

def fetch_problems_from_github():
    """
    Scans the configured GitHub repository.
    Returns a list of dicts: [{'name': 'Two Integer Sum', 'github_url': '...'}]
    """
    config = load_config()
    repo_path = config.get("github_repo", DEFAULT_REPO).strip()
    
    # Split repo path into owner and name
    if "/" in repo_path:
        repo_owner, repo_name = repo_path.split("/", 1)
    else:
        repo_owner = "ZahinDaiyan"
        repo_name = "neetcode-submissions"
        
    headers = {}
    # Use config token, fallback to environment variable
    token = config.get("github_token") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
        
    repo_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    
    try:
        # Get repository info to find default branch
        repo_info_resp = requests.get(repo_url, headers=headers, timeout=10)
        if repo_info_resp.status_code != 200:
            print(f"Error fetching repo info: {repo_info_resp.status_code}")
            return []
            
        default_branch = repo_info_resp.json().get("default_branch", "main")
        
        # Get tree recursively
        tree_url = f"{repo_url}/git/trees/{default_branch}?recursive=1"
        tree_resp = requests.get(tree_url, headers=headers, timeout=10)
        
        if tree_resp.status_code != 200:
            print(f"Error fetching repo tree: {tree_resp.status_code}")
            return []
            
        tree_data = tree_resp.json()
        tree = tree_data.get("tree", [])
        
        unique_problems = {}
        
        for item in tree:
            # Check for files (blobs) that represent submissions
            if item.get("type") == "blob":
                path = item.get("path")
                parts = path.split("/")
                
                # Expected: <topic-folder>/<problem-slug>/submission-X.<ext>
                if len(parts) >= 3 and parts[-1].startswith("submission-"):
                    problem_slug = parts[-2]
                    problem_folder = "/".join(parts[:-1])
                    
                    if problem_folder not in unique_problems:
                        # Convert slug to Title Case, e.g., "two-integer-sum" -> "Two Integer Sum"
                        words = [w.capitalize() for w in problem_slug.replace("_", "-").split("-") if w]
                        problem_name = " ".join(words)
                        
                        # URL-encode the path components
                        encoded_folder = "/".join(urllib.parse.quote(part) for part in parts[:-1])
                        github_url = f"https://github.com/{repo_owner}/{repo_name}/tree/{default_branch}/{encoded_folder}"
                        
                        unique_problems[problem_folder] = {
                            "name": problem_name,
                            "github_url": github_url
                        }
                        
        return list(unique_problems.values())
        
    except Exception as e:
        print(f"Exception during GitHub fetch: {e}")
        return []

def sync_github_repository():
    """Fetches problems from GitHub and saves new ones to SQLite."""
    problems = fetch_problems_from_github()
    if not problems:
        return 0, 0
        
    new_count = 0
    total_count = len(problems)
    
    # Initialize DB table if needed
    database.init_db()
    
    # Get existing problems names to count new ones
    existing_problems = {p["name"] for p in database.get_all_problems()}
    
    for p in problems:
        if p["name"] not in existing_problems:
            database.create_problem(p["name"], p["github_url"])
            new_count += 1
            
    update_last_sync_time()
    
    return new_count, total_count
