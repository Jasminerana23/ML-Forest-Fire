from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import os

# Initialize Flask app
app = Flask(__name__)

# Load the models (ridge regression model and scaler)
model_path = os.path.join("C:\\Users\\hp\\OneDrive\\Desktop\\ML\\LRProject", "ridge.pkl")
scaler_path = os.path.join("C:\\Users\\hp\\OneDrive\\Desktop\\ML\\LRProject", "scaler.pkl")

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(scaler_path, 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')  # You need to create an index.html file for the UI

# Define a prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data (independent features)
        data = request.form
        features = [
            float(data['Temperature']),
            float(data['RH']),
            float(data['Ws']),
            float(data['Rain']),
            float(data['FFMC']),
            float(data['DMC']),
            float(data['DC']),
            float(data['ISI']),
            float(data['BUI'])
        ]

        # Preprocess the data
        features_scaled = scaler.transform([features])

        # Make prediction
        fwi_prediction = model.predict(features_scaled)[0]

        # Return the result
        return render_template('index.html', prediction=f"Predicted Fire Weather Index (FWI): {fwi_prediction:.2f}")

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
