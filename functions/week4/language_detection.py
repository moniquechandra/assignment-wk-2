from langdetect import detect
from tabulate import tabulate
import pandas as pd
from sentiment_detection import analyze_sentiment_english, analyze_sentiment_other
def lang_and_sentiment():
    # Define the data frame we will use for language detection
    df = pd.read_excel("tweets.xlsx")
    t = df["Tweet"]

    # Make two empty lists to list tuples of (1) each tweet and its detected language &
    # (2) each tweet, its detected language, and sentiment analysis.
    tweet_list_1 = []
    tweet_list_2 = []

    try:
    # For-looping the language detection for each tweet and append the results to the list as tuples
        for tweet in t:
            language = detect(tweet)
            sentiment_data = (analyze_sentiment_english(tweet) & analyze_sentiment_other(tweet))
            tweet_list_1.append((tweet, language))
            tweet_list_2.append((tweet, language, sentiment_data))
    # If encounter any exception, language is "Unknown"
    except:    
        language = "Unknown"

    # Define headers for the table
    headers1 = ["Tweets", "Language"]
    headers2 = ["Tweets", "Language", "Sentiment"]

    # Create the table using tabulate and print
    table1 = tabulate(tweet_list_1, headers1)
    table2 = tabulate(tweet_list_2, headers2)

    # Exercise 4.1
    print(table1)

    # Exercise 4.2
    # print(table2)

    # # Print the columns
    # print("{:<10} {:<10}".format('Tweet', 'Language'))

    # for tweet, language in tweet_list:
    #     print("{:<10} {:<10}".format(tweet, language))  


lang_and_sentiment()

