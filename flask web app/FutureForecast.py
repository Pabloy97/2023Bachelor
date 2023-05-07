import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xg

## Note that this was created by following a tutorial series https://youtu.be/vV12dGe_Fho and https://youtu.be/z3ZnOW-S550 by Rob Mulla for xgboost machinelearning forecasting.

## Getting a colour palette
color_pal = sns.color_palette()

## Reading a CSV file with all vulnerability data and calling it dataframe

df = pd.read_csv('full.csv')

## Indexing the dataframe inside ('') have the text which is refered to in the CSV file that is read from

df = df.set_index('date per day')
## Making so that the datatype is stored as datetime
df.index = pd.to_datetime(df.index)


#creating functions 
# This part is taken from "kilde"

def Creation(df):
    df = df.copy()
    df['day of week'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    return df
# letting the new dataframe function be the functions of the original dataframe
df = Creation(df)



# Adding the features
Feats = ['day of week', 'quarter', 'month', 'year',
       'dayofyear']

# The target, let this be the second title which is in the CSV file
Targ = 'Count of records'



#Create functions for all data of the dataframe with the features and the target
x_alldata = df[Feats]
y_alldata =df[Targ] 
# Create a regressionmodel with how many rounds it should iterate
regressionmodel = xg.XGBRegressor(n_estimators=1000, early_stopping_rounds=50,
                                  learning_rate=0.01)
# Fit the data in the regressionmodel
regressionmodel.fit(x_alldata, y_alldata,
                    eval_set=[(x_alldata, y_alldata)],
                    verbose=100)


# Set the range of the time from either the first data if you want to see the original data and then the forecast or the last date in the dataframe and then the
# date you wish to forecast to. Frequency is set to 24h to specify one forecast each day can also be set with 1d.
frem = pd.date_range('2017-12-31', '2019-01-01', freq='1d')
# Creating the new dataframe for the future indexing the time to be what is set.
fremtidig_df = pd.DataFrame(index=frem)
# Saying that this new dataframe is the future data
fremtidig_df['isFuture'] = True
# Setting that the old dataframe is not the future ata
df['isFuture'] = False

df_and_fremtid = pd.concat([df, fremtidig_df]) 
# adding the old and new dataframe together with the features from the creation define function
df_and_fremtid =  Creation(df_and_fremtid)
# Query the future data from the added dataframe
fremtid_w_feats = df_and_fremtid.query('isFuture').copy()
#Predict the future data using the regression model predict function with look a the features.
fremtid_w_feats['pred'] = regressionmodel.predict(fremtid_w_feats[Feats])
# Plot the forecast graph
fremtid_w_feats['pred'].plot(figsize=(15, 5),
                            color=color_pal[5],
                            ms=1,
                            lw=1,
                            title='Fremtid')
plt.show()