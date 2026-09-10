# Customer Churn Prediction

A machine learning project developed as part of the **Marketing Analytics 2026** course, focused on predicting customer churn using Python and Scikit-learn.

## Overview

Customer churn prediction helps businesses identify customers who may be at risk of leaving and supports data-driven customer retention strategies.

This project develops a complete machine learning pipeline covering:

* Data exploration and quality checks
* Train/test data splitting
* Numerical and categorical feature identification
* Missing-value handling
* Feature scaling and one-hot encoding
* Machine learning model training
* Model evaluation
* Prediction generation
* Confusion matrix analysis
* Feature importance analysis

## Objective

The objective of this project was to build a customer churn prediction pipeline and use the resulting model to identify factors associated with customer churn.

Two datasets were analyzed using the same preprocessing and modeling workflow.

## Dataset

The project contains two customer churn datasets:

| Dataset   | Records | Churn Rate |
| --------- | ------: | ---------: |
| Dataset 1 |  40,000 |      51.8% |
| Dataset 2 |  50,000 |      87.3% |

Both datasets contain 14 columns and no missing values.

The target variable is:

```text
churn
```

## Methodology

### 1. Data Exploration

The datasets were inspected to understand their structure, dimensions, missing values, and summary statistics.

### 2. Train/Test Split

The data was divided into training and testing sets using an **80/20 stratified split** with `random_state=42`.

Stratification was used to preserve the distribution of the churn target across the training and testing sets.

### 3. Data Preprocessing

A Scikit-learn preprocessing pipeline was created for both numerical and categorical variables.

**Numerical features:**

* Median imputation
* Standard scaling

**Categorical features:**

* Most-frequent imputation
* One-hot encoding
* Unknown categories handled safely during transformation

### 4. Model

A **Random Forest Classifier** was used for the final model.

The model was configured with:

```text
n_estimators = 200
random_state = 42
```

The preprocessing and model were combined into a single Scikit-learn pipeline.

### 5. Evaluation

Model performance was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* Confusion matrix

## Results

For **Dataset 2**, the final model achieved:

| Metric    | Result |
| --------- | -----: |
| Accuracy  |  94.0% |
| Precision |  95.3% |
| Recall    |  98.0% |
| F1-score  |  96.6% |
| ROC-AUC   |  0.964 |

### Confusion Matrix — Dataset 2

The model produced:

* True Negatives: 851
* False Positives: 421
* False Negatives: 178
* True Positives: 8,550

The high recall indicates that the model successfully identified the large majority of customers who churned.

## Feature Importance

Feature importance analysis was performed to understand which variables contributed most to the Random Forest predictions.

The strongest features included:

* Monthly spend
* Days since last campaign
* Tenure
* Email engagement

These results suggest that customer spending behavior, campaign recency, customer tenure, and engagement may be useful signals when identifying customers at risk of churn.

### Business Insight

From a marketing perspective, customers showing declining spending or longer periods without campaign engagement could be prioritized for retention campaigns and targeted offers.

## Technologies

* Python 3
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

## Project Files

| File                                   | Description                                                     |
| -------------------------------------- | --------------------------------------------------------------- |
| `churn_prediction.py`                  | Complete Python implementation of the churn prediction pipeline |
| `Customer-Churn-Prediction-Report.pdf` | Project report                                                  |
| `dataset1_HW1_predictions.csv`         | Generated predictions for Dataset 1                             |
| `dataset2_HW1_predictions.csv`         | Generated predictions for Dataset 2                             |
| `feature_importance.png`               | Feature importance visualization                                |
| `README.md`                            | Project documentation                                           |

## How to Run

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```

Then run:

```bash
python churn_prediction.py
```

The program loads the datasets, performs preprocessing, trains the Random Forest model, evaluates its performance, generates predictions, and produces the feature importance visualization.

## Course

**Marketing Analytics — Homework 1**
2026

## Skills Demonstrated

* Python
* Data preprocessing
* Exploratory data analysis
* Classification
* Scikit-learn pipelines
* Random Forest
* Model evaluation
* Feature importance
* Data-driven marketing insights
v
