import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os





# Download Titanic dataset if not available
current_dir = os.path.dirname(os.path.abspath(__file__))
titanic_csv_path = os.path.join(current_dir, 'titanic.csv')

try:
    # Check if the dataset exists
    if not os.path.exists(titanic_csv_path):
        print("Downloading Titanic dataset...")
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        df = pd.read_csv(url)
        df.to_csv(titanic_csv_path, index=False)
        print(f"Dataset downloaded successfully to {titanic_csv_path}!")
    else:
        print(f"Using existing dataset at {titanic_csv_path}")
        df = pd.read_csv(titanic_csv_path)
except Exception as e:
    print(f"Error downloading or loading dataset: {e}")
    exit(1)

print("Data Loaded. Starting preprocessing...")






# Basic data exploration
print(f"Dataset shape: {df.shape}")






# Data preprocessing
# Select relevant features
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
X = df[features].copy()
y = df['Survived']







# Convert categorical variables
X['Sex'] = X['Sex'].map({'male': 1, 'female': 0})







# Handle missing values
imputer = SimpleImputer(strategy='median')
X['Age'] = imputer.fit_transform(X[['Age']])








# Scale numerical features
scaler = StandardScaler()
X[['Age', 'Fare']] = scaler.fit_transform(X[['Age', 'Fare']])







# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training model...")







# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)






# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))






# Feature importance
feature_importances = pd.DataFrame({
    'feature': features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print("Feature Importance:")
print(feature_importances)







# Save model and dataset
model_path = os.path.join(current_dir, 'model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
print(f"Model saved as '{model_path}'")





# Save dataset for statistics
df.to_csv(titanic_csv_path, index=False)
print(f"Dataset saved for statistics at '{titanic_csv_path}'")

print("Complete! You can now run the web application.") 