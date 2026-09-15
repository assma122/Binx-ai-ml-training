import html
import re
from pathlib import Path

import joblib
import nltk
import streamlit as st
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


st.set_page_config(
    page_title="IMDb Sentiment Analyzer",
    page_icon="🎬",
    layout="centered",
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"
VECTORIZER_PATH = BASE_DIR / "vectorizer.joblib"


@st.cache_resource(show_spinner="Preparing the language resources...")
def prepare_nlp_resources():
    resources = {
        "tokenizers/punkt": "punkt",
        "tokenizers/punkt_tab": "punkt_tab",
        "corpora/stopwords": "stopwords",
        "corpora/wordnet": "wordnet",
        "corpora/omw-1.4": "omw-1.4",
        "taggers/averaged_perceptron_tagger_eng": "averaged_perceptron_tagger_eng",
    }

    for resource_path, download_name in resources.items():
        available = False
        for candidate in (resource_path, f"{resource_path}.zip"):
            try:
                nltk.data.find(candidate)
                available = True
                break
            except LookupError:
                continue

        if not available:
            nltk.download(download_name, quiet=True)

            try:
                nltk.data.find(resource_path)
            except LookupError:
                try:
                    nltk.data.find(f"{resource_path}.zip")
                except LookupError as error:
                    raise RuntimeError(
                        f"Unable to prepare the NLTK resource: {download_name}"
                    ) from error

    negation_words = {"not", "no", "nor"}
    stop_words = set(stopwords.words("english")) - negation_words
    lemmatizer = WordNetLemmatizer()
    return stop_words, lemmatizer


@st.cache_resource(show_spinner="Loading the sentiment model...")
def load_artifacts():
    if not MODEL_PATH.exists() or not VECTORIZER_PATH.exists():
        raise FileNotFoundError(
            "model.joblib and vectorizer.joblib must be stored beside app.py."
        )

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer


stop_words, lemmatizer = prepare_nlp_resources()
model, vectorizer = load_artifacts()


def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    if tag.startswith("V"):
        return wordnet.VERB
    if tag.startswith("N"):
        return wordnet.NOUN
    if tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN


def preprocess_review(text):
    """Reuse the exact text preprocessing applied during model training."""
    text = html.unescape(str(text))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"n['’]t\b", " not", text)
    text = text.lower()
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"[^\w\s']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = word_tokenize(text)
    tokens = [
        token
        for token in tokens
        if token not in stop_words and len(token) > 1
    ]
    tagged_tokens = pos_tag(tokens)
    lemmas = [
        lemmatizer.lemmatize(word, get_wordnet_pos(tag))
        for word, tag in tagged_tokens
    ]
    lemmas = [word for word in lemmas if not word.startswith("'")]
    return " ".join(lemmas)


def predict_sentiment(review):
    cleaned_review = preprocess_review(review)
    review_vector = vectorizer.transform([cleaned_review])
    prediction = model.predict(review_vector)[0]
    probabilities = model.predict_proba(review_vector)[0]
    classes = list(model.classes_)

    negative_probability = float(probabilities[classes.index(0)])
    positive_probability = float(probabilities[classes.index(1)])
    sentiment = "Positive" if prediction == 1 else "Negative"
    confidence = max(negative_probability, positive_probability)

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "positive_probability": positive_probability,
        "negative_probability": negative_probability,
        "cleaned_review": cleaned_review,
    }


st.title("🎬 IMDb Sentiment Analyzer")
st.write(
    "Enter an English movie review and let the TF-IDF + Logistic Regression "
    "model predict whether its sentiment is positive or negative."
)

example_reviews = {
    "Write my own review": "",
    "Positive example": (
        "This movie was absolutely amazing, beautifully acted, and worth watching."
    ),
    "Negative example": (
        "The story was boring, the acting was terrible, and I regret watching it."
    ),
}

selected_example = st.selectbox("Quick example", list(example_reviews))
review = st.text_area(
    "Movie Review",
    value=example_reviews[selected_example],
    height=180,
    max_chars=5000,
    placeholder="Example: This movie was amazing and beautifully acted...",
)

if st.button("Analyze Sentiment", type="primary", use_container_width=True):
    if len(review.strip()) < 3:
        st.warning("Please enter a movie review with at least 3 characters.")
    else:
        result = predict_sentiment(review)

        if result["sentiment"] == "Positive":
            st.success("😊 Positive Sentiment")
        else:
            st.error("😕 Negative Sentiment")

        st.metric("Model Confidence", f'{result["confidence"] * 100:.2f}%')

        st.subheader("Prediction Probabilities")
        st.write(f'Positive: {result["positive_probability"] * 100:.2f}%')
        st.progress(result["positive_probability"])
        st.write(f'Negative: {result["negative_probability"] * 100:.2f}%')
        st.progress(result["negative_probability"])

        with st.expander("View the processed text"):
            st.code(result["cleaned_review"] or "No tokens remained after preprocessing.")

st.divider()
st.caption("IMDb Sentiment Analysis • TF-IDF + Logistic Regression")
