#!/usr/bin/env python
# coding: utf-8

# ## Squad Matching Algorithm

# #### Import all required libraries

# In[1]:


import pandas as pd
import numpy as np


# #### Load Dataset

# In[2]:


df = pd.read_csv("SquadData.csv",header=None)


# In[3]:


df.head(5)


# In[4]:


headers = ["Name","Squad_Num","Prefered_Lang","Interested_Grp","Age","City","Country","Region","Timezone",
          "Occupation","Degree","Prev_Took_Courses","Intern_Experience","Product_Management","Digital_Marketing",
          "Market_Research","Digital_Illustration","Product_Design","Prodcut_Developement","Growth_Marketing",
          "Leading_Groups","Internship_News","Cohort_Product_Marketing","Cohort_Product_Design",
          "Cohort_Product_Development","Cohort_Product_Growth","Hours_Per_Week"]


# In[5]:


df = df.drop(index=0)


# In[6]:


df.reset_index(drop=True,inplace=True)


# In[7]:


df.columns = headers


# In[8]:


abc_str = ['English','Hindi','Espanyol']


# In[9]:


df.head(10)


# In[10]:


df.to_csv("Dataset.csv",index=False)


# In[11]:


# The values in the column used to be objects which are now converted to float.
df["Digital_Marketing"] = pd.to_numeric(df["Digital_Marketing"], downcast="integer")


# In[12]:


# finding mean of column
mean_df = (df['Digital_Marketing'].mean())
# replacing nan values with mean of column
df['Digital_Marketing'].fillna((mean_df) , inplace = True)
#changing type to integer
df['Digital_Marketing'] = df['Digital_Marketing'].astype(int)


# In[13]:


df['Digital_Marketing']


# In[14]:


df["Market_Research"] = pd.to_numeric(df["Market_Research"], downcast="float")
# filling NaN values with average of entire column
mean_df = (df['Market_Research'].mean())
# replacing nan values with mean of column
df['Market_Research'].fillna((mean_df) , inplace = True)
df['Market_Research'] = df['Market_Research'].astype(int)
df['Market_Research']


# In[15]:


# df['Digital_Illustration']
df["Digital_Illustration"] = pd.to_numeric(df["Digital_Illustration"], downcast="float")
# finding mean of column
mean_df = (df['Digital_Illustration'].mean())
# replacing nan values with mean of column
df['Digital_Illustration'].fillna((mean_df) , inplace = True)
df['Digital_Illustration'] = df['Digital_Illustration'].astype(int)
df['Digital_Illustration']


# In[16]:


# df['Product_Design']
df["Product_Design"] = pd.to_numeric(df["Product_Design"], downcast="float")
# finding mean of column
mean_df = (df['Product_Design'].mean())
# replacing nan values with mean of column
df['Product_Design'].fillna((mean_df) , inplace = True)
df['Product_Design'] = df['Product_Design'].astype(int)
df['Product_Design']


# In[17]:


# df['Growth_Marketing']
df["Growth_Marketing"] = pd.to_numeric(df["Growth_Marketing"], downcast="float")
# finding mean
mean_df = (df['Growth_Marketing'].mean())
# replacing nan values with mean of column
df['Growth_Marketing'].fillna((mean_df) , inplace = True)
df['Growth_Marketing'] = df['Growth_Marketing'].astype(int)
df['Growth_Marketing']


# In[18]:


# df['Leading_Groups']
df["Leading_Groups"] = pd.to_numeric(df["Leading_Groups"], downcast="float")
# finding mean of column
mean_df = (df['Leading_Groups'].mean())
# replacing nan values with mean of column 
df['Leading_Groups'].fillna((mean_df) , inplace = True)
df['Leading_Groups'] = df['Leading_Groups'].astype(int)
df['Leading_Groups']


# In[19]:


df[['Digital_Marketing' , 'Market_Research' , 'Digital_Illustration' , 'Product_Design' , 'Growth_Marketing' , 'Leading_Groups']].isnull().sum()


# In[ ]:




