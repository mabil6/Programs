#!/usr/bin/env python
# coding: utf-8

# Data Science Visualization Peer Review Assignment

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as ply
import matplotlib.patches as patches
get_ipython().run_line_magic('matplotlib', 'inline')


# Question 1

# In[31]:


df = pd.read_csv('https://cocl.us/datascience_survey_data',index_col=0)
df


# In[32]:


df.shape


# In[33]:


df.info()


# In[34]:


df.describe()


# #Question 2

# In[35]:


#create new dataset with percentages
respondents=2233
df=round((df/respondents)*100,2)
df


# In[36]:


df.sort_values(['Very interested'], ascending=False, axis=0, inplace=True)
#create bar graph
bar=df.plot(kind='bar',figsize=(20,8),rot=90,width=.8,fontsize=14,color=['#5cb85c','#5bc0de','#d9534f'])
ply.title("Percentage of Respondents' Interest in Data Science Areas",fontsize=16)
bar.legend(fontsize=14)
bar.set_frame_on(False)
bar.get_yaxis().set_visible(False)
for i in bar.patches:
    bar.annotate(np.round(i.get_height(),decimals=2),
                (i.get_x()+i.get_width()/2., i.get_height()),
                ha='center',
                va='center',
                xytext=(0, 10),
                textcoords='offset points',
                fontsize = 14
                )
ply.show()


# Question 3

# In[25]:


df_crime = pd.read_csv('https://cocl.us/sanfran_crime_dataset')
df_crime.head()


# In[26]:


#create the dataframe and reindex 

df_crime=df_crime['PdDistrict'].value_counts()
df_crime=pd.DataFrame(df_crime)
df_crime=df_crime.reindex(["CENTRAL", "NORTHERN", "PARK", "SOUTHERN", "MISSION", "TENDERLOIN", "RICHMOND", "TARAVAL", "INGLESIDE", "BAYVIEW"])
df_crime=df_crime.reset_index()
df_crime.columns=['Neighborhood', 'Counts']
df_crime


# #Question 4

# In[13]:


#!conda install -c conda~forge folium=0.5.0 --yes
get_ipython().system('pip install folium==0.5.0')
import folium


# In[14]:


get_ipython().system('wget --quiet https://cocl.us/sanfran_geojson ')


# In[15]:


sf_geo=r'sanfran_geojson'


# In[27]:


sf_latitude=37.77
sf_longitude=-122.42


# In[30]:


sf_map=folium.Map(location=[sf_latitude,sf_longitude],zoom_start=12)
sf_map.choropleth(
    geo_data=sf_geo,
    data=df_crime,
    columns=['Neighborhood', 'Counts'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco'
)
sf_map


# In[ ]:




