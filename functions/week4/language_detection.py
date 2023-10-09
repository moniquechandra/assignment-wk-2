from langdetect import detect

# n is the number of tweets we want to detect.
# This code could also be modified to process an existing data.
# e.g. by editing the tweet list -- add/read the data there

def tweets(n):   
    ''' Prints a column of tweets with their languages '''
    tweet_list = []
    try:
        # For-looping the input and append the tweets to the list
        for i in range(n):
            tweeting = input("Insert your tweet here: ")
            language = detect(tweeting) 
            tweet_list.append((tweeting, language))
        
    # If encounter any exception, language is "Unknown"
    except:
        language = "Unknown"
    
    # Print the columns
    print("{:<10} {:<10}".format('Tweet', 'Language'))

    for tweet, language in tweet_list:
        print("{:<10} {:<10}".format(tweet, language))
    
tweets(3)
        





