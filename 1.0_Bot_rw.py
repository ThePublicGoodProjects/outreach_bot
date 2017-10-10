# bot to read file of tweets from excel, then tweet them if we are past their
# scheduled time but they have not yet been tweeted

import pandas as pd
import numpy as np
import datetime
from dateutil.parser import parse

# get current date along with hour, minutes, seconds
now = datetime.datetime.now()

# load excel file of tweet data
df = pd.read_excel('data.xlsx', sheetname=0) # read excel

def post_tweet(row):
    try:
        status = '@{screenname} {content}'.format(screenname=row['screenname'], content=row['content'])
        #api.PostUpdate(status=status)
        return datetime.datetime.now()
    except:
        # log the error message
        pass

mask = (df['datetime'] < now) & pd.isnull(df['complete'])
df_tweet = df.loc[mask]
if len(df_tweet) > 0:
    df_tweet['complete'] = df_tweet.apply(post_tweet, axis=1)

# overwrite the file
df_tweet.to_excel('data.xlsx', index=False)
