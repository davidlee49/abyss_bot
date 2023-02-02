import praw
from bot_reqs import REDDIT_ID, REDDIT_CS, REDDIT_PASS, REDDIT_CID


def get_img():
    reddit = praw.Reddit(client_id=REDDIT_CID,
                         client_secret=REDDIT_CS,
                         username=REDDIT_ID,
                         password=REDDIT_PASS,
                         user_agent="praw",
                         check_for_async=False)


    for submission in reddit.subreddit("confusingperspective").random_rising(limit=1):
        print(submission.url)
        return submission.url



