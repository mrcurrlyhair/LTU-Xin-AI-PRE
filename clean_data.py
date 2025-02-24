import pandas as pd
import numpy as np 

# Traffic data location and opening 
filepath = 'traffic_accidents.csv'
trafficdata = pd.read_csv('traffic_accidents.csv')

# checking and removing duplicated data 
trafficdata = trafficdata.drop_duplicates()

# remove rows with missing data 
trafficdata = trafficdata.dropna()

# removing columns whihc are not needed 
trafficdata = trafficdata.drop(columns=['crash_day_of_week'])

# removing rows with any unknown data 
toremove = []

for index, row in trafficdata.iterrows():
    if "UNKNOWN" in row.astype(str).values:  
        toremove.append(index)

trafficdata = trafficdata.drop(toremove)

print('data cleaned')

# OHE applied to weather condtion 
trafficdata = pd.get_dummies(trafficdata, columns=['weather_condition'])

#save changes 
trafficdata.to_csv("cleaned_traffic_accidents.csv", index=False)


print('data prepared ')

#save changes 
trafficdata.to_csv("cleaned_traffic_accidents.csv", index=False)

print('data saved')
