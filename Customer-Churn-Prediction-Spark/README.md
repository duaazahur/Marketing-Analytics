# Customer Churn Prediction Using PySpark

## Overview

This project applies Apache Spark's machine learning API to predict customer churn using two customer datasets.

The project demonstrates an end-to-end Spark machine learning workflow, including data preparation, feature preprocessing, model training, evaluation, and model comparison.

## Objectives

- Prepare customer data for machine learning using PySpark.
- Handle numerical and categorical features.
- Build a reusable Spark preprocessing pipeline.
- Train and compare multiple classification models.
- Evaluate customer churn prediction performance.
- Identify the best-performing model for each dataset.

## Datasets

Two customer churn datasets were analyzed.

| Dataset | Rows | Columns |
|---|---:|---:|
| Dataset 1 | 40,000 | 14 |
| Dataset 2 | 50,000 | 14 |

The target variable is `churn`.

### Features

- `age`
- `gender`
- `region`
- `income`
- `tenure_months`
- `monthly_spend`
- `website_visits`
- `support_tickets`
- `email_click_rate`
- `loyalty_score`
- `campaign_type`
- `discount_used`
- `last_campaign_days`

Both datasets were checked for missing values.

## Methodology

### 1. Data Preparation

The datasets were loaded using PySpark. Their schemas, dimensions, and sample records were inspected.

### 2. Feature Preprocessing

A Spark ML preprocessing pipeline was created using:

- `Imputer` for numerical variables
- `StringIndexer` for categorical variables
- `OneHotEncoder` for categorical features
- `VectorAssembler` to combine the features
- `StandardScaler` to standardize the feature vector

The datasets were divided into training and testing sets using an 80/20 split.

### 3. Machine Learning Models

Three classification models were trained on both datasets:

1. Logistic Regression
2. Random Forest
3. Gradient-Boosted Trees

### 4. Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Confusion matrices were also used to examine the predictions of the selected models.

## Results

### Dataset 1

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8107 | 0.8107 | 0.8107 | 0.8107 | **0.8960** |
| Random Forest | 0.7945 | 0.7953 | 0.7945 | 0.7939 | 0.8758 |
| Gradient-Boosted Trees | 0.8034 | 0.8033 | 0.8034 | 0.8033 | 0.8885 |

### Dataset 2

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9399 | 0.9375 | 0.9399 | 0.9382 | **0.9690** |
| Random Forest | 0.9250 | 0.9235 | 0.9250 | 0.9142 | 0.9489 |
| Gradient-Boosted Trees | 0.9361 | 0.9338 | 0.9361 | 0.9347 | 0.9658 |

## Best Model

Logistic Regression achieved the highest ROC-AUC on both datasets:

- **Dataset 1:** ROC-AUC = 0.8960
- **Dataset 2:** ROC-AUC = 0.9690

Dataset 2 achieved substantially stronger predictive performance than Dataset 1 across the evaluated metrics.

## Key Takeaway

The results demonstrate an end-to-end Spark machine learning workflow for customer churn prediction.

Among the three evaluated models, Logistic Regression provided the strongest overall predictive performance on both datasets.

##Technologies

Python
PySpark
Apache Spark ML
Pandas
Jupyter Notebook

## Project Structure

```text
Customer-Churn-Prediction-Spark/
│
├── Customer_Churn_Prediction_Spark.ipynb
├── HW3_final_model_results.csv
└── README.md

