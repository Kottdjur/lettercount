import json
import re

tweets_file = open("tweets_sample.txt", "r")

for line in tweets_file:
    try:
        tweets_json = json.loads(line)
    except json.decoder.JSONDecodeError:
        continue

    if "retweeted_status" not in tweets_json:
        tweet = tweets_json["text"]
        words = tweet.split()
        for word in words:
            word = word.lower()
            word = re.sub("\W+", "", word)
            if re.match("han|hon|hen|den|det|denne|denna", word):
                print(word)
