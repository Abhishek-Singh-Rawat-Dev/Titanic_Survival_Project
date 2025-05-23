# Titanic Survival Prediction

A full-stack machine learning web application that predicts whether a passenger on the Titanic would have survived based on their characteristics. The application also provides statistical insights comparing survival rates between men, women, and children.

## Features

- Interactive web form to input passenger details
- Real-time prediction of survival probability
- Statistical visualizations showing survival rates by gender, age group, and passenger class
- Responsive design that works on desktop and mobile devices

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn, pandas, numpy

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository or download the project files

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. First, train the machine learning model:
   ```
   cd model
   python train.py
   cd ..
   ```

2. Start the Flask web server:
   ```
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Fill in the passenger details form with the following information:
   - Passenger Class (1st, 2nd, or 3rd)
   - Gender (Male or Female)
   - Age
   - Number of Siblings/Spouses Aboard
   - Number of Parents/Children Aboard
   - Fare paid for the ticket

2. Click the "Predict Survival" button to see the prediction result

3. View the statistics section to understand survival patterns across different demographic groups

## Project Structure

- `app.py`: Main Flask application
- `model/train.py`: Script to train the machine learning model
- `model/model.pkl`: Saved trained model
- `model/titanic.csv`: Titanic dataset
- `templates/index.html`: Main HTML template
- `static/css/style.css`: CSS styling
- `static/js/script.js`: Frontend JavaScript #   W e b _ C r a w l e r  
 