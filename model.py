import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE

# SPLITTING AND SCALING

# clean traffic data location and opening 
clean_traffic_data = pd.read_csv('cleaned_traffic_accidents.csv')

# define features 
x = clean_traffic_data.drop(columns=['most_severe_injury', 'injuries_total', 'injuries_incapacitating', 'injuries_non_incapacitating', 'injuries_reported_not_evident', 'injuries_no_indication'])

y = clean_traffic_data['most_severe_injury']

# split into 80% training and 20% testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=28, stratify=y)

# integer columns NOT OHE
intcolumns = ['cars_involved', 'crash_hour', 'crash_day_of_week']  

# scaler
scaler = StandardScaler()

# fit and transform only for integers 
x_train[intcolumns] = scaler.fit_transform(x_train[intcolumns])
x_test[intcolumns] = scaler.transform(x_test[intcolumns])

# SMOTE

# using SMOTE to balance the data
smote = SMOTE(sampling_strategy='not majority', random_state=28)
X_train_balanced, y_train_balanced = smote.fit_resample(x_train, y_train)

# print class distribution after SMOTE
print("Original Class Distribution:", y_train.value_counts())
print("New Class Distribution:", y_train_balanced.value_counts())

# TRAIN & TEST RANDOM FOREST 

# using Random Forest model 
rf_model = RandomForestClassifier(
    n_estimators=500,  
    random_state=28,
    max_depth=30,  
    min_samples_split=5,  
    min_samples_leaf=10,  
)

# Train the model using SMOTE data
rf_model.fit(X_train_balanced, y_train_balanced)

# Make predictions
rf_prediction = rf_model.predict(x_test)

# test the model
print('Random Forest Model Performance:')
print(classification_report(y_test, rf_prediction))
print('Accuracy:', accuracy_score(y_test, rf_prediction))

# Matrix
conf_matrix = confusion_matrix(y_test, rf_prediction)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['No Injury', 'Reported, Not Evident', 'Non-Incapacitating', 'Incapacitating', 'Fatal'], yticklabels=['No Injury', 'Reported, Not Evident', 'Non-Incapacitating', 'Incapacitating', 'Fatal'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
