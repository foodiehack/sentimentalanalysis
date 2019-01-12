mport tweepy
import csv
from textblob import TextBlob

cus_key = 'MGURGewHn0r6Pch0Ta2zRiytV'
cus_secret = 'AMkWMSTdCR5TTzXUZdDS8RThi0eRGEFiO1dXzQpLZYYcHDOoHY'
access_token = '806000841798713344-nzuo0ydRCZNes0dTXkb6gZJY67m9jkR'
access_token_secret = '8B6dFXjkYe6GSEFO7WgsNxTO4ECxP2a49bEq01DPrlAeq'

def get_label(analysis, threshold = 0):
    if analysis.sentiment[0] > 0:
        return 'Positive'
    else:
        return 'Negative'


auth = tweepy.OAuthHandler(cus_key, cus_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('win')
rows = [["tweet", "Sentiment"]]

with open('tweets.csv','w') as csvfile:
    myWriter = csv.writer(csvfile, lineterminator = '\n')

    for tweets in public_tweets:
        analysis = TextBlob(tweets.text)
        rows.append([tweets.text, get_label(analysis)])
    myWriter.writerows(rows)
