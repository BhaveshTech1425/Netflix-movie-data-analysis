#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv("mymoviedb.csv",lineterminator = '\n')


# In[6]:


df.head()


# In[7]:


df.info()


# In[10]:


df['Genre']


# In[14]:


df.duplicated().sum()


# In[15]:


df.describe()

# Exploration summary


# we have a dataframe cosisting of 9827 rows and 9 columns
# our dataset looks a bit tidy with  no nans  nor duplicated values.
# Release_date column needs to be casted into date time and to extract only the year value.
# Overview, original_language and poster_Url wouldn't be so useful during analysis, so we'll drop them.
# there is noticable outliers in popularity column. 
# Vote_average better be categorized for proper analysis.
# Genre column has comma saperated values and white spaces that needs to be handled and casted into catefory .
# In[18]:


df['Release_Date'] = pd.to_datetime(df['Release_Date'])


# In[20]:


df.dtypes


# In[21]:


df['Release_Date'] = df['Release_Date'].dt.year


# In[22]:


df.head()


# # Dropping the columns

# In[23]:


cols = ['Overview','Original_Language','Poster_Url']


# In[24]:


df.drop(cols, axis = 1, inplace = True)
df.columns


# In[25]:


df.head()

# categorized Vote_Average column

# we would cut the  Vote_Average values and make 4 categorized: popular, average, below_avg, not_popular to describe it more using catigorize_col() function
# In[27]:


def categorize_col(df, col, labels):
    
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
    
    df[col] = pd.cut(df[col], edges, labels = labels, duplicates = 'drop')
    return df


# In[28]:


labels = ['not_popular', 'below_average', 'average', 'popular']

categorize_col(df, 'Vote_Average', labels)

df['Vote_Average'].unique()


# In[29]:


df.head()


# In[32]:


df['Vote_Average'].value_counts()


# In[33]:


df.dropna(inplace = True)

df.isna().sum()


# ## we'd split geners into a list and then explode our dataframe to have only one genre per row for each movie

# In[34]:


df['Genre'] = df['Genre'].str.split(', ')

df = df.explode('Genre').reset_index(drop = True)

df.head()


# In[35]:


# casting column into category

df['Genre'] = df['Genre'].astype('category')

df['Genre'].dtypes


# In[36]:


df.info()


# In[37]:


df.nunique()


# # Data visualization

# In[39]:


sns.set_style('whitegrid')


# ## What is the most frequent genre of movies released on Netflix?
# 

# In[40]:


df['Genre'].describe()


# In[53]:


sns.catplot(y = 'Genre', data = df, kind = 'count', order = df['Genre'].value_counts().index,color = 'r')
plt.title("Genre column distribution")
plt.show()


# # Which has highest votes in vote avg column?
# 

# In[46]:


plt.figure(figsize = (15,15))
sns.catplot(y ='Vote_Average', data = df, kind = 'count', order = df['Vote_Average'].value_counts().index,color = 'blue')
plt.title('Votes_distribution')
plt.show()


# # What movie got the highest popularity? what's its genre

# In[47]:


df.head(3)


# In[49]:


df[df['Popularity'] == df['Popularity'].max()]


# # What movie got the lowest popularity? what's its genre?
# 

# In[50]:


df[df['Popularity'] == df['Popularity'].min()]


# # Which year has the most filmmed movies?
# 

# In[51]:


df['Release_Date'].hist()
plt.title("Realese date column distribution")
plt.show


# # conclusion

# #Q1:What is the most frequent genre of movies released on Netflix?
#  ##   Drama genre is the most frequent genre in our dataset and has appeared more than 14% of the  times among 19 other genres.
#     
# #Q2:Which has highest votes in vote avg column?
#  ##  we have 25.5% of our dataset with popular vote(6520 rows) drama again gets the highest popularity among fans by being  having more than 18.5% of movies popularities.
# 
# #Q3:What movie got the highest popularity? what's its genre?
#  ##   spider man no way home has the highest popularity rate in our dataset and it has genres of action,adventure, and science fiction
#     
# #Q4:What movie got the lowest popularity? what's its genre?
#  ##   the united states, thread has the lowest  rate in our dataset and it has genres of music, drama , war, sci-fi, and history
#     
# #Q5:Which year has the most filmmed movies?
#   ##  year 2020 has the  highest filmming  rate in our dataset.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




