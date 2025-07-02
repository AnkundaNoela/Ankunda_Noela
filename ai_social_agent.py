import os
from dotenv import load_dotenv
import tweepy
import schedule
import time
import random

# Load environment variables
load_dotenv()

# Client with credentials from .env
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
    consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    wait_on_rate_limit=True
)

# Test connection first
def test_connection():
    try:
        me = client.get_me()
        print(f"✅ Connected successfully! Account: @{me.data.username}")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

# Initialize posts array
posts = []

def post_tweet(content):
    """Posts a tweet to Twitter"""
    try:
        if len(content) > 280:
            content = content[:277] + "..."
                
        response = client.create_tweet(text=content)
        print(f"Tweet posted: {content}")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def scheduled_post():
    """Posts a random tweet from the queue"""
    if posts:
        content = random.choice(posts)
        post_tweet(content)
    else:
        print("No posts in queue")

# Test connection before proceeding
if not test_connection():
    print("Please check your Twitter API credentials and permissions.")
    exit()

# Get initial prompt and post it
prompt = input("Enter your initial prompt: ")
post_tweet(prompt)

# Add posts to the array
print("\nAdd posts to your queue (type 'done' when finished):")
while True:
    new_post = input("Enter a post: ")
    if new_post.lower() == 'done':
        break
    posts.append(new_post)
    print(f"Added! Total posts: {len(posts)}")

# Schedule posts every day at 9 AM
schedule.every().day.at("09:00").do(scheduled_post)

print(f"\nBot started. Will post daily at 9 AM from {len(posts)} posts.")
print("Type 'post' to post a random tweet now, or 'quit' to exit.")

# Keep running
while True:
    schedule.run_pending()
    
    # Check for user input (non-blocking)
    try:
        user_input = input().strip().lower()
        if user_input == 'post':
            if posts:
                content = random.choice(posts)
                post_tweet(content)
            else:
                print("No posts available")
        elif user_input == 'quit':
            break
    except:
        pass
    
    time.sleep(1)