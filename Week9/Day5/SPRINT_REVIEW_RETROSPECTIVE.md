# CineSense — Sprint Review & Full-Project Retrospective

**Presenter:** Asma Bzoor  
**Sprint:** Sprint 4 close-out  
**Project status:** Publicly deployed and benchmark validated

## Sprint Review

### Review objective

Demonstrate that CineSense is no longer only a local notebook model. It is a
complete, reproducible machine-learning project with a public interface,
documented evaluation, and clear limitations.

### Recommended five-minute demo flow

1. **Problem — 30 seconds**  
   Explain that manually reviewing thousands of IMDb comments is slow, so the
   project predicts whether an English movie review is positive or negative.

2. **Pipeline — 45 seconds**  
   Show the path from raw review to NLTK preprocessing, TF-IDF features,
   Logistic Regression, prediction, and confidence.

3. **Results — 60 seconds**  
   Present the held-out test results: 88.62% accuracy and 88.79% F1, both above
   the 85% acceptance benchmark. Briefly explain the confusion matrix.

4. **Live application — 90 seconds**  
   Open [CineSense](https://asma-movie-sentiment.streamlit.app), test one
   clearly positive review and one clearly negative review, then show the
   probability bars and processed text.

5. **Limitations and close — 45 seconds**  
   State that the app is binary, English-only, and trained on movie reviews.
   Finish by noting that the full pipeline, public deployment, documentation,
   and reproducibility requirements are complete.

## Short presentation script

> CineSense is an IMDb sentiment-analysis application that classifies English
> movie reviews as positive or negative. I started with 49,582 unique labeled
> reviews and used a stratified 80/20 split with a fixed random seed. The text
> pipeline cleans HTML, preserves important negation words, tokenizes, removes
> stop words, and applies POS-aware lemmatization. I transformed the reviews
> into 5,000 TF-IDF features and trained Logistic Regression. On 9,917 unseen
> test reviews, the model reached 88.62% accuracy and 88.79% F1, exceeding the
> 85% benchmark. I then saved the model and vectorizer, integrated them into a
> Streamlit application, deployed it publicly, and confirmed that the live
> results match the local version. The main limitations are binary output,
> English-only support, and difficulty with sarcasm or mixed sentiment. Future
> work would add a neutral class, external evaluation, and a transformer model.

## Demo inputs

| Purpose | Review | Expected result |
|---|---|---|
| Positive | `This movie was absolutely amazing, beautifully acted, and worth watching.` | Positive |
| Negative | `The story was boring, the acting was terrible, and I regret watching it.` | Negative |
| Limitation | `It was okay.` | Negative; explain forced binary behavior |
| Validation | `a` | Input warning |

## Sprint 4 review summary

### Completed

- Model and preprocessing artifacts integrated into the application.
- Streamlit interface refined into a complete user experience.
- Dependencies pinned for deployment.
- Application published through Streamlit Community Cloud.
- Local and live predictions compared with representative inputs.
- Public URL and setup instructions documented.
- Held-out benchmark and confusion matrix added to the final write-up.

### Evidence

- Public URL: [asma-movie-sentiment.streamlit.app](https://asma-movie-sentiment.streamlit.app)
- Accuracy: 88.62%
- F1-score: 88.79%
- Live/local validation: all four recorded cases matched
- Definition of Done: six core requirements addressed

## Full-project retrospective

### Sprint 1 — Data understanding and preparation

**What went well**

- The task and target were clearly defined as binary sentiment classification.
- Duplicate removal prevented repeated reviews from influencing both splits.
- Stratification and a fixed seed established a reproducible evaluation basis.

**What I would improve**

- Define the final acceptance benchmark at the very beginning.
- Create the experiment log before training rather than documenting it at
  project close-out.

### Sprint 2 — Modelling and evaluation

**What went well**

- TF-IDF and Logistic Regression provided a strong and efficient classical
  baseline.
- Preserving negation improved the semantic quality of preprocessing.
- The final model achieved balanced accuracy, precision, recall, and F1.

**What I would improve**

- Compare more baselines systematically, such as Naive Bayes and Linear SVM.
- Add threshold analysis, cross-validation, and probability calibration.
- Record every attempted run immediately in MLflow or a structured experiment
  table.

### Sprint 3 — Integration and interface

**What went well**

- The saved vectorizer and model kept inference consistent with training.
- FastAPI and Streamlit demonstrated two ways to expose the classifier.
- Input validation and confidence display made the result easier to understand.

**What I would improve**

- Add automated unit tests for preprocessing and API responses earlier.
- Measure cold-start and prediction latency explicitly.
- Separate preprocessing into a shared module to avoid duplicated logic.

### Sprint 4 — Deployment and project close-out

**What went well**

- The application became accessible through a real public URL.
- Local and live behavior matched across representative tests.
- The repository now includes a technical write-up, metrics, limitations, and
  a Definition of Done checklist.

**What I would improve**

- Deploy an intentionally minimal version earlier in the sprint.
- Automate smoke testing after every deployment.
- Keep final documentation updated continuously rather than collecting it on
  the final day.

## What I will carry into Week 10

- Lead with the problem and the live demo, not with code.
- Memorize the project story rather than every implementation detail.
- Explain the benchmark, test split, and confusion matrix confidently.
- State limitations honestly and connect each one to future work.
- Keep a backup screenshot and local version ready in case the live service is
  temporarily unavailable.
- Use the same five-part story: **problem → pipeline → results → live demo →
  limitations**.

## Final retrospective statement

The most important transition in this project was moving from a working model
inside a notebook to a reproducible public product. The final result is not
perfect, but it is measurable, explainable, deployable, and honest about its
scope. That combination is what makes the project ready for a technical review
and Week 10 presentation.
