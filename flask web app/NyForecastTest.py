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
from sklearn.model_selection import TimeSeriesSplit

#pycurl -X GET localhost:5601/api/index_patterns/index_pattern/Nettside-eksempel

#url="http://localhost:5601/goto/b52477f0-d148-11ed-81d2-55f73385f722"

#reqs = requests.get(url)
#print(reqs)

## Getting a colour palette
color_pal = sns.color_palette()

## Reading a CSV file with all vulnerability data and calling it dataframe
#df = pd.read_csv('untitled.csv')
df = pd.read_csv('full.csv')

## Indexing the dataframe
#df = df.set_index('Vulnerabilities per day')
df = df.set_index('date per day')
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
gammel = df.loc[df.index < '2017-05-30']
videre = df.loc[df.index >= '30-05-2017']

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

Targ = 'Count of records'
#'Count of Vulnerabilities'



x_alldata = df[Feats]
y_alldata =df[Targ]  
regressionmodel = xg.XGBRegressor(n_estimators=1000, early_stopping_rounds=50,
                                  learning_rate=0.01)
regressionmodel.fit(x_alldata, y_alldata,
                    eval_set=[(x_alldata, y_alldata)],
                    verbose=100)



frem = pd.date_range('2017-01-1', '2019-01-01', freq='24h')
fremtidig_df = pd.DataFrame(index=frem)
fremtidig_df['isFuture'] = True
df['isFuture'] = False
df_and_fremtid = pd.concat([df, fremtidig_df]) 
df_and_fremtid =  Creation(df_and_fremtid)
fremtid_w_feats = df_and_fremtid.query('isFuture').copy()

fremtid_w_feats['pred'] = regressionmodel.predict(fremtid_w_feats[Feats])
fremtid_w_feats['pred'].plot(figsize=(15, 5),
                            color=color_pal[5],
                            ms=1,
                            lw=1,
                            title='Fremtid')
plt.show()