
from pathlib import Path
import re
import html
import joblib
import nltk

from fastapi import FastAPI
from pydantic import BaseModel, Field

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag


# --------------------------------------------------
# Load Day 1 artifacts
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DAY1_DIR = BASE_DIR.parent / "Day1"

MODEL_PATH = DAY1_DIR / "model.joblib"
VECTORIZER_PATH = DAY1_DIR / "vectorizer.joblib"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# --------------------------------------------------
# Reuse the exact training preprocessing
# --------------------------------------------------

resources = [
    "punkt",
    "punkt_tab",
    "stopwords",
    "wordnet",
    "omw-1.4",
    "averaged_perceptron_tagger_eng"
]

for resource in resources:
    nltk.download(resource, quiet=True)

negation_words = {"not", "no", "nor"}

stop_words = set(stopwords.words("english")) - negation_words

lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(tag):

    if tag.startswith("J"):
        return wordnet.ADJ

    elif tag.startswith("V"):
        return wordnet.VERB

    elif tag.startswith("N"):
        return wordnet.NOUN

    elif tag.startswith("R"):
        return wordnet.ADV

    return wordnet.NOUN


def preprocess_review(text):

    text = html.unescape(str(text))

    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    text = re.sub(
        r"n['’]t\b",
        " not",
        text
    )

    text = text.lower()

    text = re.sub(
        r"\d+",
        " ",
        text
    )

    text = re.sub(
        r"[^\w\s']",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    tokens = word_tokenize(text)

    tokens = [
        token
        for token in tokens
        if token not in stop_words
        and len(token) > 1
    ]

    tagged_tokens = pos_tag(tokens)

    lemmas = [
        lemmatizer.lemmatize(
            word,
            get_wordnet_pos(tag)
        )
        for word, tag in tagged_tokens
    ]

    lemmas = [
        word
        for word in lemmas
        if not word.startswith("'")
    ]

    return " ".join(lemmas)


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="IMDb Sentiment API",
    description="Predicts whether a movie review is Positive or Negative.",
    version="1.0.0"
)


# --------------------------------------------------
# Pydantic input schema
# --------------------------------------------------

class ReviewInput(BaseModel):

    review: str = Field(
        ...,
        min_length=3,
        max_length=5000
    )


# --------------------------------------------------
# Health endpoint
# --------------------------------------------------

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "model": type(model).__name__
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict_sentiment(data: ReviewInput):

    cleaned_review = preprocess_review(
        data.review
    )

    review_vector = vectorizer.transform(
        [cleaned_review]
    )

    prediction = model.predict(
        review_vector
    )[0]

    probabilities = model.predict_proba(
        review_vector
    )[0]

    sentiment = (
        "Positive"
        if prediction == 1
        else "Negative"
    )

    confidence = float(
        probabilities.max()
    )

    return {
        "review": data.review,
        "prediction": sentiment,
        "confidence": round(
            confidence,
            4
        )
    }
