# Week 9 - Day 3
## Interactive Streamlit Dashboard for IMDb Sentiment Analysis

### Project Overview
This project deploys the IMDb Movie Reviews Sentiment Analysis model through an interactive Streamlit dashboard.

The application allows a non-technical user to enter a movie review and receive an immediate sentiment prediction.

The prediction pipeline is:

Review → TF-IDF Vectorizer → Logistic Regression → Sentiment Prediction → Confidence Probabilities

---

## Day 3 Objectives
The main objectives of Day 3 were to:

- Build a Streamlit application for non-technical users.
- Use an appropriate text input widget for sentiment analysis.
- Load the saved machine learning model and TF-IDF vectorizer.
- Display the predicted sentiment clearly.
- Add confidence probabilities as a supporting visualization.
- Test the application locally.
- Evaluate normal and edge-case inputs.

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Logistic Regression
- TF-IDF Vectorizer
- joblib

---

## Saved Model Artifacts

The Streamlit application reuses the trained artifacts created during Day 1:

- `model.joblib`
- `vectorizer.joblib`

The model is not retrained during deployment. The saved TF-IDF vectorizer is also reused to ensure that new reviews are transformed using the same feature space used during training.

---

## Streamlit Application

The main application file is:

`app.py`

The application includes:

- A clear page title and short description
- Movie review text input
- Analyze Sentiment button
- Positive or Negative prediction
- Prediction confidence
- Positive probability bar
- Negative probability bar
- Empty-input validation

---

## Running the Application

Open the terminal inside the Day 3 folder:

```bash
cd D:\Main_Folder_main\Week9\Day3