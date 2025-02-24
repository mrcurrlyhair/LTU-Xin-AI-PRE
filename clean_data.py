import pandas as pd

# Traffic data location and opening 
trafficdata = pd.read_csv('traffic_accidents.csv')

# checking and removing duplicated data 
trafficdata = trafficdata.drop_duplicates()

# remove rows with missing data 
trafficdata = trafficdata.dropna()

# removing columns whihc are not needed 
trafficdata = trafficdata.drop(columns=['alignment', 'crash_date', 'crash_type', 'first_crash_type', 'damage', 'intersection_related_i'])

# removing rows with any unknown data 
toremove = []

for index, row in trafficdata.iterrows():
    if "UNKNOWN" in row.astype(str).values:  
        toremove.append(index)

trafficdata = trafficdata.drop(toremove)

print('data cleaned')

# converting to integers 
to_integers = ['num_units', 'crash_day_of_week', 'injuries_total', 'injuries_fatal', 'injuries_incapacitating', 'injuries_non_incapacitating', 'injuries_reported_not_evident', 'injuries_no_indication', 'crash_hour', 'crash_month']

trafficdata[to_integers] = trafficdata[to_integers].astype(int)

# applying OHE to multiple columns 
OHE_Columns = ['weather_condition', 'lighting_condition', 'roadway_surface_cond', 'traffic_control_device', 'trafficway_type', 'road_defect', 'prim_contributory_cause']

trafficdata = pd.get_dummies(trafficdata, columns=OHE_Columns)

print('data prepared')

#save changes 
trafficdata.to_csv("cleaned_traffic_accidents.csv", index=False)

print('data saved')
