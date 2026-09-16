# CineSense — Definition of Done

**Final status:** 6 of 6 core requirements met  
**Reviewed on:** September 16, 2026

## Final checklist

| Requirement | Evidence | Status |
|---|---|:---:|
| Full pipeline | IMDb data → duplicate removal → NLTK preprocessing → TF-IDF → Logistic Regression → evaluation → Streamlit | ✅ Met |
| Benchmark met | Accuracy 88.62% and F1 88.79%, both above the documented 85% threshold | ✅ Met |
| Public deployment | Live Streamlit app at [asma-movie-sentiment.streamlit.app](https://asma-movie-sentiment.streamlit.app) | ✅ Met |
| Clean repository | Organized Day1–Day5 files, pinned requirements, model artifacts, documentation, and relative deployment paths | ✅ Met |
| Experiments documented | Final run configuration and results recorded in the notebook and `experiments/experiment_log.csv` | ✅ Met |
| Reproducible notebook | Fixed seed, stratified split, documented preprocessing, saved outputs, and executable validation cells | ✅ Met |

## Evidence by requirement

### 1. Full end-to-end pipeline — Met

- Dataset loaded and duplicates removed.
- Sentiment labels mapped to binary targets.
- Text cleaned, tokenized, filtered, POS-tagged, and lemmatized.
- TF-IDF representation fitted with a maximum of 5,000 features.
- Logistic Regression trained with fixed configuration.
- Model evaluated on an untouched test set.
- Model and vectorizer serialized with Joblib.
- Streamlit interface connected to the saved artifacts.
- Application deployed and tested through a public URL.

### 2. Performance benchmark — Met

**Acceptance criteria**

- Test accuracy ≥ 85%
- Test F1-score ≥ 85%

**Observed results**

- Accuracy: 88.62%
- F1-score: 88.79%
- Precision: 87.76%
- Recall: 89.85%

Both acceptance thresholds were exceeded.

### 3. Public deployment — Met

- Platform: Streamlit Community Cloud
- Branch: `main`
- Entry point: `Week9/Day4/app.py`
- URL: [https://asma-movie-sentiment.streamlit.app](https://asma-movie-sentiment.streamlit.app)
- Positive, negative, short, and invalid inputs tested.
- Recorded live predictions matched the local application.

### 4. Clean repository — Met

- README includes the problem, dataset, method, results, setup, limitations,
  and live URL.
- `requirements.txt` contains pinned versions.
- `model.joblib` and `vectorizer.joblib` are included with the deployed app.
- Application paths are relative to `app.py`; no user-specific production path
  is required.
- Project evidence is separated by training day and purpose.
- Temporary files, caches, local datasets, and editor folders should remain
  excluded through `.gitignore` where appropriate.

### 5. Experiments documented — Met

The project does not claim an MLflow run. Instead, the final reproducible run is
documented honestly in:

- `Week9_Day5.ipynb`
- `experiments/experiment_log.csv`
- `results/model_metrics.json`

The log records the split, seed, preprocessing, feature extraction, model
configuration, and held-out metrics.

### 6. Reproducible notebook — Met

- Duplicate removal is documented.
- Split uses `test_size=0.2`, stratification, and `random_state=42`.
- Model uses `max_iter=1000` and `random_state=42`.
- Exact package versions are pinned for deployment.
- Metrics and confusion matrix outputs are included.
- Paths used for deployment artifacts are relative and portable.

## Final pre-submission safety check

Before the Sprint Review, verify the following directly on GitHub:

- [ ] `Week9/Day4/app.py` is present.
- [ ] `Week9/Day4/model.joblib` is present.
- [ ] `Week9/Day4/vectorizer.joblib` is present.
- [ ] `Week9/Day4/requirements.txt` is present and pinned.
- [ ] `Week9/Day5/` contains all final documentation.
- [ ] The public URL opens in a private/incognito browser window.
- [ ] The repository contains no secrets, API keys, or machine-specific paths.
- [ ] Unrelated Week7 or team-project changes are not included in the Day5 commit.

The first six requirements represent the formal project Definition of Done.
The final GitHub checks are intentionally left as manual confirmations because
they must be verified after the new Day5 files are pushed.
