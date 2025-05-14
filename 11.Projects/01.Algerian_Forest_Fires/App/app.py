from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the model (ensure the model path is correct)
model_path = '/Users/anand/Desktop/Machine Learning/11.Projects/01.Algerian_Forest_Fires/App/Model_file/final_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError(f"Model file not found at {model_path}")

@app.route('/')
def home():
    # Home page route that renders an HTML form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # API route to handle prediction requests from the form
    # Extract input values from the form
    temperature = float(request.form['Temperature'])
    RH = float(request.form['RH'])
    Ws = float(request.form['Ws'])
    Rain = float(request.form['Rain'])
    FFMC = float(request.form['FFMC'])
    DMC = float(request.form['DMC'])
    DC = float(request.form['DC'])
    ISI = float(request.form['ISI'])
    BUI = float(request.form['BUI'])

    # Prepare the data for prediction
    features = [[temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI, BUI]]

    # Make a prediction using the loaded model
    prediction = model.predict(features)

    # Return the prediction result as a rendered page
    return render_template('index.html', prediction=prediction[0])

@app.route('/favicon.ico')
def favicon():
    # Route to handle the favicon.ico request, return an empty response
    return '', 204  # No content

if __name__ == '__main__':
    app.run(debug=True)
