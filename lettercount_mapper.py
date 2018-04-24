import json
import re
import sys

for line in sys.stdin:
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
                print(word, "\t1")
