from langdetect import detect
from tabulate import tabulate
import pandas as pd
from functions.week4.sentiment_detection import analyze_sentiment_english, analyze_sentiment_other

def lang_and_sentiment():
    # Define the data frame we will use for language detection
    df = pd.read_excel("C:\\Users\\anjel\\OneDrive\\Dokumen\\GitHub\\assignment wk 2\\functions\\week4\\tweets.xlsx")
    t = df["Tweet"]

    # Make two empty lists to list tuples of (1) each tweet and its detected language &
    # (2) each tweet, its detected language, and sentiment analysis.
    tweet_list_1 = []
    tweet_list_2 = []

    try:
    # For-looping the language detection for each tweet, define whether it is in EN or not (for sentiment detection)
    # and append the results to the list as tuples
        counter = 0   
        for tweet in t:
            language = detect(tweet)
            tweet_list_1.append((tweet, language))
            def_english = df.loc[counter, "Definitely English"]
            counter += 1
            if def_english == 1:
                sentiment_data = analyze_sentiment_english(tweet)
            elif def_english == 0:
                sentiment_data = analyze_sentiment_other(tweet)
            
            tweet_list_2.append((tweet, language, sentiment_data))

    # If encounter any exception, language is "Unknown"
    except:    
        language = "Unknown"
        tweet_list_1.append((tweet, language))
        tweet_list_2.append((tweet, language, sentiment_data))

    # Define headers for the table
    headers1 = ["Tweets", "Language"]
    headers2 = ["Tweets", "Language", "Sentiment"]

    # Create the table using tabulate and print
    table1 = tabulate(tweet_list_1, headers1, tablefmt= "grid")
    table2 = tabulate(tweet_list_2, headers2, tablefmt= "grid")

    # Uncomment if you want to execute the answer(s)!
    # Since the output is quite many, two exercises at a time won't look that neat :)

    # Exercise 4.1
    # print(table1)

    # Exercise 4.2
    print(table2)

lang_and_sentiment()

