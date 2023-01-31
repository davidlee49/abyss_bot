import praw
import random


def get_img():
    reddit = praw.Reddit(client_id = "Rtg4xkG86_MqnCz3payAew",
                         client_secret = "IhSJIBXcCs6m4NIN4AnnHAb2kK4dYw",
                         username = "AbyssalAbyss",
                         password = "prawAbyssal!2#",
                         user_agent = "praw",
                         check_for_async = False)


    for submission in reddit.subreddit("confusingperspective").random_rising(limit=1):
        print(submission.url)
        return submission.url



