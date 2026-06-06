# scheduler.py
from datetime import datetime, timedelta

def calculate_next_review(rating, review_count, interval_days, ease_factor):
    """
    Calculates updated spaced repetition parameters based on the review rating:
    rating: 'easy', 'medium', or 'hard'
    
    Returns a dict with updated values:
    {
        'last_review_date': str (YYYY-MM-DD),
        'next_review_date': str (YYYY-MM-DD),
        'review_count': int,
        'interval_days': int,
        'ease_factor': float,
        'confidence_score': int
    }
    """
    rating = rating.lower().strip()
    
    # Increment review count
    new_review_count = review_count + 1
    
    # Calculate new interval and ease factor
    if rating == "easy":
        new_interval = round(interval_days * 2.5)
        new_ease = ease_factor + 0.1
    elif rating == "medium":
        new_interval = round(interval_days * 1.8)
        new_ease = ease_factor
    elif rating == "hard":
        new_interval = max(1, round(interval_days * 0.7))
        new_ease = max(1.3, ease_factor - 0.1)
    else:
        # Fallback for unexpected ratings
        new_interval = interval_days
        new_ease = ease_factor

    # Date calculations
    today = datetime.now()
    today_str = today.strftime("%Y-%m-%d")
    next_review = today + timedelta(days=new_interval)
    next_review_str = next_review.strftime("%Y-%m-%d")
    
    # Confidence score: min(100, round(review_count * ease_factor * 5))
    confidence = min(100, round(new_review_count * new_ease * 5))
    
    return {
        "last_review_date": today_str,
        "next_review_date": next_review_str,
        "review_count": new_review_count,
        "interval_days": new_interval,
        "ease_factor": round(new_ease, 2), # Keep rounded for neatness in SQLite
        "confidence_score": confidence
    }
