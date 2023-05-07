import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import matplotlib.dates as mdates
import statsmodels.api as sm


df = pd.read_csv('alldata.csv')


df = df.set_index('Vulnerabilities per 30 days')


df.index = pd.to_datetime(df.index)

de= df.set_index('Count of Vulnerabilities')


gammel = df.loc[df.index < '2017-08-30']
videre = df.loc[de.index >= '27-08-2017']


if ',' in videre:
    videre.replace(',', '')
else:
    print('what')

print(videre)
#decomposition = sm.tsa.seasonal_decompose(gammel)


def Creation(df):
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    return df

df = Creation(df)

decomposition = sm.tsa.seasonal_decompose(videre)
fig, ax = plt.subplots(figsize=(10, 5))

ax.grid(True)
plt.plot(videre, c='blue')
plt.plot(decomposition.trend, c='red')
plt.show()