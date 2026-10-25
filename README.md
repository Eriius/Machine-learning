# Adversarial Business Email Compromise Detection Using Machine Learning Techniques

## Project Description

This project builds a machine learning pipeline to classify Clean Business Email Compromise (BEC) emails and Poisoned/Adversarial BEC emails. The pipeline includes data loading, preprocessing, TF-IDF feature extraction, model training, evaluation, and security interpretation.

## Dataset

The project uses the Kaggle Adversarial BEC Email Dataset.

Files used:
- synthetic_emails.csv
- synthetic_emails_poisoned.csv

The original CSV files contain the columns:
- subject
- body
- label

The final target labels are newly created:
- 0 = Clean BEC email
- 1 = Poisoned / Adversarial BEC email

## Models

The following models are implemented and compared:
- Multinomial Naive Bayes
- Logistic Regression
- Random Forest
- Linear SVC
- Gradient Boosting
- XGBoost

## Best Model

XGBoost achieved the best performance:
- Accuracy: 0.9558
- Precision: 0.9538
- Recall: 0.9578
- F1-score: 0.9558

## How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Open the `model + data` folder.

3. Make sure the dataset files and notebooks are in the same folder:

```text
model + data/synthetic_emails.csv
model + data/synthetic_emails_poisoned.csv
model + data/XGBoost.ipynb
model + data/MultinomialNaiveBayes.ipynb
model + data/LogisticRegressionnew.ipynb
model + data/Random_Forest.ipynb
model + data/LinearSVC.ipynb
model + data/GradientBoosting.ipynb
```

4. Open each notebook and run it from top to bottom.

5. Check the output files inside the `results` folder:

```text
results/model_metrics.csv
results/xgboost_confusion_matrix.png
```