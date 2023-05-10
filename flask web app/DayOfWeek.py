import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## Note that this was created by following a tutorial series https://youtu.be/vV12dGe_Fho and https://youtu.be/z3ZnOW-S550 by Rob Mulla for xgboost machinelearning forecasting.

## Getting a colour palette
color_pal = sns.color_palette()

## Reading a CSV file with all vulnerability data from 2017
data = pd.read_csv('full.csv')

## Indexing the data
data = data.set_index('date per day')

## Setting the datatype to datetime
data.index = pd.to_datetime(data.index)

# Function to index the day of week from the dataframe
data['day of week']= data.index.dayofweek

# Create the graph figure
fig, ax = plt.subplots(figsize=(10, 5))
#Boxplot with df as data, set x and y labels
plt.title('Relation by day of week')
sns.boxplot(data=data, x='day of week', y='Count of records')
#Display plot
plt.show()