import tweepy

consumer_key = "XXXXX"
consumer_secret = "XXXXX"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Helper function for handling pagination in our search and handle rate limits
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print('Reached rate limite. Sleeping for >15 minutes')
            time.sleep(15 * 61)
        except StopIteration:
            break
 
# Define the term you will be using for searching tweets
query = '@NotionHQ'
query = query + ' -filter:retweets'
 
# Define how many tweets to get from the Twitter API
count = 25
 
# Search for tweets using Tweepy
search = limit_handled(tweepy.Cursor(api.search,
                       q=query,
                       tweet_mode='extended',
                       lang='en',
                       result_type="recent").items(count))
 
# Process the results from the search using Tweepy
tweets = []
for result in search:
    tweet_content = result.full_text
    tweets.append(tweet_content) # Only saving the tweet content.
