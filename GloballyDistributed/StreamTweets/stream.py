from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json
import sys
import os


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=os.environ['CONSUMER_KEY']
consumer_secret=os.environ['CONSUMER_SECRET']

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_status(self, status):
        try:

            tweet = {"created_at": status.created_at, "text": status.text, "screen_name": status.user.screen_name, "image": status.user.profile_image_url_https.replace("_normal", "")}
            result = tweets.insert_one( tweet )
        except:
            print("Oops!")

        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    client = MongoClient(os.environ['COSMOS_CONNECTION_STRING'])
    db = client.kubeonazure
    tweets = db.tweets

    stream = Stream(auth, l)
    stream.filter(track=['docker'])