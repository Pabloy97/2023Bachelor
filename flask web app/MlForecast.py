import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import matplotlib.dates as mdates
import statsmodels.api as sm
from datetime import datetime
import json
import xgboost as xg
import sklearn as sk
#pycurl -X GET localhost:5601/api/index_patterns/index_pattern/Nettside-eksempel

#url="http://localhost:5601/goto/b52477f0-d148-11ed-81d2-55f73385f722"

#reqs = requests.get(url)
#print(reqs)

## Getting a colour palette
color_pal = sns.color_palette()

## Reading a CSV file with all vulnerability data and calling it dataframe
df = pd.read_csv('untitled.csv')

## Indexing the dataframe
df = df.set_index('Vulnerabilities per day')

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
gammel = df.loc[df.index < '2017-08-31']
videre = df.loc[df.index >= '01-08-2017']

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

#decomposition.plot()
#plt.show()

def Creation(df):
    df = df.copy()
    df['day of week'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    return df

df = Creation(df)

jau = Creation(gammel)
train = Creation(videre)
Feats = ['day of week', 'quarter', 'month', 'year',
       'dayofyear']

Targ ='Count of Vulnerabilities'



x_tren = train[Feats] 
y_tren = train[Targ]

x_jau = jau[Feats] 
y_jau = jau[Targ] 
regressionmodel = xg.XGBRegressor(n_estimators=300, early_stopping_rounds=50,
                                  learning_rate=0.01)
re = regressionmodel.fit(x_tren, y_tren, 
                    eval_set=[(x_tren, y_tren), (x_jau, y_jau)],  
                    verbose=True)

#test = pd.DataFrame(data=regressionmodel.feature_importances_,
                    #index=regressionmodel.feature_names_in_,
                    #columns=['importance'])

#test.sort_values('importance').plot(kind='barh', title='Feature')

a = jau['prediction'] = regressionmodel.predict(x_jau)
df = df.merge(jau[['prediction'] ] , how='left', left_index=True, right_index=True)

ax=df[['Count of Vulnerabilities']].plot(figsize=(15, 10))
df['prediction'].plot(ax=ax, style='.')
ax.set_title('yahoo')
plt.show()

ax=df.loc[(df.index > '2017-08-01') & (df.index < '2017-08-21')]['Count of Vulnerabilities'].plot(figsize=(15, 10), title='yahoo')
df.loc[(df.index > '2017-08-01') & (df.index < '2017-08-21')]['prediction'].plot(style='.')

plt.show()