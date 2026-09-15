# IMDb Sentiment Analyzer

A public Streamlit Community Cloud demo for an IMDb sentiment classification
model built with TF-IDF and Logistic Regression.

## Application flow

`Movie review → preprocessing → TF-IDF → Logistic Regression → sentiment + confidence`

## Deployment files

- `app.py` — Streamlit interface, preprocessing, and prediction logic.
- `model.joblib` — trained Logistic Regression model.
- `vectorizer.joblib` — fitted TF-IDF vectorizer.
- `requirements.txt` — pinned Python dependencies.

## Local run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Public URL

Add the live Streamlit Community Cloud URL here after the deployment succeeds.

`PUBLIC_URL: pending deployment`

## Validation checklist

- The model and vectorizer load from relative paths.
- The same preprocessing used during training is applied at inference time.
- Positive, negative, short, empty, and symbol-heavy inputs are tested.
- Live predictions are compared with local predictions.
