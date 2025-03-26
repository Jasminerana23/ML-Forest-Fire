# Forest Fire Prediction Model

## Overview
This project predicts the **Fire Weather Index (FWI)** using a machine learning model. The FWI is a critical indicator of fire danger, and this tool helps in assessing potential forest fire risks based on environmental features.

The model is built using **Ridge Regression** and deployed with a Flask web application. Users can input various environmental parameters to get a predicted FWI score.

---

## Features

### Input Parameters
The model takes the following independent features:
- **Temperature (\u00b0C)**
- **Relative Humidity (RH)**
- **Wind Speed (Ws)**
- **Rain (mm)**
- **Fine Fuel Moisture Code (FFMC)**
- **Duff Moisture Code (DMC)**
- **Drought Code (DC)**
- **Initial Spread Index (ISI)**
- **Buildup Index (BUI)**

### Output
- **Fire Weather Index (FWI):** A numerical value that indicates the fire danger level.

---

## How to Run the Application

### Prerequisites
1. Install **Python 3.8 or higher**.
2. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/KrishnaChauhan7/ForestFirePrediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ForestFirePrediction
   ```
3. Run the Flask application:
   ```bash
   python application.py
   ```
4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Folder Structure
- **`application.py`**: Flask app handling user input and model predictions.
- **`index.html`**: Frontend HTML template for the web interface.
- **`forest.ipynb`**: Jupyter Notebook for building and training the model.
- **`ridge.pkl`**: Pickle file containing the trained Ridge Regression model.
- **`scaler.pkl`**: Pickle file for the feature scaler used during preprocessing.
- **`Algerian_forest_fires_cleaned_dataset.csv`**: Dataset used to train and evaluate the model.
- **`requirements.txt`**: List of Python packages required to run the application.

---

## Example
To predict the Fire Weather Index:
1. Input the values for **Temperature**, **Relative Humidity**, **Wind Speed**, and other features in the web application.
2. Click **Predict**.
3. The predicted **Fire Weather Index (FWI)** will be displayed on the screen.

---

## Author
- **Krishna Chauhan**  
  Email: krishna.chauhan.ug22@nsut.ac.in  
  GitHub: [KrishnaChauhan7](https://github.com/KrishnaChauhan7)

---

## License
This project is licensed under the MIT License.



