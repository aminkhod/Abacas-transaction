#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


naval=['']
clientlist = pd.read_csv('CLIENT_LIST.csv', na_values =naval)


# In[5]:


clientlist.dropna()


# In[6]:


productlist = pd.read_csv('products.csv' , na_values =naval)


# In[ ]:




