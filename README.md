# UCS Value Predictor 

## Overview

This project implements a machine learning model to predict the Unconfined Compressive Strength (UCS) of stabilized expansive clay soil based on various input features. The model is trained using machine learning techniques, and the Flask web application allows users to input soil composition data and obtain predictions for the UCS using the pre-trained model.

## Live Demo

Check out the live demo of the deployed application: [UCS Value Predictor](https://your-app-url-here)
![Screenshot (446)](https://github.com/BiswajitJena2002/ucs_value_predictor_/assets/121337717/1f84d1e3-165a-4094-b8ce-f8adb7dc47e0)

## Files

- `model_gf.joblib`: Pre-trained machine learning model for UCS prediction.
- `scaler.joblib`: Fitted scaler used for data normalization.
- `app.py`: Flask web application that enables users to input soil composition data and receive UCS predictions.

## Getting Started

### Prerequisites

Make sure you have the following dependencies installed:

- Python (version 3.6 or higher)
- Flask
- NumPy
- scikit-learn

Install the required Python packages using:

```bash
pip install flask numpy scikit-learn
```





Clone the repository:
bash
```
git clone https://github.com/your-username/your-repo.git
```
bash
```
cd your-repo
```
Run the Flask app:
bash
```
python app.py
```
Open your web browser and go to http://localhost:5000.

Fill in the input form with the required soil composition details:

Harha (%)
LL (%)
PL (%)
PI (%)
OMC (%)
CA (%)
MDD (g/cm³)
Click the "Predict" button to get the predicted UCS value.
