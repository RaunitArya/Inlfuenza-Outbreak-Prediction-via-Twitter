import tweepy
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

query = "influenza India OR flu India OR swine India OR fever India OR cough OR India outbreak -is:retweet lang:en"

tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "geo"])

tweet_data = []
if tweets.data:
    for tweet in tweets.data:
        tweet_data.append({"Date": tweet.created_at, "Text": tweet.text})

    df = pd.DataFrame(tweet_data)
    df.to_csv("influenza_tweets.csv", index=False)
    print("Scraping Complete! Data saved to 'influenza_tweets.csv'")
else:
    print("No tweets found. Try modifying your query.")