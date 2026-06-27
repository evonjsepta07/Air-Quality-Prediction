# 🌍 Air Quality Prediction System

## 📌 Overview

The **Air Quality Prediction System** is a Machine Learning web application developed using **Python**, **Flask**, and **Scikit-learn**. It predicts the **Air Quality Index (AQI) category** based on pollutant index values entered by the user.

The application provides both:

* A user-friendly web interface for predictions.
* A REST API that can be tested using Postman.

---

## 🚀 Features

* Predicts Air Quality category using a trained Machine Learning model.
* Interactive web interface built with HTML and CSS.
* REST API support for JSON requests.
* Accepts pollutant index values as input.
* Displays user-friendly air quality messages.
* Supports browser and Postman testing.

---

## 🛠 Technologies Used

* Python
* Flask
* Scikit-learn
* NumPy
* Pandas
* Joblib
* HTML5
* CSS3
* Jupyter Notebook

---

## 📊 Machine Learning Model

### Input Features

* Sulphur Dioxide Index (SO₂)
* Nitrogen Dioxide Index (NO₂)
* Respirable Particulate Matter Index (RPI)
* Suspended Particulate Matter Index (SPMI)

### Output Categories

* Good
* Satisfactory
* Moderately Polluted
* Poor
* Very Poor
* Severe

---

## 📂 Project Structure

```
Air-Quality-Prediction/
│
├── app.py
├── air_quality_model.pkl
├── AIR_QUALITY.ipynb
├── requirements.txt
├── README.md
├── .gitignore
├── data.csv
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/evonjsepta07/Air-Quality-Prediction.git
```

Move into the project folder:

```bash
cd Air-Quality-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5001
```

---

## 📬 API Endpoint

### POST

```
/predict
```

### Example JSON Request

```json
{
    "SOi": 18,
    "Noi": 25,
    "Rpi": 40,
    "SPMi": 60
}
```

### Example Response

```json
{
    "Predicted AQI Category": "Moderately Polluted"
}
```

---

## 📈 Future Improvements

* Deploy the application online using Render or Railway.
* Add data visualizations and AQI charts.
* Improve the user interface with animations.
* Integrate live air quality data from public APIs.

---

## 👨‍💻 Author

**Evon J Septa**

B.Tech Computer Science Engineering Student

Machine Learning & Python Enthusiast
