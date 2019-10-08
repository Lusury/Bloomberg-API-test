#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import blpapi
import pybbg


# In[2]:


bbg = pybbg.Pybbg()
bbg.service_refData()


# In[15]:


ticker = ['FR RB5011 Mtge']


# In[16]:


download = bbg.bdh(ticker, 'PX_LAST', '19000101', '', periodselection = 'MONTHLY')


# In[17]:


download.to_excel('0926-pool.xlsx')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




