from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("air_quality_model.pkl")


# Friendly messages for website users
aqi_messages = {
    "Good": "🟢 The air quality is good and safe for outdoor activities.",
    "Satisfactory": "🟡 The air quality is satisfactory with minimal health concerns.",
    "Moderately Polluted": "🟠 The air is moderately polluted. Sensitive individuals should take precautions during prolonged outdoor activities.",
    "Poor": "🔴 The air quality is poor. It is advisable to reduce prolonged outdoor activities.",
    "Very Poor": "🟣 The air quality is very poor. Limit outdoor exposure and consider wearing a mask if necessary.",
    "Severe": "⚫ The air quality is severe. Stay indoors whenever possible and follow local health advisories."
}


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    try:

        # ----------- POSTMAN (JSON) -----------
        if request.is_json:

            data = request.get_json()

            soi = float(data["SOi"])
            noi = float(data["Noi"])
            rpi = float(data["Rpi"])
            spmi = float(data["SPMi"])

        # ----------- WEBSITE (HTML FORM) -----------
        else:

            soi = float(request.form["SOi"])
            noi = float(request.form["Noi"])
            rpi = float(request.form["Rpi"])
            spmi = float(request.form["SPMi"])

        # Prepare Features
        features = np.array([[soi, noi, rpi, spmi]])

        # Predict Category
        prediction = str(model.predict(features)[0])

        # ----------- POSTMAN RESPONSE -----------
        if request.is_json:

            return jsonify({
                "Predicted AQI Category": prediction
            })

        # Friendly message for website
        message = aqi_messages.get(prediction, prediction)

        # ----------- WEBSITE RESPONSE -----------
        return render_template(
            "index.html",
            prediction=message,
            soi=soi,
            noi=noi,
            rpi=rpi,
            spmi=spmi
        )

    except Exception as e:

        if request.is_json:
            return jsonify({
                "Error": str(e)
            }), 400

        return render_template(
            "index.html",
            prediction=f"❌ Error: {e}",
            soi=request.form.get("SOi", ""),
            noi=request.form.get("Noi", ""),
            rpi=request.form.get("Rpi", ""),
            spmi=request.form.get("SPMi", "")
        )


if __name__ == "__main__":
    app.run(debug=True, port=5001)