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



# When you open a .csv file in Excel and save it as .xlsx, it parses the date as Timestamp
# so we need to tweak the code a bit using datetime.date() instead of parse()
# Here the code will compare "Tweet's date" vs "Current date" and "Complete" vs "Not complete".
for i in range(0,len(df)):
    if type(df.datetime[i]) == str:
        tweet_date = parse(df.datetime[i])
    else:
        tweet_date = df.datetime[i].to_pydatetime()

    if (tweet_date < now) & (pd.isnull(df.complete[i])):
        # api.PostUpdate(status = "@" + df.screenname[i], df.content[i])
        df.loc[i,'complete'] = str(now)
    else:
        print 'already done'

#Overwrite the file
df.to_excel('data.xlsx', index=False)
