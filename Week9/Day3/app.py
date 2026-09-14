import streamlit as st
import joblib
from pathlib import Path

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="IMDb Sentiment Analyzer",
    page_icon="🎬",
    layout="centered"
)

# =========================
# PATHS
# =========================
CURRENT_DIR = Path(__file__).resolve().parent

MODEL_PATH = CURRENT_DIR.parent / "Day1" / "model.joblib"
VECTORIZER_PATH = CURRENT_DIR.parent / "Day1" / "vectorizer.joblib"

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

model, vectorizer = load_artifacts()

# =========================
# TITLE
# =========================
st.title("🎬 IMDb Sentiment Analyzer")

st.write(
    "Enter a movie review and let the model predict "
    "whether the sentiment is Positive or Negative."
)

# =========================
# INPUT
# =========================
review = st.text_area(
    "Movie Review",
    height=180,
    placeholder="Example: This movie was amazing and beautifully acted..."
)

# =========================
# PREDICTION
# =========================
if st.button("Analyze Sentiment", use_container_width=True):

    if review.strip() == "":
        st.warning("Please enter a movie review first.")

    else:
        review_vector = vectorizer.transform([review])

        prediction = model.predict(review_vector)[0]

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(review_vector)[0]
            confidence = max(probabilities)
        else:
            confidence = None

        if prediction == 1:
            st.success("😊 Positive Sentiment")

        else:
            st.error("😕 Negative Sentiment")

        if confidence is not None:
            st.write(f"Confidence: {confidence * 100:.2f}%")

        # Probability bars
        if hasattr(model, "predict_proba"):
            classes = list(model.classes_)

            if 0 in classes and 1 in classes:
                negative_prob = probabilities[classes.index(0)]
                positive_prob = probabilities[classes.index(1)]

                st.subheader("Prediction Probabilities")

                st.write(f"Positive: {positive_prob * 100:.2f}%")
                st.progress(float(positive_prob))

                st.write(f"Negative: {negative_prob * 100:.2f}%")
                st.progress(float(negative_prob))

# =========================
# FOOTER
# =========================
st.divider()
st.caption("IMDb Sentiment Analysis • TF-IDF + Logistic Regression")