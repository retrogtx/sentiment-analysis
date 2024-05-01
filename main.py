import tweepy

consumer_key = "XXXXX"
consumer_secret = "XXXXX"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)