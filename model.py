import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB





#                                                       SPLITTING AND SCALING
# clean traffic data location and opening
clean_traffic_data = pd.read_csv("cleaned_traffic_accidents.csv")

# define features and target variable
X = clean_traffic_data.drop(columns=["injuries_fatal"])
y = clean_traffic_data["injuries_fatal"]

# split into 80% training and 20% testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# integer columns not OHE  
numeric_features = ["cars_involved", "injuries_total", "crash_hour", "crash_day_of_week"]

# scaler 
scaler = StandardScaler()

# fit and transform only the numeric features
X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])
X_test[numeric_features] = scaler.transform(X_test[numeric_features])



#                                                       RANDOM FORREST 
# Initialize the model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions
rf_preds = rf_model.predict(X_test)

# Evaluate the model
print("Random Forest Model Performance:")
print(classification_report(y_test, rf_preds))
print("Accuracy:", accuracy_score(y_test, rf_preds))


