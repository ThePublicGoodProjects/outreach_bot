################################################################################
# Module: bot.py
# Description: bot to read file of tweets from excel, then tweet them if we are
#              past their scheduled time but they have not yet been tweeted
################################################################################

import datetime as dt
import logging as lg
import numpy as np
import pandas as pd
import time
import twitter
from dateutil.parser import parse

from settings import pause_duration, test_mode
from bot_utils import log

from keys import consumer_key, consumer_secret, access_token_key, access_token_secret


# get current date along with hour, minutes, seconds
now = dt.datetime.now()
log('Script started at {}'.format(now))

# log into twitter
api = twitter.Api(consumer_key = consumer_key,
                  consumer_secret = consumer_secret,
                  access_token_key = access_token_key,
                  access_token_secret = access_token_secret)

user = api.VerifyCredentials().AsDict()
log('logged into twitter as "{}" id={}'.format(user['screen_name'], user['id']))

# load excel file of tweet data
df = pd.read_excel('data.xlsx', sheet_name=0) # read excel

def post_tweet(row):
    """
    Create a tweet's content from a dataframe row, then post it.
    """
    try:
        # create a status from screenname and content values, then post it
        status = '@{screenname} {content}'.format(screenname=row['screenname'], content=row['content'])
        if test_mode:
            log('TEST MODE did not tweet: "{}"'.format(status))
            return None

        else:
            api.PostUpdate(status=status)
            log('tweeted: "{}"'.format(status))
            time.sleep(pause_duration)
            return dt.datetime.now() #return the current datetime to save completion time to excel file

    except Exception as e:
        log('Error: {}'.format(e), level=lg.ERROR)
        return None

# filter the dataframe to retain only rows with datetime in the past and that
# have null in the complete column (ie, there is no completed timestamp)
mask = (df['datetime'] < now) & pd.isnull(df['complete'])
df_tweet = df.loc[mask]

# if we have any rows that meet this condition, tweet their contents
if len(df_tweet) > 0:
    # save the result as the completed timestamp
    completed = df_tweet.apply(post_tweet, axis=1)
    df.loc[completed.index, 'complete'] = completed

# overwrite the file
df.to_excel('data.xlsx', index=False)
log('Script finished at {}'.format(dt.datetime.now()))
