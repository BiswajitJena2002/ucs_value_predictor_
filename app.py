from flask import Flask, request, render_template
import numpy as np
import joblib

# Flask app
app = Flask(__name__)

# Load the pre-trained model and the fitted scaler
loaded_model = joblib.load('UCS_gb.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        harha = float(request.form['harha'])
        ll = float(request.form['ll'])
        pl = float(request.form['pl'])
        pi = float(request.form['pi'])
        omc = float(request.form['omc'])
        ca = float(request.form['ca'])
        mdd = float(request.form['mdd'])

        # Organize the input features as a numpy array
        features = np.array([[harha, ll, pl,pi,omc,ca,mdd]])

        # Scale the input data using the fitted scaler
        scaled_test_data = scaler.transform(features)

        # Make prediction using the pre-trained model
        prediction = loaded_model.predict(scaled_test_data)

        return render_template('index.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)