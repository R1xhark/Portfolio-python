import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer

# Nastavení přístupových údajů k Twitter API
consumer_key = "váš_consumer_key"
consumer_secret = "váš_consumer_secret"
access_token = "váš_access_token"
access_token_secret = "váš_access_token_secret"

# Nastavení ověření pomocí Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Vytvoření objektu API
api = tweepy.API(auth)

# Funkce pro provádění sentimentální analýzy
def provest_sentimentalni_analyzu(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Pozitivní'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negativní'
    else:
        sentiment = 'Neutrální'

    return sentiment, sentiment_scores

# Získání tweetů a provedení sentimentální analýzy
def analyzovat_tweety(hledani, pocet):
    tweets = api.search(q=hledani, count=pocet)

    for tweet in tweets:
        text = tweet.text
        sentiment, sentiment_scores = provest_sentimentalni_analyzu(text)

        print("Tweet: ", text)
        print("Sentiment: ", sentiment)
        print("Sentimentální skóre: ", sentiment_scores)
        print("------------------------------")

# Příklad použití
hledani = input("Zadejte hledací dotaz: ")
pocet = int(input("Zadejte počet tweetů k analýze: "))

analyzovat_tweety(hledani, pocet)
