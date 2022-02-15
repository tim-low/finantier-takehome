import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, render_template

# from pytorch_tabnet.tab_model import TabNetClassifier, TabNetRegressor


# Load ML model
model = pickle.load(open("data/model.pkl", "rb"))


# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route("/")
def home():
    return render_template("index.html")


# Bind predict function to URL
@app.route("/predict", methods=["POST"])
def predict():
    # Put all form entries values in a list
    print(request.form.values())
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]

    output = model.predict(array_features)

    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template("index.html", result="Prediction = 1: The customer is likely to default!")
    else:
        return render_template("index.html", result="Prediction = 0: The customer is not likely to default.")


if __name__ == "__main__":
    # Run the application
    app.run(host="0.0.0.0", port=5000)
