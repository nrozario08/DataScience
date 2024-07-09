#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings


# In[5]:


df = pd.read_csv('full_grouped.csv')


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.isna().sum()


# In[11]:


print(df['Country/Region'].nunique())

print(df['WHO Region'].unique())


# In[12]:


df.isnull().sum()


# In[13]:


df.duplicated().sum()


# In[14]:


df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'].dtype)


# In[22]:


df = df.rename(columns = {'Country/Region':'Country'})


# In[23]:


df.columns


# In[26]:


Who_regions = df.groupby('WHO Region')['Confirmed'].sum().sort_values()
Who_regions


# In[58]:


who_regions = df.groupby('WHO Region')['Confirmed'].sum().sort_values()
explode = [0,0,0,0,0.01,0.05]
plt.figure(figsize = (10,6))
plt.style.use('dark_background')
plt.pie(who_regions.values, explode = explode, labels= who_regions.index,
       autopct = '%1.1f%%', pctdistance = 0.8, startangle = 305,
       colors = plt.cm.Paired.colors, textprops = {'fontsize':10})
plt.title('Distribution of COVID cases in WHO regions',fontsize =15, 
          weight = 'bold', loc ="left")
plt.show()


# In[45]:


grouped_data_dates = df.groupby('Date').agg({'Confirmed':'sum',
                                            'Deaths':'sum',
                                            'Recovered':'sum',
                                            'Active':'sum',
                                            'New cases':'sum',
                                            'New deaths':'sum',
                                            'New recovered':'sum'}).reset_index()
grouped_data_dates.tail()


# In[65]:


plt.figure(figsize = (10,6))
plt.style.use('seaborn')
plt.plot(grouped_data_dates['Date'], grouped_data_dates['Confirmed'],
        linestyle = '-', color = '#051282',label = 'Confirmed',lw =3)
plt.plot(grouped_data_dates['Date'], grouped_data_dates['Deaths'],
        linestyle = '-.', color = '#ed0231',label = 'Deaths')
plt.plot(grouped_data_dates['Date'], grouped_data_dates['Recovered'],
        linestyle = '--', color = '#30c90e',label = 'Recovered', lw=2)
plt.plot(grouped_data_dates['Date'], grouped_data_dates['Active'],
        linestyle = ':', color = '#000000',label = 'Active',lw =2)
plt.xlabel('Date')
plt.ylabel('No: of cases(in millions)')
plt.title('Global Trend of Covid Cases')
plt.legend()
plt.show()


# In[68]:


country_grouped = df.groupby('Country').max()
country_grouped.sample(6)


# In[73]:


top10_confirmed = country_grouped.nlargest(10,'Confirmed')

plt.figure(figsize=(12,6))
plt.style.use('dark_background')
sns.barplot(x = top10_confirmed['Confirmed'].sort_values(ascending = False),
            y = top10_confirmed.index,palette = 'BrBG')
plt.title('Top 10 Countries with the Highest Confirmed Cases')
plt.xlabel('Number of Confirmed Cases(in millions)')
plt.ylabel('Country')
plt.show()

top10_deaths = country_grouped.nlargest(10,'Deaths')

plt.figure(figsize=(12,6))
plt.style.use('dark_background')
sns.barplot(x = top10_deaths['Deaths'].sort_values(ascending = False),
            y = top10_deaths.index,palette = 'RdBu')
plt.title('Top 10 Countries with the Highest Deaths')
plt.xlabel('Number of Deaths(in millions)')
plt.ylabel('Country')
plt.show()

top10_recovered = country_grouped.nlargest(10,'Recovered')

plt.figure(figsize=(12,6))
plt.style.use('dark_background')
sns.barplot(x = top10_recovered['Recovered'].sort_values(ascending = False),
            y = top10_recovered.index,palette = 'Set2')
plt.title('Top 10 Countries with the Highest Recovered Cases')
plt.xlabel('Number of Recovered Cases(in millions)')
plt.ylabel('Country')
plt.show()


# In[76]:


correlation_matrix = df[['Confirmed','Deaths','Recovered']].corr()
correlation_matrix


# In[78]:


plt.style.use('dark_background')
sns.heatmap(correlation_matrix,annot = True, cmap = 'coolwarm',fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# In[79]:


plt.figure(figsize = (10,6))
plt.style.use('dark_background')

plt.plot(grouped_data_dates['Date'],grouped_data_dates['New cases'],
         linestyle = '-',color = '#051282',label = 'New Cases',lw = 2)

plt.plot(grouped_data_dates['Date'],grouped_data_dates['New deaths'],
         linestyle = '-',color = '#ed0231',label = 'New Deaths',lw = 2)

plt.plot(grouped_data_dates['Date'],grouped_data_dates['New recovered'],
         linestyle = '-',color = '#30c90e',label = 'New Recoveries',lw = 2)
plt.xlabel('Date')
plt.ylabel('No: of cases (in millions)')
plt.title('Daily New Cases, Deaths and Recoveries')
plt.legend()
plt.show()


# In[ ]:




