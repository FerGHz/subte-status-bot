import praw
import datetime

# Reddit credentials (use environment variables in production)
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
USER_AGENT = "subte-status-bot by u/YOUR_USERNAME"

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT,
)

def get_subway_status():
    # Placeholder for subway API call
    return "All lines operating normally."

def create_post():
    subreddit = reddit.subreddit("YOUR_SUBREDDIT")

    status = get_subway_status()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    title = f"Subway Status Update - {timestamp}"
    body = f"**Current Status:**\n\n{status}\n\n*Automated update.*"

    subreddit.submit(title, selftext=body)

if __name__ == "__main__":
    create_post()
