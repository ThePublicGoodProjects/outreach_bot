
# coding: utf-8

# In[ ]:


#!sudo pip install xlrd
#!sudo pip install openpyxl


# In[ ]:


import pandas as pd
import numpy as np
import datetime
from dateutil.parser import parse

now = datetime.datetime.now() ## this brings current date along with hour, minutes, seconds
# current_day = datetime.date.today() ## this brings only year, month, day.

# df = pd.read_csv('data.csv') # read csv
df = pd.read_excel('data.xlsx', sheetname=0) # read excel

df.head()


# In[ ]:


## When you open a .csv file in Excel and save it as .xlsx, it parses the date as Timestamp 
## so we need to tweak the code a bit using datetime.date() instead of parse()
## Here the code will compare "Tweet's date" vs "Current date" and "Complete" vs "Not complete".

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


# In[ ]:


df.head()


# In[ ]:


#Overwrite the file
#df.to_csv('data.csv', index=False)
df.to_excel('data.xlsx', index = False)

#Create a new file
#df.to_csv('data1.csv', index=False)
#df.to_excel('data1.xlsx', index = False)

