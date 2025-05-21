from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import os
import numpy as np
import traceback

app = Flask(__name__)

# Get absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load model with proper error handling
model_path = os.path.join(current_dir, 'model', 'model.pkl')
model = None
try:
    if os.path.exists(model_path):
        print(f"Loading model from {model_path}")
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print("Model loaded successfully")
    else:
        print(f"Warning: Model file not found at {model_path}")
except Exception as e:
    print(f"Error loading model: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not trained yet or failed to load'}), 400

    try:
        # Get form data
        age = float(request.form.get('age', 0))
        sex = request.form.get('sex', 'male')
        pclass = int(request.form.get('pclass', 3))
        fare = float(request.form.get('fare', 0))
        sibsp = int(request.form.get('sibsp', 0))
        parch = int(request.form.get('parch', 0))
        
        # Create a dataframe with the input data
        input_data = pd.DataFrame({
            'Pclass': [pclass],
            'Sex': [1 if sex == 'male' else 0],
            'Age': [age],
            'SibSp': [sibsp],
            'Parch': [parch],
            'Fare': [fare]
        })
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        result = {
            'prediction': int(prediction),
            'probability': float(probability),
            'survival_status': 'Survived' if prediction == 1 else 'Did not survive'
        }
        
        return jsonify(result)
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 400

@app.route('/stats')
def stats():
    # Read the dataset
    try:
        dataset_path = os.path.join(current_dir, 'model', 'titanic.csv')
        print(f"Loading dataset from {dataset_path}")
        
        if not os.path.exists(dataset_path):
            return jsonify({'error': f'Dataset not found at {dataset_path}'}), 404
            
        df = pd.read_csv(dataset_path)
        print(f"Dataset loaded successfully with {len(df)} records")
        
        # Calculate survival statistics
        total_passengers = len(df)
        survivors = df[df['Survived'] == 1].shape[0]
        survival_rate = survivors / total_passengers * 100
        
        # By gender
        male_survival = df[df['Sex'] == 'male']['Survived'].mean() * 100
        female_survival = df[df['Sex'] == 'female']['Survived'].mean() * 100
        
        # By class
        class1_survival = df[df['Pclass'] == 1]['Survived'].mean() * 100
        class2_survival = df[df['Pclass'] == 2]['Survived'].mean() * 100
        class3_survival = df[df['Pclass'] == 3]['Survived'].mean() * 100
        
        # By age group
        df['AgeGroup'] = pd.cut(df['Age'], [0, 12, 60, 100], labels=['Child', 'Adult', 'Elderly'])
        children_survival = df[df['AgeGroup'] == 'Child']['Survived'].mean() * 100
        adult_survival = df[df['AgeGroup'] == 'Adult']['Survived'].mean() * 100
        elderly_survival = df[df['AgeGroup'] == 'Elderly']['Survived'].mean() * 100
        
        stats = {
            'total_passengers': total_passengers,
            'survivors': survivors,
            'survival_rate': survival_rate,
            'male_survival': male_survival,
            'female_survival': female_survival,
            'class1_survival': class1_survival,
            'class2_survival': class2_survival,
            'class3_survival': class3_survival,
            'children_survival': children_survival,
            'adult_survival': adult_survival,
            'elderly_survival': elderly_survival
        }
        
        return jsonify(stats)
    except Exception as e:
        print(f"Statistics error: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)