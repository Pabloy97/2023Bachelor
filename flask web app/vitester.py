#import requests
#import pycurl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import matplotlib.dates as mdates
import statsmodels.api as sm
from datetime import datetime
#pycurl -X GET localhost:5601/api/index_patterns/index_pattern/Nettside-eksempel

#url="http://localhost:5601/goto/b52477f0-d148-11ed-81d2-55f73385f722"

#reqs = requests.get(url)
#print(reqs)

## Getting a colour palette
color_pal = sns.color_palette()

## Reading a CSV file with all vulnerability data and calling it dataframe
df = pd.read_csv('what.csv')

## Indexing the dataframe
df = df.set_index('date per month')

## Making so that the datatype is stored as datetime
df.index = pd.to_datetime(df.index)

#print(df.index)

#df = df.set_index('Datetime')
    #df.plot(style='', figsize=(15,5), color=color_pal[3], title = 'test')
#df.head()
#<iframe src="http://localhost:5601/goto/9164b550-d201-11ed-81d2-55f73385f722" width="50%" height="500"> </iframe>
#plt.save(a)
#plt.plot(df)
    #plt.show()

## Localise certian dates within the dataframe to use for the forecast analysis
gammel = df.loc[df.index < '2017-08-30']
videre = df.loc[df.index >= '27-08-2017']

#s_d = datetime('2017, 02, 04')
#e_d = datetime('2017, 10, 8')

#df.plot(style='', figsize=(15,5), color=color_pal[3], title = 'test')

#fig, ax = plt.subplots(figsize=(15, 5))
#gammel.plot(ax=ax, label='Dagens data', title='Earlier data')
#videre.plot(ax=ax, label='Newest data')
#ax.axvline('27-08-2017', color='black', ls='--')
#ax.legend(['Dagens data', 'Newest data'])
#plt.show()
#print(df.index.month)
#fig, ax = plt.subplots(figsize=(15, 5))
decomposition = sm.tsa.seasonal_decompose(gammel)

print(decomposition.trend)
#decomposition.plot()
#plt.show()

def Creation(df):
    df['day of week'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    return df

df = Creation(df)



fig, ax = plt.subplots(figsize=(10, 5))

#fig, ax = plt.subplots(figsize=(15, 5))
#<iframe src="http://localhost:5601/goto/9164b550-d201-11ed-81d2-55f73385f722" width="50%" height="500"> </iframe>


    #sns.barplot(data=df, x='dayofweek',y ='Count of Vulnerabilities')
    #ax.set_title('Something')
    #plt.show()
#print(df.index)
ax.grid(True)
plt.plot(gammel, c='blue')
plt.plot(decomposition.trend, c='red')
plt.show()
 #style="position:absolute; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; padding:0; overflow:hidden; z-index:9;" 
    #style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; padding:0; overflow:hidden; z-index:999999;" 
    #<iframe src="http://localhost:5601/goto/dff8b800-d900-11ed-81d2-55f73385f722" height="600" width="800"></iframe> 
    #<iframe src="http://localhost:5601/app/dashboards#/view/3b66c9c0-cee8-11ed-87fe-53cf7399d29b?embed=true&_g=(filters%3A!()%2CrefreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3A'2017-08-01T03%3A15%3A37.072Z'%2Cto%3A'2017-09-01T00%3A00%3A00.000Z'))&show-top-menu=true&show-query-input=true&show-time-filter=true" height="600" width="800"></iframe> 