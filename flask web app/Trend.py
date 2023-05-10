import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

## Note data indexing was made with help from the tutorial https://youtu.be/vV12dGe_Fho by Rob Mulla and the trend decomposition was made with help from tutorial https://www.youtube.com/watch?v=0fWa9-Vj89g by Packt


## Reading a CSV file with all vulnerability from 2017
data = pd.read_csv('full.csv')

## Indexing the dataframe
data = data.set_index('date per day')

## Making so that the datatype is stored as datetime
data.index = pd.to_datetime(data.index)
# Setting the location of data to be the data.index (data.index by itself yields an empty graph)
data = data.loc[data.index]


# Create a decomposition of the data
decomposition = sm.tsa.seasonal_decompose(data)

# Create graph figure
fig, ax = plt.subplots(figsize=(13, 5))

#Set labels and titles
plt.title('Trend')
plt.xlabel('Date')
plt.ylabel('Count of Vulnerabilities')
# Plot the data
plt.plot(data, c='green')

# Plot the trend
plt.plot(decomposition.trend, c='red')

#Display plot
plt.show()
