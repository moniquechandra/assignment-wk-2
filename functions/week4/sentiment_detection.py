from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment_english(tweet):
    ''' Return the sentiment of the tweet '''
    polarity = TextBlob(tweet).polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment

def analyze_sentiment_other(tweet):
    sia = SentimentIntensityAnalyzer()
    pol_score = sia.polarity_scores(tweet)
    if pol_score >= 0.05:
        sentiment = "positive"
    elif pol_score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment