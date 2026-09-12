# Customer Lifetime Value Analysis

## Overview

This project develops a customer lifetime value (CLV) and purchase prediction framework using transactional customer data. The analysis combines **RFM customer segmentation**, **BG/NBD purchase prediction**, and **CLV estimation** to identify high-value customers and support customer retention and marketing decisions.

The project was originally completed as part of a Marketing Analytics assignment and has been organized here as a portfolio project.

## Objectives

* Segment customers using RFM analysis.
* Model customer purchasing behavior using the **BG/NBD model**.
* Estimate expected customer profit using the **Gamma-Gamma model**.
* Calculate customer lifetime value across 30-day, 90-day, and 365-day horizons.
* Validate purchase predictions using a leakage-free holdout period.
* Compare predicted CLV with actual holdout-period revenue.
* Identify high-value customer segments and individual customers.
* Analyze product-category behavior across CLV segments.

## Methodology

### 1. RFM Segmentation

Customers were evaluated using:

* **Recency** – how recently the customer purchased.
* **Frequency** – number of repeat purchases.
* **Monetary Value** – customer spending.

The resulting RFM segments include:

* Champions
* Potential Loyalists
* Loyal Customers
* Recent Customers
* Need Attention
* Hibernating
* At Risk High Value
* At Risk

### 2. BG/NBD Model

The Beta-Geometric/Negative Binomial Distribution (BG/NBD) model was used to estimate:

* Probability that a customer is still active.
* Expected future purchases.

A leakage-free temporal validation framework was used:

**Calibration period:**
2023-02-26 to 2025-11-22

**Holdout period:**
2025-11-23 to 2026-02-21

The final leakage-free BG/NBD validation produced:

| Metric              |    Result |
| ------------------- | --------: |
| MAE                 |     1.334 |
| RMSE                |    1.9881 |
| R²                  |      0.77 |
| Correlation         |    0.8779 |
| Predicted purchases | 29,540.86 |
| Actual purchases    |    28,517 |

The strong correlation and R² indicate that the model captured the overall differences in customer purchasing activity reasonably well.

### 3. Customer Lifetime Value

CLV was estimated using predicted purchasing behavior and expected average profit.

CLV was calculated for:

* 30-day horizon
* 90-day horizon
* 365-day horizon

The final CLV validation compared predicted 90-day CLV against actual holdout-period revenue.

| Metric                       |        Result |
| ---------------------------- | ------------: |
| MAE                          |      1,140.64 |
| RMSE                         |      1,813.55 |
| Correlation                  |        0.8231 |
| Total predicted 90-day CLV   | 19,970,196.52 |
| Total actual holdout revenue | 19,616,944.23 |

The predicted and actual aggregate values are relatively close, while the correlation indicates that the model successfully captures substantial variation in customer value.

## Key Findings

### RFM and CLV

The highest-value customers are concentrated in the **Champions** segment.

Champions had:

* 2,306 customers
* Average 90-day CLV of approximately **5,065.79**
* Total predicted 90-day CLV of approximately **11.68 million**

Other important segments include Potential Loyalists and Loyal Customers.

### CLV Tiers

Customers were additionally grouped into four CLV tiers:

* Bronze
* Silver
* Gold
* Platinum

Platinum customers represented approximately 20% of customers but had the highest predicted 365-day CLV, with an average of approximately **24,079** per customer.

### Highest-Value Customers

The highest predicted 365-day CLV customer had an estimated CLV of approximately **208,824**.

The top predicted CLV customers were overwhelmingly classified as **Champions**, demonstrating the relationship between strong historical purchasing behavior and predicted future customer value.

## Product Category Analysis

Product purchasing behavior was analyzed across CLV segments.

Across the major CLV segments, **Beverages (Coffee/Malt)** was the highest-quantity product category, followed by categories such as:

* Dairy & Nutrition
* Confectionery
* Culinary (Soups/Seasonings)
* Bottled Water

This analysis provides an additional perspective for designing segment-specific marketing and product strategies.

## Business Implications

The analysis can support marketing decisions such as:

* Prioritizing retention efforts for high-CLV customers.
* Developing loyalty programs for Champions and Platinum customers.
* Identifying customers with high potential future value.
* Designing targeted reactivation campaigns for At Risk and Hibernating customers.
* Using predicted purchasing behavior to support campaign planning.
* Tailoring product recommendations by customer value segment.

## Validation Approach

A temporal holdout methodology was used to reduce information leakage.

Customer behavior observed during the calibration period was used to train the predictive models, while transactions occurring during the subsequent holdout period were reserved for validation.

This provides a more realistic assessment of how the models would perform when predicting future customer behavior.

## Project Structure

```text
Customer-Lifetime-Value-Analysis/
│
├── Customer_Lifetime_Value_Analysis.ipynb
├── CLV_BG_NBG.pdf
├── README.md
└── .gitignore
```

The raw `data/` directory is intentionally excluded from the public repository.

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Lifetimes
* Jupyter Notebook

## Files

**Customer_Lifetime_Value_Analysis.ipynb**
Complete analysis, modeling, validation, segmentation, and visualizations.

**CLV_BG_NBG.pdf**
Project report containing the analysis and results.

**README.md**
Project documentation and methodology summary.

## Conclusion

This project demonstrates an end-to-end customer analytics workflow, progressing from descriptive RFM segmentation to probabilistic purchase prediction and customer lifetime value estimation.

The combination of customer segmentation, BG/NBD modeling, CLV estimation, temporal validation, and product-category analysis provides a practical framework for identifying valuable customers and supporting data-driven marketing strategies.
