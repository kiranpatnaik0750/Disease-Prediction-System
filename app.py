from flask import Flask, render_template, request
import numpy as np
import joblib
from risk_level import detect_risk
from medical_advice import get_advice

app = Flask(__name__)

# Load trained model and label encoder
model = joblib.load("best_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Symptoms used in dataset
symptoms = [
    "high_fever","chills","sweating","headache",
    "joint_pain","muscle_pain","cough","nausea",
    "vomiting","abdominal_pain","fatigue","dehydration"
]


@app.route("/")
def home():
    return render_template("index.html", symptoms=symptoms)


@app.route("/predict", methods=["POST"])
def predict():

    values = []
    selected = []

    for s in symptoms:
        if s in request.form:
            values.append(1)
            selected.append(s.replace("_"," "))
        else:
            values.append(0)

    sample = np.array(values).reshape(1,-1)

    # Predict disease
    prediction = model.predict(sample)[0]
    disease = label_encoder.inverse_transform([prediction])[0]

    # Prediction probability
    probabilities = model.predict_proba(sample)[0]
    confidence = round(max(probabilities) * 100, 2)

    # Risk level
    risk = detect_risk(values)

    # Medical advice
    advice = get_advice(disease)

    # ---------- Top 3 diseases ----------
    classes = label_encoder.classes_
    top3_index = probabilities.argsort()[-3:][::-1]

    top3 = []
    for i in top3_index:
        top3.append((classes[i], round(probabilities[i]*100,2)))

    # ---------- Alert logic ----------
    alert_message = None

    if risk == "HIGH":
        alert_message = "⚠ HIGH RISK ALERT: Please consult a doctor immediately."

    elif risk == "MEDIUM":
        alert_message = "⚠ Warning: Symptoms indicate moderate risk."

    print("\n========= PREDICTION ANALYSIS =========")
    print("Symptoms:", selected)
    print("Prediction:", disease)
    print("Confidence:", confidence)
    print("Risk:", risk)
    print("Top3:", top3)
    print("=======================================\n")

    return render_template(
        "result.html",
        disease=disease,
        confidence=confidence,
        risk=risk,
        symptoms=selected,
        advice=advice,
        alert_message=alert_message,
        top3=top3
    )


if __name__ == "__main__":
    app.run(debug=True)