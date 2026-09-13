# Marketing Mix Modeling with Google Meridian & SHAP

A Bayesian Marketing Mix Modeling (MMM) project that evaluates the effectiveness of paid marketing channels, estimates ROI and marginal ROI, analyzes adstock and saturation, and uses SHAP explainability to support data-driven marketing budget decisions.

## Project Overview

This project analyzes daily eCommerce marketing and purchase data to answer key business questions:

- Which marketing channels generate the most incremental purchases?
- Which channels provide the strongest return on investment?
- Which channels are approaching saturation?
- Where should additional marketing budget be allocated?
- How can model predictions be explained using SHAP?
- What marketing scenarios could improve revenue and profitability?

The analysis combines **Google Meridian Bayesian Marketing Mix Modeling** with **SHAP explainability** and scenario simulation to translate model results into actionable marketing recommendations.

---

## Business Objective

The primary objective is to evaluate marketing effectiveness across paid-media channels and identify opportunities for more efficient budget allocation.

The project focuses on:

1. Measuring channel contribution
2. Estimating historical and marginal ROI
3. Understanding advertising carryover effects through adstock
4. Identifying saturation effects
5. Explaining model predictions using SHAP
6. Simulating alternative marketing budget scenarios
7. Developing a recommended investment strategy

---

## Dataset

The analysis uses daily marketing and purchase data from an eCommerce organization.

For this project, one organization-level time series was selected to maintain a consistent daily history.

**Dataset characteristics:**

- **Industry:** Beauty & Fitness
- **Category:** Face & Body Care
- **Currency:** USD
- **Modeling period:** 21 November 2020 – 19 May 2024
- **Daily observations:** 1,276

### Paid Media Channels

Six paid-media channels were included in the marketing mix model:

- Google Paid Search
- Google Shopping
- Google PMAX
- Google Video
- Meta Facebook
- Meta Instagram

The model also incorporates non-paid and control variables such as organic traffic, email, referral traffic, trend, seasonality, and Black Friday effects.

---

## Methodology

The project follows an end-to-end marketing analytics workflow.

### 1. Exploratory Data Analysis

- Data quality checks
- Missing-value analysis
- Time-series exploration
- Marketing spend analysis
- Purchase and revenue trends
- Channel-level analysis

### 2. Feature Engineering

Marketing and control variables were prepared for modeling, including:

- Media impressions
- Media spend
- Organic traffic
- Email traffic
- Referral traffic
- Trend variables
- Seasonal controls
- Black Friday event controls

### 3. Bayesian Marketing Mix Modeling

The model was developed using **Google Meridian**.

The model incorporates:

- Daily purchase KPI
- Media exposure variables
- Media spend
- Geometric adstock
- Hill saturation transformations
- Maximum lag of 8 days
- Trend and seasonal controls
- Black Friday controls
- Four MCMC chains
- 2,000 retained posterior samples

The model estimates the incremental contribution of each marketing channel while accounting for baseline demand and other control variables.

### 4. Channel Contribution Analysis

The model was used to estimate the contribution of individual marketing channels to incremental purchases.

### 5. ROI & Marginal ROI Analysis

Both historical ROI and marginal ROI were evaluated.

Marginal ROI is particularly important for budget allocation because it estimates the expected return from additional investment rather than evaluating only historical performance.

### 6. SHAP Explainability

SHAP was applied using a Random Forest surrogate model to explain Meridian predictions and identify the relative importance of model inputs.

The surrogate model achieved:

- **R²:** approximately 0.974
- **Correlation with Meridian predictions:** approximately 0.988

### 7. Scenario Simulation

Alternative marketing investment scenarios were evaluated to estimate potential changes in:

- Revenue
- Purchases
- Profit
- Incremental return

---

## Model Performance

The Meridian model produced the following performance:

| Evaluation Set | R² | RMSE | MAPE | Weighted MAPE |
|---|---:|---:|---:|---:|
| Training | 0.746 | 85.62 | 18.27% | 16.65% |
| Holdout | 0.710 | 81.16 | 16.49% | 15.92% |

The holdout results indicate that the model maintained substantial predictive performance on unseen data.

---

## Key Findings

### Channel Contribution

The largest estimated contributors to incremental purchases were:

| Channel / Component | Contribution |
|---|---:|
| Meta Instagram | 35.90% |
| Meta Facebook | 27.56% |
| Google Paid Search | 16.84% |
| Baseline Demand | 17.66% |

Meta Instagram and Meta Facebook were the largest contributors to incremental purchases, while Google Paid Search showed particularly strong efficiency.

### ROI & Marginal ROI

| Channel | Historical ROI | Marginal ROI |
|---|---:|---:|
| Google Paid Search | 11.53 | 5.41 |
| Meta Facebook | 2.40 | 1.42 |
| Meta Instagram | 2.33 | 1.33 |
| Google Shopping | 1.39 | 0.46 |
| Google PMAX | 1.13 | 0.44 |
| Google Video | 0.89 | 0.40 |

### Main Insight

**Google Paid Search was the strongest opportunity for additional investment.**

It achieved both the highest historical ROI and the highest marginal ROI among the analyzed channels.

Google PMAX and Google Shopping showed relatively high saturation and weaker marginal returns, suggesting that additional investment in these channels may be less efficient.

---

## Marketing Budget Scenarios

Several alternative investment scenarios were evaluated:

| Scenario | Revenue Change | Purchase Change | Estimated Profit Change |
|---|---:|---:|---:|
| Paid Search spend +50% | $980,398 | 11,608 | $760,543 |
| Total budget +20%, equal increment | $2,271,142 | 27,018 | $453,296 |
| Random half of channels +10% | $815,244 | 9,861 | $306,115 |
| PMAX and Shopping spend -30% | -$66,816 | -819 | $59,320 |

The **Google Paid Search +50% scenario** produced the highest estimated profit improvement.

---

## Business Recommendation

Based on the model results, the recommended strategy is to use a **marginal-ROI-based approach to budget allocation**.

### Recommended Actions

1. **Increase Google Paid Search investment first**
   - Highest historical ROI: 11.53
   - Highest marginal ROI: 5.41
   - Strongest estimated profit improvement in the scenario analysis

2. **Maintain Meta Facebook and Meta Instagram**
   - Both channels contribute substantially to incremental purchases.
   - Additional investment should be scaled gradually because of potential saturation.

3. **Reduce or hold Google PMAX and Google Shopping**
   - Both channels show relatively weak marginal returns.
   - Additional spending should be approached cautiously.

4. **Review Google Video**
   - Historical ROI and marginal ROI are below 1.
   - Further investment should be evaluated carefully.

5. **Use experimentation to validate budget changes**
   - MMM scenario results are model-based estimates and are not guaranteed future outcomes.
   - Recommended budget changes should be implemented gradually and validated using campaign-level experiments.

---

## Revenue Maximization vs. Profit Maximization

The analysis highlights an important distinction between maximizing revenue and maximizing profitable growth.

The **equal +20% total-budget scenario** produced the largest estimated revenue uplift:

- $2,271,142 additional revenue
- 27,018 additional purchases
- $453,296 estimated profit improvement

However, the **Google Paid Search +50% scenario** generated the highest estimated profit improvement:

- $980,398 additional revenue
- 11,608 additional purchases
- $760,543 estimated profit improvement
- 4.46 incremental ROI on the additional budget

Therefore:

| Business Goal | Preferred Strategy |
|---|---|
| Maximum absolute revenue uplift | Increase total budget by 20% |
| Maximum efficiency and profit | Increase Google Paid Search |
| Recommended overall strategy | Prioritize channels based on marginal ROI |

---

## Technologies

- Python
- Google Meridian
- Bayesian Marketing Mix Modeling (MMM)
- SHAP (SHapley Additive exPlanations)
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Key Skills Demonstrated

- Marketing Analytics
- Marketing Mix Modeling
- Bayesian Modeling
- Marketing Attribution
- ROI Analysis
- Marginal ROI Analysis
- Time-Series Analysis
- Adstock Modeling
- Saturation Modeling
- SHAP Explainability
- Feature Importance Analysis
- Scenario Analysis
- Marketing Budget Optimization
- Data Visualization
- Predictive Analytics
- Business Intelligence
- Data-Driven Decision Making
- Business Recommendation Development

---

## Deliverables

The project includes:

- Complete Marketing Mix Modeling notebook
- Exploratory Data Analysis (EDA)
- Data preparation and feature engineering
- Google Meridian Bayesian MMM implementation
- Channel contribution analysis
- Historical ROI analysis
- Marginal ROI analysis
- Adstock analysis
- Saturation analysis
- SHAP explainability analysis
- Marketing budget scenario analysis
- Model performance evaluation
- Result tables and CSV outputs
- Marketing analytics visualizations
- Business recommendation document
- Project presentation in PDF format
- Project presentation in PowerPoint format
- `requirements.txt` for the project environment

---

## Conclusion

This project demonstrates how marketing analytics can move beyond descriptive reporting toward **data-driven marketing investment decisions**.

By combining **Bayesian Marketing Mix Modeling, ROI analysis, marginal ROI, adstock, saturation analysis, SHAP explainability, and scenario simulation**, the analysis provides a structured framework for evaluating marketing effectiveness and improving budget allocation.

The key findings indicate that:

- **Meta Instagram and Meta Facebook** are major contributors to incremental purchases.
- **Google Paid Search** delivers the strongest historical ROI and marginal ROI.
- **Google PMAX and Google Shopping** show weaker marginal returns and signs of saturation.
- Increasing investment in **Google Paid Search** produced the strongest estimated profit improvement among the tested scenarios.
- Marketing budget decisions should consider **marginal ROI**, rather than relying only on historical ROI.
- Scenario analysis can help compare potential revenue and profit outcomes before implementing budget changes.

The recommended strategy is to **prioritize incremental investment toward Google Paid Search, maintain strong-performing Meta channels, and carefully control additional spending in lower-marginal-return channels**.

Overall, this project demonstrates the practical application of advanced marketing analytics to connect **marketing spend, customer response, channel performance, profitability, and business strategy**.

> **Important:** Scenario results are model-based estimates and should be validated through controlled marketing experiments before implementing large-scale budget changes.

## Project Structure

```text
Marketing-Mix-Modeling-Meridian-SHAP/
│
├── README.md
├── BUSINESS_RECOMMENDATION.md
├── requirements.txt
├── .gitignore
├── Marketing_Mix_Modeling_Meridian_SHAP.ipynb
│
├── outputs/
│   ├── charts/
│   └── tables/
│
└── presentation/
    ├── Marketing_Mix_Modeling_Meridian_SHAP_Assignment.pdf
    └── Marketing_Mix_Modeling_Meridian_SHAP_Assignment.pptx
```

