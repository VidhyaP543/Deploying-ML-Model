from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    print("Model loaded successfully!")
except FileNotFoundError:
    model = None
    print("Error: model.pkl not found.")

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Iris Flower Prediction API!",
        "status": "API is running successfully."
    })

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not found. Please train and save the model first."}), 500

    try:
        data = request.get_json()

        # Extract input values
        sepal_length = float(data["sepal_length"])
        sepal_width = float(data["sepal_width"])
        petal_length = float(data["petal_length"])
        petal_width = float(data["petal_width"])

        # Prepare input for prediction
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Predict
        prediction = model.predict(features)[0]

        # Convert prediction to flower name
        classes = {
            0: "Setosa",
            1: "Versicolor",
            2: "Virginica"
        }

        result = classes.get(prediction, "Unknown")

        return jsonify({
            "prediction": result,
            "input": {
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width
            }
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
