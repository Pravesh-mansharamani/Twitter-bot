import tweepy
import time


consumer_key = '94hZmXWynZuuLbKPaPARv3x0z'
consumer_secret = 'HMOH36nFZH0cusED9O2nwgpr3ZrwCd8saWVjvha70dX5V6BOEq'
access_token = '1334002957503721480-tUCOOXzwq2jEfZdhSo53NUcz6sBTv8'
access_token_secret = 'PEQYhQIz9eJuiK9yUzNWPIXgZQIdSC8BKddbx5BXvsNHU'


auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Create a set to store the IDs of mentions that have already been replied to
replied_to_mentions = set()

def handle_mentions():
  # Get the mentions timeline
  mentions = api.mentions_timeline()

  # Reply to each mention with a message that includes the mentioning user's username
  for mention in mentions:
    # Check if the mention has already been replied to
    if mention.id not in replied_to_mentions:
      username = mention.user.screen_name
      message = f"Hello @{username}! Hope you are having a great day. I will reply to you shortly."
      api.update_status(message, in_reply_to_status_id=mention.id)
      # Add the mention's ID to the replied_to_mentions set
      replied_to_mentions.add(mention.id)

# Run the mention handling function every 60 seconds
while True:
  handle_mentions()
  time.sleep(60)
