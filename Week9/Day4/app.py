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
    page_title="CineSense | Sentiment Intelligence",
    page_icon="◐",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --ivory: #f5f0e8;
        --paper: #fffdf9;
        --ink: #211a1d;
        --muted: #776c6e;
        --wine: #731f3d;
        --wine-dark: #481226;
        --gold: #b58a51;
        --gold-light: #dbc39e;
        --line: #ddd2c5;
    }

    * { box-sizing: border-box; }

    .stApp {
        background:
            radial-gradient(circle at 3% 10%, rgba(181, 138, 81, .10), transparent 25%),
            radial-gradient(circle at 96% 24%, rgba(115, 31, 61, .07), transparent 28%),
            var(--ivory);
        color: var(--ink);
        font-family: "Aptos", "Segoe UI", sans-serif;
    }

    [data-testid="stAppViewContainer"] > .main { background: transparent; }

    .block-container {
        max-width: 1050px;
        padding-top: 1.35rem;
        padding-bottom: 2rem;
    }

    #MainMenu, footer, header { visibility: hidden; }

    .nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: .25rem 0 1.15rem;
        border-bottom: 1px solid rgba(88, 68, 61, .20);
    }

    .brand {
        display: flex;
        align-items: center;
        gap: .72rem;
    }

    .brand-mark {
        position: relative;
        display: grid;
        place-items: center;
        width: 38px;
        height: 38px;
        overflow: hidden;
        border-radius: 50%;
        background: var(--ink);
        color: var(--gold-light);
        font-family: Georgia, serif;
        font-size: 1rem;
    }

    .brand-mark::after {
        content: "";
        position: absolute;
        right: -9px;
        width: 23px;
        height: 42px;
        background: var(--wine);
        transform: rotate(12deg);
    }

    .brand-name {
        color: var(--ink);
        font-size: .88rem;
        font-weight: 900;
        letter-spacing: .18em;
    }

    .brand-caption {
        margin-top: .07rem;
        color: #998b86;
        font-size: .59rem;
        font-weight: 700;
        letter-spacing: .11em;
    }

    .nav-meta {
        display: flex;
        align-items: center;
        gap: .5rem;
        color: #7b6c69;
        font-size: .67rem;
        font-weight: 800;
        letter-spacing: .08em;
    }

    .live-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #3f8d62;
        box-shadow: 0 0 0 4px rgba(63, 141, 98, .12);
    }

    .hero {
        display: grid;
        grid-template-columns: 1.25fr .75fr;
        align-items: center;
        gap: 4.3rem;
        min-height: 410px;
        padding: 3.4rem 1.6rem 3rem;
    }

    .kicker {
        display: flex;
        align-items: center;
        gap: .7rem;
        color: var(--wine);
        font-size: .66rem;
        font-weight: 900;
        letter-spacing: .18em;
    }

    .kicker::before {
        content: "";
        width: 34px;
        height: 1px;
        background: var(--gold);
    }

    .hero h1 {
        max-width: 650px;
        margin: 1rem 0 1.15rem;
        color: var(--ink);
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(3.3rem, 6.8vw, 5.7rem);
        font-weight: 500;
        line-height: .98;
        letter-spacing: -.055em;
    }

    .hero h1 em {
        color: var(--wine);
        font-weight: 500;
    }

    .hero-copy {
        max-width: 555px;
        margin: 0;
        color: var(--muted);
        font-size: .98rem;
        line-height: 1.75;
    }

    .specs {
        display: flex;
        flex-wrap: wrap;
        gap: 1.15rem;
        margin-top: 1.55rem;
        color: #554b4c;
        font-size: .68rem;
        font-weight: 850;
        letter-spacing: .07em;
        text-transform: uppercase;
    }

    .specs span::before {
        content: "◆";
        margin-right: .46rem;
        color: var(--gold);
        font-size: .48rem;
        vertical-align: .08rem;
    }

    .poster-wrap {
        position: relative;
        display: flex;
        justify-content: center;
    }

    .poster {
        position: relative;
        width: 255px;
        height: 310px;
        overflow: hidden;
        border-radius: 128px 128px 18px 18px;
        background:
            radial-gradient(circle at 68% 28%, rgba(219, 195, 158, .22), transparent 25%),
            linear-gradient(155deg, #7b2946 0%, #481226 66%, #281219 100%);
        box-shadow: 0 30px 55px rgba(61, 25, 37, .24);
    }

    .poster::before {
        content: "";
        position: absolute;
        inset: 12px;
        border: 1px solid rgba(219, 195, 158, .33);
        border-radius: 118px 118px 12px 12px;
    }

    .poster-number {
        position: absolute;
        top: 43px;
        left: 0;
        right: 0;
        color: rgba(255, 255, 255, .06);
        font-family: Georgia, serif;
        font-size: 8rem;
        line-height: 1;
        text-align: center;
    }

    .poster-content {
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 2.2rem;
        color: white;
        text-align: center;
    }

    .poster-icon {
        margin-bottom: 1.1rem;
        color: var(--gold-light);
        font-family: Georgia, serif;
        font-size: 3.2rem;
        line-height: .6;
    }

    .poster-label {
        color: var(--gold-light);
        font-size: .55rem;
        font-weight: 850;
        letter-spacing: .2em;
    }

    .poster-title {
        margin-top: .65rem;
        font-family: Georgia, serif;
        font-size: 1.35rem;
        line-height: 1.25;
    }

    .poster-tag {
        position: absolute;
        right: -22px;
        bottom: 33px;
        min-width: 145px;
        padding: .72rem .85rem;
        border: 1px solid rgba(181, 138, 81, .45);
        border-radius: 3px;
        background: rgba(255, 253, 249, .95);
        box-shadow: 0 14px 35px rgba(50, 29, 34, .15);
        color: var(--ink);
        font-size: .63rem;
        font-weight: 900;
        letter-spacing: .08em;
        text-align: center;
    }

    .poster-tag b { color: var(--wine); }

    .workspace-label {
        margin: .5rem 0 .9rem;
        color: #8a7c77;
        font-size: .62rem;
        font-weight: 900;
        letter-spacing: .17em;
        text-transform: uppercase;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        padding: 1.6rem 1.75rem 1.45rem;
        border: 1px solid var(--line) !important;
        border-radius: 10px !important;
        background: rgba(255, 253, 249, .93) !important;
        box-shadow: 0 18px 55px rgba(60, 42, 38, .08) !important;
    }

    .section-top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: .55rem;
    }

    .section-no {
        color: var(--gold);
        font-family: Georgia, serif;
        font-size: .92rem;
        font-style: italic;
    }

    .section-title {
        margin: 0;
        color: var(--ink);
        font-family: Georgia, serif;
        font-size: 1.65rem;
        font-weight: 500;
    }

    .section-copy {
        margin-top: .25rem;
        color: #8a7d79;
        font-size: .79rem;
    }

    div[data-testid="stSelectbox"] label,
    div[data-testid="stTextArea"] label {
        color: #453a3c !important;
        font-size: .76rem !important;
        font-weight: 850 !important;
        letter-spacing: .035em !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
    div[data-testid="stTextArea"] textarea[data-testid="stTextAreaInput"] {
        border: 1px solid #d8cdc2 !important;
        border-radius: 5px !important;
        background-color: #fffefa !important;
        color: var(--ink) !important;
        box-shadow: none !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div * {
        color: var(--ink) !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:focus-within,
    div[data-testid="stTextArea"] textarea[data-testid="stTextAreaInput"]:focus {
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 3px rgba(181, 138, 81, .11) !important;
    }

    div[data-testid="stTextArea"] textarea[data-testid="stTextAreaInput"] {
        min-height: 165px !important;
        padding: .95rem !important;
        line-height: 1.6 !important;
        -webkit-text-fill-color: var(--ink) !important;
    }

    div[data-testid="stTextArea"] textarea[data-testid="stTextAreaInput"]::placeholder {
        color: #a09590 !important;
        -webkit-text-fill-color: #a09590 !important;
        opacity: 1 !important;
    }

    div[data-baseweb="popover"],
    div[data-baseweb="popover"] ul {
        background-color: #fffefa !important;
        color: var(--ink) !important;
    }

    div[data-baseweb="popover"] li,
    div[data-baseweb="popover"] li * {
        color: var(--ink) !important;
    }

    .stButton > button {
        min-height: 3.18rem;
        margin-top: .45rem;
        border: 1px solid var(--wine) !important;
        border-radius: 5px !important;
        background: var(--wine) !important;
        color: #fffaf4 !important;
        font-size: .76rem !important;
        font-weight: 900 !important;
        letter-spacing: .11em !important;
        text-transform: uppercase !important;
        box-shadow: 0 12px 24px rgba(86, 23, 47, .16) !important;
        transition: all .2s ease !important;
    }

    .stButton > button:hover {
        border-color: var(--wine-dark) !important;
        background: var(--wine-dark) !important;
        transform: translateY(-1px);
        box-shadow: 0 16px 28px rgba(86, 23, 47, .22) !important;
    }

    .result-card {
        position: relative;
        overflow: hidden;
        margin-top: 1.15rem;
        padding: 1.8rem;
        border-radius: 10px;
        background: var(--ink);
        box-shadow: 0 22px 50px rgba(44, 29, 34, .17);
        color: #fffaf4;
    }

    .result-card::after {
        content: "";
        position: absolute;
        top: -110px;
        right: -80px;
        width: 250px;
        height: 250px;
        border: 1px solid rgba(219, 195, 158, .14);
        border-radius: 50%;
        box-shadow: 0 0 0 38px rgba(219, 195, 158, .035), 0 0 0 76px rgba(219, 195, 158, .025);
    }

    .result-top {
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1.2rem;
        padding-bottom: 1.25rem;
        border-bottom: 1px solid rgba(255, 250, 244, .13);
    }

    .result-kicker {
        color: var(--gold-light);
        font-size: .58rem;
        font-weight: 900;
        letter-spacing: .18em;
        text-transform: uppercase;
    }

    .result-title {
        margin-top: .32rem;
        font-family: Georgia, serif;
        font-size: 2rem;
        font-weight: 500;
    }

    .confidence {
        min-width: 120px;
        padding-left: 1.3rem;
        border-left: 1px solid rgba(255, 250, 244, .16);
        text-align: right;
    }

    .confidence-value {
        color: var(--gold-light);
        font-family: Georgia, serif;
        font-size: 1.72rem;
    }

    .confidence-label {
        margin-top: .12rem;
        color: #ac9fa0;
        font-size: .55rem;
        font-weight: 800;
        letter-spacing: .1em;
    }

    .bars-title {
        position: relative;
        z-index: 1;
        margin: 1.15rem 0 .85rem;
        color: #cfc3c3;
        font-size: .65rem;
        font-weight: 850;
        letter-spacing: .12em;
        text-transform: uppercase;
    }

    .bar-row {
        position: relative;
        z-index: 1;
        margin-top: .72rem;
    }

    .bar-labels {
        display: flex;
        justify-content: space-between;
        margin-bottom: .34rem;
        color: #eee5df;
        font-size: .72rem;
        font-weight: 700;
    }

    .bar-track {
        height: 7px;
        overflow: hidden;
        border-radius: 999px;
        background: rgba(255, 250, 244, .11);
    }

    .bar-fill {
        height: 100%;
        border-radius: 999px;
    }

    .bar-fill.positive { background: var(--gold-light); }
    .bar-fill.negative { background: #9c4767; }

    div[data-testid="stExpander"] {
        margin-top: .75rem;
        overflow: hidden;
        border: 1px solid var(--line) !important;
        border-radius: 6px !important;
        background: rgba(255, 253, 249, .75) !important;
    }

    div[data-testid="stExpander"] summary { color: var(--ink) !important; }

    .footer-note {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        margin-top: 2rem;
        padding-top: 1.15rem;
        border-top: 1px solid rgba(88, 68, 61, .20);
        color: #8c7e79;
        font-size: .64rem;
        font-weight: 750;
        letter-spacing: .07em;
        text-transform: uppercase;
    }

    .footer-note strong { color: var(--wine); }

    @media (max-width: 760px) {
        .block-container { padding: 1rem .95rem 1.5rem; }
        .nav-meta { display: none; }
        .hero { grid-template-columns: 1fr; min-height: auto; padding: 2.6rem .35rem 2rem; }
        .poster-wrap { display: none; }
        .hero h1 { font-size: clamp(3rem, 15vw, 4.4rem); }
        div[data-testid="stVerticalBlockBorderWrapper"] { padding: 1.25rem 1rem; }
        .result-card { padding: 1.35rem; }
        .result-title { font-size: 1.55rem; }
        .confidence { min-width: 100px; }
        .footer-note { display: block; line-height: 1.8; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"
VECTORIZER_PATH = BASE_DIR / "vectorizer.joblib"


@st.cache_resource(show_spinner="Preparing language resources...")
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


st.markdown(
    """
    <div class="nav">
        <div class="brand">
            <div class="brand-mark">C</div>
            <div>
                <div class="brand-name">CINESENSE</div>
                <div class="brand-caption">SENTIMENT INTELLIGENCE</div>
            </div>
        </div>
        <div class="nav-meta"><span class="live-dot"></span> MODEL ONLINE · IMDb REVIEWS</div>
    </div>

    <div class="hero">
        <div>
            <div class="kicker">WEEK 9 · PUBLIC DEPLOYMENT</div>
            <h1>Every review<br>holds a <em>feeling.</em></h1>
            <p class="hero-copy">
                A refined sentiment experience that reads an English movie review,
                reveals its emotional direction, and presents the model's confidence.
            </p>
            <div class="specs">
                <span>TF-IDF</span>
                <span>Logistic Regression</span>
                <span>Live Analysis</span>
            </div>
        </div>
        <div class="poster-wrap">
            <div class="poster">
                <div class="poster-number">09</div>
                <div class="poster-content">
                    <div class="poster-icon">“</div>
                    <div class="poster-label">REVIEW INTELLIGENCE</div>
                    <div class="poster-title">Cinema speaks.<br>We listen.</div>
                </div>
            </div>
            <div class="poster-tag"><b>◆</b>&nbsp;&nbsp; READY TO ANALYZE</div>
        </div>
    </div>
    <div class="workspace-label">01 / Sentiment workspace</div>
    """,
    unsafe_allow_html=True,
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

with st.container(border=True):
    st.markdown(
        """
        <div class="section-top">
            <div>
                <div class="section-title">Analyze a movie review</div>
                <div class="section-copy">Choose a sample or compose your own review.</div>
            </div>
            <div class="section-no">No. 01</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    selected_example = st.selectbox("QUICK EXAMPLE", list(example_reviews))
    review = st.text_area(
        "MOVIE REVIEW",
        value=example_reviews[selected_example],
        height=180,
        max_chars=5000,
        placeholder="Write your honest movie review here...",
    )
    analyze_clicked = st.button(
        "Analyze sentiment", type="primary", use_container_width=True
    )


if analyze_clicked:
    if len(review.strip()) < 3:
        st.warning("Please enter a movie review with at least 3 characters.")
    else:
        with st.spinner("Reading the feeling behind your review..."):
            result = predict_sentiment(review)

        confidence_pct = result["confidence"] * 100
        positive_pct = result["positive_probability"] * 100
        negative_pct = result["negative_probability"] * 100

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-top">
                    <div>
                        <div class="result-kicker">Analysis complete</div>
                        <div class="result-title">{result['sentiment']} Sentiment</div>
                    </div>
                    <div class="confidence">
                        <div class="confidence-value">{confidence_pct:.2f}%</div>
                        <div class="confidence-label">MODEL CONFIDENCE</div>
                    </div>
                </div>
                <div class="bars-title">Probability profile</div>
                <div class="bar-row">
                    <div class="bar-labels"><span>Positive</span><span>{positive_pct:.2f}%</span></div>
                    <div class="bar-track"><div class="bar-fill positive" style="width:{positive_pct:.2f}%"></div></div>
                </div>
                <div class="bar-row">
                    <div class="bar-labels"><span>Negative</span><span>{negative_pct:.2f}%</span></div>
                    <div class="bar-track"><div class="bar-fill negative" style="width:{negative_pct:.2f}%"></div></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("View processed text"):
            st.code(result["cleaned_review"] or "No tokens remained after preprocessing.")


st.markdown(
    """
    <div class="footer-note">
        <span>Designed &amp; built by <strong>Asma Bzoor</strong></span>
        <span>IMDb Sentiment Analysis · 2026</span>
    </div>
    """,
    unsafe_allow_html=True,
)
