# Day 5 — Phase 3 Project Selection & Sprint 1 Planning

> Planning the next stage of the **Cardiac Patient Monitoring System**.

## 1. Selected Capstone Project

For Phase 3, I selected the **Cardiac Patient Monitoring System** as my capstone project.

The project uses 13 clinical patient features to predict whether heart disease is present or absent. Since the target has two possible classes, this is a **binary classification** problem.

I selected this project because it allows me to apply a complete machine-learning workflow: data validation, EDA, preprocessing, baseline modeling, model comparison, tuning, evaluation, and deployment.

## 2. Problem Statement

Heart disease assessment requires examining several clinical measurements together rather than relying on one value alone.

This project aims to build a machine-learning system that uses patient information—such as age, chest pain type, cholesterol, resting blood pressure, maximum heart rate, and other examination results—to predict whether heart disease is present or absent.

The system is intended to support early risk assessment and demonstrate a complete machine-learning workflow. It is **not** intended to replace professional medical diagnosis.

## 3. Project Objective

The objective is to create a clear and reproducible workflow that:

- validates and explores the heart disease dataset;
- prepares the data for model training;
- establishes Logistic Regression as a baseline model;
- compares and tunes alternative models;
- evaluates performance using appropriate classification metrics;
- and deploys the selected model through a simple public application.

## 4. Definition of Done

The project will be considered complete when all of the following are ready:

- [ ] A clean notebook documents EDA, preprocessing, modeling, and evaluation.
- [ ] The selected model is evaluated using accuracy, precision, recall, F1-score, confusion matrix, and other relevant results.
- [ ] The final trained model is saved as a reusable artifact.
- [ ] A working Streamlit or FastAPI application is available through a public URL.
- [ ] The repository contains a clear README, `requirements.txt`, source files, and model artifacts.
- [ ] A short technical write-up explains the approach, results, final decision, and limitations.

> A high model score alone does not mean that the project is complete or medically ready. The final result must also be reproducible, documented, deployable, and clear about its limitations.

## 5. Four-Sprint Plan

I divided the project into four sprints so that each week has one clear purpose.

1. **Sprint 1 — Understand:** Validate the dataset, complete the EDA, prepare the data, and build a baseline model.
2. **Sprint 2 — Improve:** Compare models, analyze errors, use cross-validation, and tune the selected model.
3. **Sprint 3 — Build:** Prepare the final pipeline, save the model, and build a simple prediction interface.
4. **Sprint 4 — Deliver:** Test and deploy the application, then complete the README and final documentation.

## 6. Sprint 1 Goal

By the end of Sprint 1, I want to have:

1. a clear understanding of each patient record, feature, and target value;
2. a complete data-quality check;
3. documented EDA findings about the main patient patterns;
4. prepared training and testing data;
5. and a Logistic Regression baseline with recorded evaluation metrics.

The baseline result will be used as the reference that later models must improve upon.

## 7. Sprint 1 Backlog

| Task | What I will do | Effort estimate |
|---|---|---:|
| Document the dataset | Record the source, shape, features, target, and problem type. | 2 hours |
| Check data quality | Check missing values, duplicates, data types, category values, and numerical ranges. | 2 hours |
| Complete the EDA | Explore class balance, distributions, group differences, correlations, and potential outliers. | 5 hours |
| Prepare the data | Separate features and target, then create a stratified train-test split. | 2 hours |
| Build the baseline | Scale the features and train Logistic Regression. | 3 hours |
| Evaluate and document | Report the metrics, confusion matrix, observations, and baseline conclusion. | 3 hours |

**Estimated Sprint 1 effort:** 17 hours

The estimates are planning guides. They may change if a task reveals an unexpected data or modeling issue.

## 8. Acceptance Criteria

### Criteria for Every Task

- The notebook cells run without errors.
- The result is explained in Markdown instead of leaving unexplained output.
- The work is committed to the correct feature branch with a clear message.
- A pull request is opened for review before merging into `main`.

### Task-Specific Criteria

#### Dataset Documentation

- The dataset source is included.
- The shape is documented as 303 patient records and 14 columns.
- The 13 input features and binary target are explained.

#### Data Quality Check

- Missing values and duplicate records are checked.
- Data types, categorical codes, and numerical ranges are validated.
- Potential outliers are identified, and the decision to keep or treat them is explained.

#### Exploratory Data Analysis

- The target balance is reported.
- Main numerical and categorical features are explored.
- Differences between the two target groups are interpreted.
- Correlations and potential outliers are discussed without treating correlation as causation.

#### Data Preparation

- The input features `X` and target `y` are separated.
- A stratified train-test split is created.
- Any learned preprocessing is fitted using the training data only.

#### Baseline Model and Evaluation

- Logistic Regression is trained as the baseline model.
- Predictions are generated on the held-out test set.
- Accuracy, precision, recall, F1-score, and a confusion matrix are reported.
- False positives and false negatives are explained in the heart-disease context.

## 9. GitHub Workflow

The project will use a feature-branch and pull-request workflow:

```text
main
  └── feature/sprint1-baseline
          └── commit and push changes
                  └── open pull request
                          └── mentor review
                                  └── merge into main
```

Example branch name:

```text
feature/sprint1-baseline
```

Example commit message:

```text
Complete Sprint 1 EDA and baseline model
```

## 10. Mentor Sign-off

- **Selected project:** Cardiac Patient Monitoring System
- **Sprint 1 goal:** Defined
- **Backlog and acceptance criteria:** Prepared
- **Mentor approval:** Pending review

## Final Planning Note

Sprint 1 establishes the foundation of the project. Later improvements will be meaningful only if the dataset is understood, the evaluation is documented, and a clear baseline exists for comparison.
