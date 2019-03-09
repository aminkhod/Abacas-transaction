#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd


# In[85]:


naval=['']
clientlist = pd.read_csv('CLIENT_LIST.csv', na_values =naval)


# In[86]:


clientlist.dropna()


# In[87]:


import csv
productname = []
unit = []
doller = []
derham = []
euro = []
code =[]
with open('products.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        productname.append(row[0])
        unit.append(row[1])
        doller.append(row[2])
        derham.append(row[3])
        euro.append(row[4])
        code.append(row[5])
productname =list(productname)
unit = list(unit)
doller=list(doller)
derham = list(derham)
euro=list(euro)
code= list(code)     


# In[88]:


productfram = []
productfram = pd.DataFrame()
productfram['p_name'] ,productfram['unit'], productfram['doller'],productfram['derham'], productfram['euro'],productfram['code'] = productname , unit , doller, derham, euro, code
# productfram['unit'], productfram['doller'] = unit , doller


# In[89]:


productfram.to_csv('product.csv',index=False)


# In[90]:


productlist = pd.read_csv('product.csv' , na_values =naval)


# In[92]:


productlist.dropna()


# In[119]:


Colist = pd.read_excel('List of Companies.xlsx')


# In[120]:


Colist.dropna()


# In[211]:


track = pd.read_csv('TRACKING SHEET.csv',skiprows = 7)


# In[212]:


track


# In[205]:


r,c = track.shape

po = []
for i in range(r):
    
    if track.loc[i,'Unnamed: 3'] == 'EURO':
        track.is_copy = False
        track.loc[i,'Unnamed: 3'] = 'AED'
        track.loc[i,'Unnamed: 2'] = str(int(track.loc[i,'Unnamed: 2']) * 4.13)
        print(track.loc[i,'Unnamed: 2'])
 


# In[206]:


track


# In[147]:





# In[ ]:




