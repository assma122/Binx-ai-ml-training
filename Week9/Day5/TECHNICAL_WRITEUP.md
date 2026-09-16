# CineSense — Technical Write-Up

**Author:** Asma Bzoor  
**Project:** IMDb Sentiment Analysis  
**Final model:** TF-IDF with Logistic Regression  
**Live application:** [asma-movie-sentiment.streamlit.app](https://asma-movie-sentiment.streamlit.app)

## 1. Problem

The project addresses binary sentiment classification for English movie
reviews. Given a review, the system predicts whether its sentiment is positive
or negative and returns the corresponding class probabilities. The objective
is to build a complete and reproducible machine-learning pipeline, then expose
the trained model through an accessible public application.

This is useful as a first-stage text analytics tool for organizing large
collections of audience feedback. It is not intended to replace detailed human
interpretation, especially for ambiguous, sarcastic, or mixed reviews.

## 2. Dataset

The IMDb dataset contains a review text field and a binary sentiment label.
Duplicate records were removed before splitting the data, leaving **49,582
unique reviews**.

| Data item | Value |
|---|---:|
| Unique reviews | 49,582 |
| Training set | 39,665 |
| Test set | 9,917 |
| Split | Stratified 80/20 |
| Random seed | 42 |
| Negative label | 0 |
| Positive label | 1 |

Stratification was used to preserve the label balance in both subsets. The
test set was kept separate from model fitting and used for final evaluation.

## 3. Method

### 3.1 Text preprocessing

Each review passes through the same deterministic preprocessing sequence during
training and inference:

1. Decode HTML entities and remove HTML tags.
2. Normalize negative contractions such as `n't` to `not`.
3. Convert text to lowercase.
4. Remove digits and punctuation.
5. Tokenize with NLTK.
6. Remove English stop words while preserving `not`, `no`, and `nor`.
7. Apply part-of-speech tagging.
8. Lemmatize tokens with WordNet.

Preserving negation is important because removing words such as `not` can
reverse the intended meaning of a review.

### 3.2 Feature extraction

The cleaned reviews are converted to sparse numerical vectors using TF-IDF.
The vocabulary is limited to **5,000 features**, balancing useful textual
coverage with memory and inference efficiency. The fitted vectorizer is saved
as `vectorizer.joblib` and reused in production.

### 3.3 Model

A Logistic Regression classifier was trained with `max_iter=1000` and
`random_state=42`. This model was selected because it is a strong, efficient,
and interpretable baseline for high-dimensional sparse text features. The
trained classifier is saved as `model.joblib`.

### 3.4 Reproducibility controls

- Duplicate removal occurs before splitting.
- The split uses stratification and a fixed seed.
- Training and deployment share the same preprocessing function.
- The fitted vectorizer is never refitted during inference.
- Package versions are pinned in `requirements.txt`.
- The model configuration and final metrics are recorded in the experiment log.

## 4. Results

The project acceptance benchmark was defined as at least **85% test accuracy**
and **85% test F1-score**. The final model exceeded both thresholds.

| Metric | Test score | Benchmark | Outcome |
|---|---:|---:|:---:|
| Accuracy | **88.62%** | ≥ 85% | Met |
| Precision, positive class | **87.76%** | Documented | — |
| Recall, positive class | **89.85%** | Documented | — |
| F1-score, positive class | **88.79%** | ≥ 85% | Met |

### Confusion matrix

| Actual / Predicted | Negative | Positive |
|---|---:|---:|
| Negative | 4,316 | 624 |
| Positive | 505 | 4,472 |

Of 9,917 test reviews, 8,788 were classified correctly and 1,129 were
misclassified. The model correctly identified 4,472 of 4,977 positive reviews,
giving a positive recall of 89.85%. It missed 505 positive reviews and
incorrectly labeled 624 negative reviews as positive.

The test classes are nearly balanced, so accuracy is meaningful here; however,
F1 is also reported to jointly reflect precision and recall. Their similar
values indicate that the model is not achieving accuracy by favoring only one
class.

## 5. Deployment

The final inference workflow is packaged as a Streamlit application and hosted
on Streamlit Community Cloud. The app loads the serialized model and vectorizer
from the deployment directory, applies the training preprocessing, and returns
the predicted label with probability-based confidence.

The deployed application was tested with positive, negative, short, and invalid
inputs. Its outputs matched the local version for all recorded validation
cases. The public application is available at:

**https://asma-movie-sentiment.streamlit.app**

## 6. Limitations

1. **Binary output:** neutral and mixed reviews must be assigned to one of two
   classes. For example, a short statement such as “It was okay.” can be forced
   into a negative prediction.
2. **Domain restriction:** the training data consists of IMDb movie reviews;
   behavior may change for product feedback, social posts, or other domains.
3. **Language restriction:** the pipeline was developed for English text.
4. **Representation limits:** TF-IDF captures weighted word occurrence but
   does not model full sentence structure, sarcasm, or long-range context.
5. **Confidence interpretation:** the displayed probability is the classifier's
   estimate, not a guarantee that a prediction is correct.
6. **No production monitoring:** the current version does not track drift,
   latency, or real-world error rates after deployment.

## 7. Future work

- Introduce a neutral or mixed-sentiment option.
- Compare Logistic Regression with Linear SVM and transformer-based models.
- Add probability calibration and threshold analysis.
- Evaluate on an external movie-review dataset.
- Add automated tests for preprocessing and artifact compatibility.
- Collect anonymous feedback and monitor prediction drift.
- Add continuous integration checks before deployment.

## 8. Conclusion

CineSense completes the full machine-learning lifecycle: data preparation,
text preprocessing, feature extraction, model training, held-out evaluation,
artifact serialization, application integration, public deployment, and live
validation. The final Logistic Regression model achieved **88.62% accuracy**
and **88.79% F1-score**, exceeding the documented acceptance benchmark while
remaining fast enough for an interactive public application.
