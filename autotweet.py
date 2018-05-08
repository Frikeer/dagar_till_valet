import tweepy
from tid_till_valet import get_msg

consumer_key = "..."
consumer_secret = "..."
access_token_secret = "..."
access_token = "..."

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(get_msg())
