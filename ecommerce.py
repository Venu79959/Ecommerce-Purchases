#!/usr/bin/env python
# coding: utf-8

# # Ecommerce Purchase Project ( Data Analysis ) by KODI VENU

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv('Ecommerce Purchases')
data


#  #Top 10 rows of the dataset

# In[3]:


data.head(10)


# #  Last 10 rows of the dataset

# In[4]:


data.tail(10)


# #Datatype of the Columns

# In[6]:


data.dtypes


# # Check Null Values in the Dataset

# In[7]:


data.isnull()


# In[8]:


data.isnull().sum()


# #Dataset rows & columns count

# In[9]:


data.columns


# In[10]:


len(data.columns)


# In[12]:


len(data)


# In[13]:


data.info()


# In[15]:


data.shape


# #Highest & Lowest Purchases prices

# In[16]:


data.columns


# In[17]:


data['Purchase Price'].max()


# In[18]:


data['Purchase Price'].min()


# #Average Purchase Price

# In[19]:


data['Purchase Price'].mean()


# In[20]:


# Finding how many people have the French 'fr' as their Language


# In[22]:


data.columns


# In[23]:


data['Language']


# In[24]:


data[data['Language']=='fr']


# In[25]:


len(data[data['Language']=='fr'])


# In[29]:


data[data['Language']=='fr'].count()


# In[30]:


# Job Title contains Engineer


# In[31]:


data.columns


# In[32]:


data['Job']


# In[33]:


len(data[data['Job'].str.contains('engineer',case=False)])


# In[ ]:


# Finding email of the person with IP address 132.207.160.22


# In[34]:


data.columns


# In[35]:


data['IP Address']=="132.207.160.22"


# In[36]:


data[data['IP Address']=="132.207.160.22"]


# In[37]:


data[data['IP Address']=="132.207.160.22"]['Email']


# In[ ]:


# Finding how many people have the Mastercard and made a purchase of  above 50


# In[38]:


data.columns


# In[39]:


data['CC Provider']


# In[40]:


(data['CC Provider']=='Mastercard')&(data['Purchase Price']>50)


# In[42]:


data[(data['CC Provider']=='Mastercard')&(data['Purchase Price']>50)]


# In[43]:


len(data[(data['CC Provider']=='Mastercard')&(data['Purchase Price']>50)])


# In[ ]:


# Finding email of person with credit card number 4664825258997302


# In[44]:


data.columns


# In[45]:


data['Credit Card']


# In[46]:


data['Credit Card']=="4664825258997302"


# In[48]:


data[data['Credit Card']==4664825258997302]


# In[49]:


data[data['Credit Card']==4664825258997302]['Email']


# In[ ]:


# Number of people purchased during AM & Number of people purchased during PM


# In[50]:


data.columns


# In[51]:


data['AM or PM'].value_counts()


# In[52]:


# How many people's credit card expires in 2020


# In[53]:


data.columns


# In[54]:


data['CC Exp Date']


# In[55]:


data['CC Exp Date'].apply(lambda x:x[3:]=='20')


# In[56]:


data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')]


# In[57]:


len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')])


# In[58]:


# Top 5 Most Popular Email Providers (gmail.com , yahoo.com)


# In[59]:


data.columns


# In[60]:


data['Email']


# In[64]:


data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head()


# In[ ]:




