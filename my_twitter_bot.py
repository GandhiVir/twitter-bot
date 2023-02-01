import tweepy

CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'
BEARER_TOKEN = 'YOUR_BEARER_TOKEN'
FILE_NAME = 'last_seen_id.txt'
_user_id = 'your_user_id' #can get using client.get_user(twitter_handle)

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

_since_id=retrieve_last_seen_id(FILE_NAME)

client1 = tweepy.Client(bearer_token=BEARER_TOKEN)
client2 = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

mentions = client1.get_users_mentions(id=_user_id, since_id=_since_id)

for mention in reversed(mentions.data):
    print(str(mention.id) + ' - ' + str(mention.text))
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#helloworld' in mention.text.lower():
        client2.create_tweet(text='I found #helloworld', in_reply_to_tweet_id=last_seen_id)

