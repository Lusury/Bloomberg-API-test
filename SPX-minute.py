#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pybbg
from pandas import Series, DataFrame, Panel
from datetime import datetime, date, time
import pandas as pd
import blpapi


# In[2]:


bbg = pybbg.Pybbg()
bbg.service_refData()


# In[3]:


ticker = ['KOSPI2 Index', 'KOSPI Index']
fld_list = ['PX_OPEN', 'PX_HIGH', 'PX_LOW', 'PX_LAST']


# In[4]:


bbg.bdh(ticker, fld_list, '20131201', end_date=date.today().strftime('%Y%m%d'), periodselection = 'DAILY')


# In[8]:


ticker = 'SPX Index'
fld_list = ['open', 'high', 'low', 'close', 'volume', 'numEvents', 'value']


# In[10]:


bbg.bdib(ticker, fld_list, datetime(2004,9,24,1,30), datetime(2019,9,24,21,30), eventType='TRADE', interval = 1)


# In[ ]:




