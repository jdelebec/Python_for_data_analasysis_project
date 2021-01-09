import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open("final_model.pickle", "rb"))
scaler = pickle.load(open('scaler.pickle', 'rb'))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def funct_prediction():
    response = "Non"
    features = [float(x) for x in request.form.values()]
    features = np.array(features)
    features = np.reshape(features, (-1, 1))
    features = np.transpose(features)
    features = scaler.transform(features)
    prediction = model.predict(features)
    if prediction == 1:
        response = "Oui"
    return render_template("index.html", prediction_text="Est-ce que la molécule est biodégradable?  {}".format(response))


if __name__ == "__main__":
    app.run(debug=True)
