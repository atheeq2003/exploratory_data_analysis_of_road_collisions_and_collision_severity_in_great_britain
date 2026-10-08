#!/usr/bin/env python
# coding: utf-8

# # Data Loading
# 
# This notebook contains the steps for the loading the dataset and gathering info on the dataset.
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

raw_df = pd.read_csv(r"dft-road-casualty-statistics-collision-2025.csv")
raw_df.head()


# In[2]:


raw_df.shape


# In[3]:


# Making a copy of the raw data

cleaned_df = raw_df.copy()


# In[4]:


cleaned_df.shape


# In[5]:


cleaned_df.head()


# In[6]:


cleaned_df.info()


# In[7]:


cleaned_df.describe()


# In[8]:


cleaned_df.describe(include=["object"])


# In[9]:


cleaned_df.columns


# In[10]:


cleaned_df.dtypes

