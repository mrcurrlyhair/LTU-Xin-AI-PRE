import pandas as pd

# traffic data location and opening 
trafficdata = pd.read_csv('traffic_accidents.csv')

# rename column
trafficdata = trafficdata.rename(columns={'num_units': 'cars_involved'})

# checking and removing duplicated data 
trafficdata = trafficdata.drop_duplicates()

# remove rows with missing data 
trafficdata = trafficdata.dropna()

# removing columns which are not needed 
trafficdata = trafficdata.drop(columns=['alignment', 'crash_date', 'crash_type', 'first_crash_type', 'damage', 'intersection_related_i'])

# removing rows with any unknown data 
toremove = []

for index, row in trafficdata.iterrows():
    if "UNKNOWN" in row.astype(str).values:  
        toremove.append(index)

trafficdata = trafficdata.drop(toremove)

print('Data cleaned')

# converting to integers 
to_integers = ['cars_involved', 'crash_day_of_week', 'injuries_total', 'injuries_incapacitating', 'injuries_non_incapacitating', 'injuries_reported_not_evident', 'injuries_no_indication', 'crash_hour', 'crash_month']

trafficdata[to_integers] = trafficdata[to_integers].astype(int)

# mapping most_severe_injury into numerical categories
injury_mapping = {'NO INDICATION OF INJURY': 0, 'REPORTED, NOT EVIDENT': 1, 'NONINCAPACITATING INJURY': 2, 'INCAPACITATING INJURY': 3, 'FATAL': 4
}

trafficdata['most_severe_injury'] = trafficdata['most_severe_injury'].map(injury_mapping)

# applying OHE to multiple columns
OHE_Columns = ['weather_condition', 'lighting_condition', 'roadway_surface_cond', 'traffic_control_device', 'trafficway_type', 'road_defect', 'prim_contributory_cause']

trafficdata = pd.get_dummies(trafficdata, columns=OHE_Columns)

print('Data prepared')

# save changes 
trafficdata.to_csv('cleaned_traffic_accidents.csv', index=False)

print('Data saved')
