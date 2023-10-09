from functions.week4.language_detection import tweets
from functions.week4.sentiment_detection import analyze_sentiment_english, analyze_sentiment_other
import pandas as pd
from tabulate import tabulate

df = pd.read_excel("tweets.xlsx")
t = df["Tweet"]
tweets(t)

for tweet in t:
    sentiment_data = (analyze_sentiment_english(tweet) & analyze_sentiment_other(tweet))
    headers = ["Tweets", "Language", "Sentiment"]

    # Create the table using tabulate and print
    table = tabulate(tweet_list, headers, tablefmt="grid")
    print(table)
