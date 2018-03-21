import re
import random
import praw

reddit = praw.Reddit(client_id='Retracted', client_secret='Retracted'',
                     password='Retracted'', user_agent='Retracted',
                     username='Retracted')

subreddit = reddit.subreddit("all")
users = ["UsernameOfActorGoesHere", ]
count = 0

replies_quotes = \
[
    "This is one of the replies"
    "This is another possible one"
    "Would love to work on making some more probable than others"
]

while True:

    try:

        for comment in subreddit.stream.comments():
            if re.search("keywordWeAreLookingFor", comment.body, re.IGNORECASE):
                if comment.author.name not in users:
                    say = random.choice(replies_quotes)
                    print(say)
                    count += 1
                    print(count)

    except Exception as err:

        print("Exception handled while parsing")