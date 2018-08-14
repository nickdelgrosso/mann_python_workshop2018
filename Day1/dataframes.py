
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# # Pandas and DataFrames
# 
# Often, we have tables of data--collections of named columns arranged in rows.  The **Pandas** package gives us a **DataFrame()** class that lets us index these columns the same way as with dicts, while still getting the benefit of Numpy arrays, meaning we can still write vectorized code.  
# 
# Let's start playing with the analysis now.  We'll examine Pandas in more depth in the coming days.

# In[2]:


import pandas as pd


# Please open the file “MentalRotationData.xlsx” and use it to answer the following questions about the results of the Mental Rotation psychology experiment. If you reach the end of the exercises, explore the dataset and DataFrames more and see what you can find about this experiment!

# In[3]:


df = pd.read_csv('MentalRotation.csv')
df.head()


# ## Examining the Dataset
# 
# **head()**, **tail()**, **sample()**

# Look at the first 5 lines of the dataset

# In[4]:


df.head()


# Look at the last 5 lines of the dataset

# In[5]:


df.tail()


# Check 3 random lines in the dataset.

# In[6]:


df.sample(3)


# How Many Total Trials (rows) are in the study?

# In[7]:


len(df)


# In[8]:


df.shape[0]


# In[9]:


df.info()


# What is the maximum number of trials that one subject performed?

# In[10]:


df['Trial'].max()


# ### Making New Columns

# Convert the Time column to seconds by dividing it by 1000.

# In[11]:


df['TimeSec'] = df['Time'] / 1000
df.head()


# Change the "Correct" column to *bool* (True/False) using the **astype()** method

# In[22]:


df['isCorrect'] = df['Correct'].astype(bool)
df.head()


# ### The mean() method

# What is the mean response time, across all trials?

# In[23]:


df['TimeSec'].mean()


# In[26]:


import numpy as np
np.mean(df['TimeSec'])


# What percent of trials were answered correctly?

# In[35]:


np.mean(df['isCorrect'] == True)


# In[38]:


df['isCorrect'].mean()


# In[39]:


df['Correct'].mean()


# What percent of trials were “Matching” trials?

# In[41]:


df['Matching'].mean()


# ### Slicing

# Is there a difference in accuracy between matching and non-matching trials?

# In[48]:


isMatching = df.loc[df['Matching'] == 1, 'Correct']
notMatching = df.loc[df['Matching'] == 0, 'Correct']
isMatching.mean(), notMatching.mean()


# In[49]:


isMatching = df[df['Matching'] == 1]['Correct']
notMatching = df[df['Matching'] == 0]['Correct']
isMatching.mean(), notMatching.mean()


# In[50]:


isMatching = df['Correct'].loc[df['Matching'] == 1]
notMatching = df['Correct'].loc[df['Matching'] == 0]
isMatching.mean(), notMatching.mean()


# In[51]:


df.groupby('Matching')['Correct'].mean()


# Is there a response time difference between matching and nonmatching
# trials?

# Is there a response time difference between matching and nonmatching
# trials, for different rotation Angles?

# In[58]:


df.groupby(['Matching', 'Angle'])['TimeSec'].mean().unstack()


# ### Plotting

# Plot the response time distribution as a histogram.

# In[64]:


3;


# In[67]:


df.TimeSec.plot.hist();


# In[78]:


df.hist();


# Is there a correlation between Angle of mental rotation and response time?  Visualize the relationship

# In[72]:


df.plot.box(by='Angle')

