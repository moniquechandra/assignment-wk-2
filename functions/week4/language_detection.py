from langdetect import detect
from tabulate import tabulate
import pandas as pd
# n is the number of tweets we want to detect.
# This code could also be modified to process an existing data.
# e.g. by editing the tweet list -- add/read the data there


def tweets():   
    ''' Prints a column of tweets with their languages '''
    tweet_list = []
    df = pd.read_excel("tweets.xlsx")
    tweet = df["Tweet"]
    try:
        # For-looping the input and append the tweets to the list
        for t in tweet:
            language = detect(t) 
            tweet_list.append((t, language))
        
    # If encounter any exception, language is "Unknown"
    except:
        language = "Unknown"
    
    headers = ["Tweets", "Language"]

    # Create the table using tabulate and print
    table = tabulate(tweet_list, headers, tablefmt="grid")
    print(table)

    # # Print the columns
    # print("{:<10} {:<10}".format('Tweet', 'Language'))

    # for tweet, language in tweet_list:
    #     print("{:<10} {:<10}".format(tweet, language))

tweets()        





