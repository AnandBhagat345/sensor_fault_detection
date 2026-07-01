# 🚀 Sensor Fault Detection using Machine Learning

> **An end-to-end Machine Learning pipeline that predicts wafer sensor faults using Flask, MongoDB, Scikit-learn, and a modular production-style architecture.**

---

## 📌 Overview

Modern semiconductor manufacturing generates thousands of sensor readings during wafer production. Faulty wafers can lead to production losses and quality issues.

This project automates wafer quality prediction by training multiple machine learning models on historical sensor data and serving predictions through a Flask web application.

The application allows users to:

- Upload wafer sensor CSV files
- Predict whether each sensor record is **Good** or **Bad**
- View predictions on the web interface
- Download prediction results as CSV
- Retrain the model through a dedicated training endpoint

---

# ✨ Features

- End-to-End ML Pipeline
- Flask Web Application
- MongoDB Data Source
- Modular Architecture
- Data Ingestion
- Data Transformation
- Multiple Model Training
- Hyperparameter Tuning
- Model Serialization
- Prediction Pipeline
- CSV Upload & Download
- Custom Logging
- Custom Exception Handling

---

# 🏗️ Architecture

```text
                 MongoDB
                    │
                    ▼
          Data Ingestion
                    │
                    ▼
        Data Transformation
                    │
                    ▼
         Feature Engineering
                    │
                    ▼
      Train Multiple ML Models
                    │
                    ▼
      Select Best Performing Model
                    │
                    ▼
      Save model.pkl & preprocessor.pkl
                    │
────────────────────────────────────────
                    │
                    ▼
               Flask Web App
                    │
            Upload Sensor CSV
                    │
                    ▼
          Prediction Pipeline
                    │
     Load Preprocessor + Model
                    │
                    ▼
         Good / Bad Prediction
                    │
         Display + Download CSV
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Backend | Flask |
| Machine Learning | Scikit-learn, XGBoost |
| Database | MongoDB |
| Data Processing | Pandas, NumPy |
| Model Storage | Pickle / Dill |
| Frontend | HTML, CSS, Jinja2 |
| Configuration | YAML |
| Logging | Python Logging |

---

# 📂 Project Structure

```text
sensor_fault_detection/
│
├── app.py
├── requirements.txt
├── setup.py
├── config/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── utils/
│   ├── logger.py
│   ├── exception.py
│   └── constant/
├── templates/
├── static/
├── artifacts/
├── prediction/
└── prediction_artifact/
```

---

# 🔄 Training Workflow

1. Read wafer data from MongoDB.
2. Save raw dataset into artifacts.
3. Clean missing values.
4. Transform features.
5. Split train/test.
6. Train multiple ML models.
7. Tune best model using GridSearchCV.
8. Save trained model and preprocessor.

---

# 🔮 Prediction Workflow

1. User uploads CSV.
2. Flask receives file.
3. Prediction pipeline stores uploaded CSV.
4. Load trained preprocessor.
5. Transform input features.
6. Load trained model.
7. Predict Good/Bad.
8. Display results.
9. Download prediction CSV.

---

# 🌐 API Routes

| Route | Method | Description |
|------|------|-------------|
| / | GET | Home |
| /train | GET | Train ML Pipeline |
| /predict | GET/POST | Upload CSV & Predict |
| /download | GET | Download prediction CSV |

---

# 📸 Screenshots

Add screenshots here:

- Upload Page
- Prediction Result
- Downloaded CSV

---

# ▶️ Installation

```bash
git clone https://github.com/your-username/sensor_fault_detection.git

cd sensor_fault_detection

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000/predict
```

---

# 📄 Input Format

Upload a wafer sensor CSV containing the same sensor feature columns used during training.

Example:

```
Sensor-1
Sensor-2
Sensor-3
...
Sensor-n
```

---

# 📤 Output

The application appends a **quality** column:

| Sensor | Quality |
|--------|---------|
| Sensor 1 | Good |
| Sensor 2 | Bad |

---

# 🧠 Machine Learning Models

- XGBoost Classifier
- Gradient Boosting
- Random Forest
- Support Vector Classifier

The best-performing model is selected automatically and optimized using GridSearchCV.

---

# 💼 Skills Demonstrated

- Machine Learning
- Data Preprocessing
- Model Selection
- Hyperparameter Tuning
- Flask Backend Development
- MongoDB Integration
- Modular Project Structure
- Exception Handling
- Logging
- Production-style ML Pipeline

---

# 🚀 Future Improvements

- Docker Deployment
- CI/CD with GitHub Actions
- MLflow Experiment Tracking
- Model Versioning
- REST API
- Authentication
- Dashboard with Charts
- Cloud Deployment

---

# 🎤 Interview Summary

> Built an end-to-end machine learning system that predicts wafer sensor faults. The project follows a modular architecture separating data ingestion, preprocessing, model training, and prediction. Historical data is fetched from MongoDB, transformed, and used to train multiple classification models. The best model is selected using GridSearchCV and persisted. Users can upload sensor CSV files through a Flask interface to receive Good/Bad predictions, visualize results, and download the output.

---

# 👨‍💻 Author

**Anand Bhagat**

B.Tech CSE (AI & ML)

Python Backend & Machine Learning Developer
