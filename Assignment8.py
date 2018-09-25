
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

izero = np.r_[-1, (df['X'] == 0).nonzero()[0]] # indices of zeros
idx = np.arange(len(df))
df['Y'] = idx - izero[np.searchsorted(izero - 1, idx) - 1]

print(df['Y'])


# In[5]:


import pandas as pd
dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
print(dti)
print('\n\n')

#Index the series, s be the index
s = pd.Series(np.random.rand(len(dti)), index=dti)
print(s)


# 3) Find the sum of the values in s for every Wednesday

# In[6]:


s[dti.weekday == 2].sum() 


# 4) Average For each calendar month

# In[7]:


s.resample('M').mean()


# 5) For each group of four consecutive calendar months in s, find the date on which the
# highest value occurred.

# In[8]:


s.groupby(pd.Grouper(freq='4M')).idxmax()

