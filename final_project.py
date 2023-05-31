#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pathlib as path
import pandas as pd
import numpy as np
import csv
from IPython.display import display
import re
from sklearn.linear_model import LinearRegression
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3


# In[181]:


#data cleaning and organization

def delist(args):
    delist = [var for small_list in args for var in small_list]
    return (delist)


_path = path.Path.cwd()

rw_metadata = []
rw_data = []

cs_metadata = []
cs_data = []

#open csv and extract information
for _filename in _path.iterdir():
    if _filename.stem == 'Rainier_Weather':
        with open(_filename) as file:
            rows = list(csv.reader(file))

            metadata = rows[0]
            data = rows[1:]

            new_data = []

            for var in data:
                float_var = []
                for subvar in var:
                    try:
                        floater = float(subvar)
                        float_var.append(floater)

                    except:
                        float_var.append(subvar)
                new_data.append(float_var)

            for var in metadata:
                rw_metadata.append(var)

            for var in new_data:
                rw_data.append(var)



    elif _filename.stem == 'climbing_statistics':
        with open(_filename) as file:
            # data = file.read()
            rows = list(csv.reader(file))

            metadata = rows[0]
            data = rows[1:]
            new_data = []

            # remove unwanting chars in Date column
            date_clean = re.compile(r'(?<=\ufeff)Date')
            date_cleaned = date_clean.findall(metadata[0])
            metadata[0] = "".join(date_cleaned)
           

            for var in data:
                float_var = []
                for subvar in var:
                    try:
                        floater = float(subvar)
                        float_var.append(floater)
                    except:
                        float_var.append(subvar)
                new_data.append(float_var)

            for var in metadata:
                cs_metadata.append(var)

            for var in new_data:
                cs_data.append(var)

    else:
        pass

#dataframe generation
df_cs = pd.DataFrame(cs_data, columns=cs_metadata)
df_rw = pd.DataFrame(rw_data, columns=rw_metadata)

df_combined = df_cs.merge(df_rw, how='inner', on='Date')
df_combined.sort_values(by=['Date'])
display(df_combined)


# After loading the datasets into python, I transformed them into two dataframes. First, df_cs is all about climbing statistics. We see dates, routes, attempts, successes and the success percentage. Second, we have df_rw which reveals different weather attributes on a series of dates. We have much more data on df_cs, so I performed an inner join combining the two, only when they had dates in common. 

# In[182]:


##Tier 1 (1/5, 2/5, 3/5, 4/5, 5/5) column data

def statistics(df, row):
    _min = round(df.iloc[:,row].min(),2)
    _max = round(df.iloc[:,row].max(),2)
    _mean = round(df.iloc[:,row].mean(),2)
    _median = round(df.iloc[:,row].median(),2)
    _stdev = round(df.iloc[:,row].std(),2)

    return [_min, _max, _mean, _median, _stdev]


stats = {}
stats['Attempted'] = statistics(df_combined,2)
stats['Succeeded'] = statistics(df_combined,3)
stats['Success Percentage'] = statistics(df_combined, 4)
stats['Battery Voltage AVG'] = statistics(df_combined, 5)
stats['Temperature AVG'] = statistics(df_combined, 6)
stats['Relative Humidity AVG'] = statistics(df_combined, 7)
stats['Wind Speed Daily AVG	Wind Direction '] = statistics(df_combined, 8)
stats['Wind Direction AVG'] = statistics(df_combined, 9)
stats['Solare Radiation AVG'] = statistics(df_combined, 10)

df_stats = pd.DataFrame(stats, index=['Min', 'Max', 'Mean', 'Median', 'Stdev'])
display(df_stats)


# Next, we have interesting statistics laid out for the viewer. These correspond to each column in the df_combined. I have listed notable features, revealing important attributed regarding the dataset. 
# 
# We can also see an outlier in the data regarding the "Succeeded." I assume this is a typo as it is far more than the attempts. From this, we can remove the outlier as it does not make sense and will alter the data trends.

# In[184]:


#remove outliers... basically anything with a success % over 1 & confirm
pattern_remove = []

for var in df_combined.iloc[:,4]:
    if var > 1:
        pattern_remove.append(var)

def indexer_drop(df, row, item):
    '''Count the number of occurences of item in row of df and remove from table'''
    index_list = []
    index = df.index[df.iloc[:,row] == item].to_list()
    index_list.append(index)
    df.drop(index=index_list[0], inplace=True)

print(len(df_combined))

for var in pattern_remove:
    indexer_drop(df_combined,4,var)

print(len(df_combined))


# With the row corresponding to the invalid input dropped, we can now relook at our statistics.

# In[185]:


stats2 = {}
stats2['Attempted'] = statistics(df_combined,2)
stats2['Succeeded'] = statistics(df_combined,3)
stats2['Success Percentage'] = statistics(df_combined, 4)
stats2['Battery Voltage AVG'] = statistics(df_combined, 5)
stats2['Temperature AVG'] = statistics(df_combined, 6)
stats2['Relative Humidity AVG'] = statistics(df_combined, 7)
stats2['Wind Speed Daily AVG	Wind Direction '] = statistics(df_combined, 8)
stats2['Wind Direction AVG'] = statistics(df_combined, 9)
stats2['Solare Radiation AVG'] = statistics(df_combined, 10)

df_stats2 = pd.DataFrame(stats2, index=['Min', 'Max', 'Mean', 'Median', 'Stdev'])
display(df_stats2)


# We see that the average success percentage over the time period between 09/23/2014 to 11/27/2015 was just under half; ringing in at a mean of 0.45. While there were some days with no successes and others with all!
# 
# On the mountain itself, it is important to note how the data was collected and reviewing the battery usage. It would be significant if we saw a larger standard deviation, as this would mean flucations in voltage output averages per day. Yet, we have consistent output, so I can assume our data from the mountain is valid. 
# 
# We see an average temperature of 40.71 F with an average humidity at 47.84%. Temperatures dropped to a low of around 6 as a minimum and up to 56 while data was being collected. There were instances with no wind, and others with gusts up to 65 MPH (average per day). Solar radiation corresponds to the amount of energy output by the sun, we see there were somedays where the detecting device recieved no sun (0 solar radiation) and other days were there was up to 368 kWh/m2.

# In[186]:


#tier 2 (1/2, 2/2)
route_analysis = {}
route_analysis['route_count'] = df_combined.groupby("Route")["Attempted"].count()
route_analysis['route_success'] = df_combined.groupby("Route")['Success Percentage'].mean()

df_route = pd.DataFrame(route_analysis)
df_route.sort_values(by=['route_success', 'route_count'], inplace=True)
pd.set_option('display.max_rows', None)

display(df_route)
fig, ax = plt.subplots()
display(sns.histplot(df_combined, x="Route"))
plt.xticks(rotation=90)
ax.set(xlabel='Count', ylabel='Route', title='Count of Routes Attempted')


# Tier 3 (1/3)
# 
# Data reveals a notable difference in the routes attempted, with well over half the attempts on Disappointment Cleaver. However, Gibralter Chute and Sunset RIngraham Directge saw the fewest attempts, with no successful summit bids.
# 
# While Tahoma Cleaver has the highest success percentage, it only has a single attempt. This skews the data a bit when we consider which route has the highest percentage of success. 
# 
# Notable, Emmons-Winthrop has the second highest, with just over every 1 in 2 parties sending successfully.
# 

# In[188]:


#Tier 3 (1/1), looking at the effects of weather patterns on successful bids

def regression_function(x,y):
    shape_x = np.array(x).reshape(-1,1)
    global model
    model = LinearRegression().fit(shape_x, y)
    r2_val = round(model.score(shape_x, y),4)
    global intercept
    intercept = round(model.intercept_, 4)
    global slope
    slope = model.coef_
    
    equation = f'y={slope}x + {intercept}, r2 = {r2_val}'
    return equation


# Overall, in this dataset I am trying to analyze the most common routes climbed, which route has the highest success rate, and to see if weather features have any effect on the success of the climbs. I have touched on the first two, and now will go into depth on the last.
# 
# 
# This final idea is displayed below by attempting to show a relationship between success percentage & different weather variables.

# In[189]:


#comparing IV (Temperature AVG) to DV (success percentage)
temp_equation = regression_function(df_combined.iloc[:,6], df_combined.iloc[:,4])
print(temp_equation)
fig, ax = plt.subplots()
plt.scatter(df_combined.iloc[:,6], df_combined.iloc[:,4])
ax.set(xlabel = 'daily temperature average', ylabel='success percentage', title='Daily Temperature Average vs. Success Percentage')
ax.grid()


# There is a minor trend (r2=0.0166) seen on the low end, with average daily temperatures lower than roughly 20F (1 exception) and 0% success. Above this, there is not much of a trend.

# In[190]:


#comparing IV (Relative Himidity Average AVG) to DV (success percentage)
temp_equation = regression_function(df_combined.iloc[:,7], df_combined.iloc[:,4])
print(temp_equation)
fig, ax = plt.subplots()
plt.scatter(df_combined.iloc[:,7], df_combined.iloc[:,4])
ax.set(xlabel = 'relative humidity average', ylabel='success percentage', title='Relative Humidity Average vs. Success Percentage')
ax.grid()


# No trend observed

# In[191]:


#comparing IV (Wind Speed AVG) to DV (success percentage)
temp_equation = regression_function(df_combined.iloc[:,8], df_combined.iloc[:,4])
print(temp_equation)
fig, ax = plt.subplots()
plt.scatter(df_combined.iloc[:,8], df_combined.iloc[:,4])
ax.set(xlabel = 'wind speed daily average', ylabel='success percentage', title='Wind Speed Daily Average vs. Success Percentage')
ax.grid()


# There is a noteable trend on the high end of the chart. We see when wind speeds get above roughly 38, there are far less successful summit bids (with 2 exceptions).

# In[192]:


#comparing IV (Wind Direction AVG) to DV (success percentage)
temp_equation = regression_function(df_combined.iloc[:,9], df_combined.iloc[:,4])
print(temp_equation)
fig, ax = plt.subplots()
plt.scatter(df_combined.iloc[:,9], df_combined.iloc[:,4])
ax.set(xlabel = 'wind direction average', ylabel='success percentage', title='Wind Direction Average vs. Success Percentage')
ax.grid()


# No trend observed.

# In[193]:


#comparing IV (Solar Radiation AVG) to DV (success percentage)
temp_equation = regression_function(df_combined.iloc[:,10], df_combined.iloc[:,4])
print(temp_equation)
fig, ax = plt.subplots()
plt.scatter(df_combined.iloc[:,10], df_combined.iloc[:,4])
ax.set(xlabel = 'solar radiation average', ylabel='success percentage', title='Solar Radiation Average vs. Success Percentage')
ax.grid()


# There is a small trend seen here will higher solar radiation having a larger portion of the successful bids. While it is minor it is observed.

# Overall, it seems with higher solar radiation averages, higher daily average temperatures, & lower average wind speeds there is an increased chance of a successful summit bid. While the data isn't profoundly in support of this, there is data to show these trends.

# In[194]:


#create storage method for df
try:
    conn = sqlite3.connect('climbing_db.sqlite', timeout=10)
    cur = conn.cursor()
except sqlite3.Error as error:
    print('error connecting due to,', error)


# In[195]:


#upload dataframes to SQLite3 database
df_cs.to_sql('df_cs', con=conn, if_exists='replace')
df_rw.to_sql('df_rw', con=conn, if_exists='replace')
df_combined.to_sql('df_combined', con=conn, if_exists='replace')
df_route.to_sql('df_route', con=conn, if_exists='replace')


# In[196]:


#testing uploading to database
cur.execute("SELECT * FROM df_route").fetchall()

