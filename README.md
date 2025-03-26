# Forest Fire Prediction Model

## Overview
This project predicts the **Fire Weather Index (FWI)** using a machine learning model. The FWI is a critical indicator of fire danger, and this tool helps in assessing potential forest fire risks based on environmental features.

The model is built using **Ridge Regression** and deployed with a Flask web application. Users can input various environmental parameters to get a predicted FWI score.

---

## Features
### Input Parameters
The model takes the following independent features:
- **Temperature (°C)**
- **Relative Humidity (RH)**
- **Wind Speed (Ws)**
- **Rainfall (mm)**
- **Fine Fuel Moisture Code (FFMC)**
- **Duff Moisture Code (DMC)**
- **Drought Code (DC)**
- **Initial Spread Index (ISI)**
- **Buildup Index (BUI)**

### Output
The output is the **Fire Weather Index (FWI)**, which measures the likelihood and intensity of a forest fire.

---

## File Structure
- **`forest.ipynb`**: Jupyter notebook containing data preprocessing, model training, and evaluation.
- **`application.py`**: Flask application code to serve the model.
- **`index.html`**: HTML file for the web interface.
- **`ridge.pkl`**: Serialized Ridge Regression model.
- **`scaler.pkl`**: Serialized scaler for data preprocessing.
- **`Algerian_forest_fires_cleaned_dataset.csv`**: Cleaned dataset used for training the model.

---

## How to Run the Application

### Prerequisites
1. Install **Python 3.x**.
2. Install the following Python libraries:
   - Flask
   - NumPy
   - Scikit-learn
   - Pandas

### Steps to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/KrishnaChauhan7/ForestFirePrediction.git
   cd ForestFirePrediction
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate    # On Linux/Mac
   myvenv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask application:
   ```bash
   python application.py
   ```
5. Open your browser and navigate to:
   ```
http://127.0.0.1:5000/
   ```
6. Input the environmental parameters to get the FWI prediction.

---

## Dataset
- **Source**: Algerian Forest Fires Dataset
- **Description**: The dataset contains meteorological and vegetation data that impact forest fires.

---

## Future Improvements
1. Enhance the user interface for better usability.
2. Add more features like geographical data to improve prediction accuracy.
3. Deploy the model using cloud services (e.g., AWS, Azure, or Google Cloud).
4. Integrate real-time weather data for live predictions.

---

## Contributing
Feel free to fork this repository and make pull requests for improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For any questions or feedback, please contact:
- **Name**: Krishna Chauhan
- **Email**: krishna.chauhan.ug22@nsut.ac.in
- **GitHub**: [KrishnaChauhan7](https://github.com/KrishnaChauhan7)


