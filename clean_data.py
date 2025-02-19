import pandas as pd
import numpy as np 

# Traffic data location and opening 
filepath = 'traffic_accidents.csv'
trafficdata = pd.read_csv('traffic_accidents.csv')

# checking and removing duplicated data 
trafficdata = trafficdata.drop_duplicates()

# remove rows with missing data 
trafficdata = trafficdata.dropna()

# removing rows with any unknonw data 
toremove = []

for index, row in trafficdata.iterrows():
    if "UNKNOWN" in row.astype(str).values:  
        toremove.append(index)

trafficdata = trafficdata.drop(toremove)


print('data cleaned')
