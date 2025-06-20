from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the model (ensure the model path is correct)
model_path = '/Users/anand/Desktop/Machine Learning/11.Projects/01.Algerian_Forest_Fires/App/Model_file/scaled_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError(f"Model file not found at {model_path}")

@app.route('/')
def home():
    # Home page route that renders an HTML form
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # API route to handle prediction requests from the form
    if request.method == 'POST':
        try:
            # Extract input values from the form (make sure keys match form field names)
            temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            DC = float(request.form.get('DC'))
            ISI = float(request.form.get('ISI'))
            BUI = float(request.form.get('BUI'))

            # Prepare the data for prediction
            features = [[temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI, BUI]]

            # Make a prediction using the loaded model
            prediction = model.predict(features)

            # Render the result back to the page
            return render_template('index.html', prediction=prediction[0])

        except Exception as e:
            return jsonify({"error": str(e)})

    # If not a POST request, render the page again without prediction
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    # Route to handle the favicon.ico request, return an empty response
    return '', 204  # No content

if __name__ == '__main__':
    app.run(debug=True)
