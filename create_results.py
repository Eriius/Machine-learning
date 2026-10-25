import csv
import os

os.makedirs("results", exist_ok=True)

rows = [
    ["Model", "Accuracy", "Precision", "Recall", "F1-score"],
    ["Multinomial Naive Bayes", 0.8042, 0.9737, 0.6245, 0.7609],
    ["Logistic Regression", 0.8189, 0.8683, 0.7511, 0.8054],
    ["Random Forest", 0.7811, 0.8276, 0.7089, 0.7636],
    ["Linear SVC", 0.7832, 0.8045, 0.7468, 0.7746],
    ["Gradient Boosting", 0.8589, 0.8571, 0.8608, 0.8589],
    ["XGBoost", 0.9558, 0.9538, 0.9578, 0.9558],
]

with open("results/model_metrics.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Created results/model_metrics.csv successfully.")