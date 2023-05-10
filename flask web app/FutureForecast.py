import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xg

## Note that this was created by following a tutorial series https://youtu.be/vV12dGe_Fho and https://youtu.be/z3ZnOW-S550 by Rob Mulla for xgboost machinelearning forecasting.

## Getting a colour palette
color_pal = sns.color_palette()

## Reading a CSV file with all vulnerability data from 2017

data = pd.read_csv('full.csv')

## Indexing the data
data = data.set_index('date per day')

## Setting the datatype to datetime
data.index = pd.to_datetime(data.index)


#creating functions 
# This part is taken from https://youtu.be/vV12dGe_Fho
# Make functions to get every day of week, quarter, each month, year and the day of the year.
def Creation(data):
    data = data.copy()
    data['day of week'] = data.index.dayofweek
    data['quarter'] = data.index.quarter
    data['month'] = data.index.month
    data['year'] = data.index.year
    data['dayofyear'] = data.index.dayofyear
    return data
# Applying functions to data
data = Creation(data)



# Adding the features
Feats = ['day of week', 'quarter', 'month', 'year',
       'dayofyear']

# The target, let this be the second title which is in the CSV file
Targ = 'Count of records'



#Create functions for all data with the features and the target
x_alldata = data[Feats]
y_alldata =data[Targ] 
# Create a regressionmodel
regressionmodel = xg.XGBRegressor(n_estimators=1000, early_stopping_rounds=50,
                                  learning_rate=0.01)
# Fit the data in the regressionmodel
regressionmodel.fit(x_alldata, y_alldata,
                    eval_set=[(x_alldata, y_alldata)],
                    verbose=50)


# Set the range of the time from either the first data if you want to see the original data and then the forecast or the last date in the dataframe and then the
# date you wish to forecast to. Frequency is set to 24h to specify one forecast each day can also be set with 1d.
fremtidig = pd.date_range('2017-12-31', '2019-01-01', freq='1d')
# Creating the new dataframe for the future
fremtidig_data = pd.DataFrame(index=fremtidig)
# Saying that this new data is the future data
fremtidig_data['isFuture'] = True
# Setting that the old data is not the future ata
data['isFuture'] = False

data_and_fremtid = pd.concat([data, fremtidig_data]) 
# adding the old and new ddata together with the features from the creation define function
data_and_fremtid =  Creation(data_and_fremtid)
# Query the future data from the added dataframe
fremtid_w_feats = data_and_fremtid.query('isFuture').copy()
#Predict the future data using the regression model predict function with look a the features.
fremtid_w_feats['pred'] = regressionmodel.predict(fremtid_w_feats[Feats])
# Plot the forecast graph
fremtid_w_feats['pred'].plot(figsize=(15, 5),
                            xlabel='Date',
                            ylabel='Count',
                            color=color_pal[3],
                            ms=1,
                            lw=1,
                            title='Future')
plt.show()