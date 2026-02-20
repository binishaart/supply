from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Mock function to simulate anomaly prediction
def predict_anomaly(shipment_info):
    # In real app, you would integrate AI/ML model here
    anomalies = ["No anomaly", "Delay predicted", "Reroute recommended", "High risk"]
    return random.choice(anomalies)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    shipment_info = data.get('shipment', {})
    result = predict_anomaly(shipment_info)
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
