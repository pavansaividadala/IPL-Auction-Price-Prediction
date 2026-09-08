# 🏏 IPL Auction Price Prediction

An end-to-end machine learning project that predicts a cricket player's IPL auction price based on their performance stats, role, and profile — built from raw data all the way to a deployed, interactive app.

## 📌 Overview

IPL franchises spend crores of rupees on players every auction season, often driven by gut feeling as much as data. This project builds a regression model that estimates a fair auction price (in ₹ Crores) for a player using historical performance metrics, comparing multiple algorithms to find the one that generalizes best.

## 🎯 Problem Statement

Given a player's stats (batting/bowling performance, experience, role, country, team preference, etc.), predict their expected IPL auction price.

## 🗂️ Project Structure

```
├── IPL_Auction_Player_Performance_Analytics.csv   # Raw dataset
├── Modified_dataset.csv                           # Cleaned/processed dataset
├── IPL_EDA.ipynb                                  # Exploratory Data Analysis
├── feature_engineering.ipynb                      # Feature engineering & preprocessing
├── Perfect_Model_Building.ipynb                   # Model training, comparison & tuning
├── xgb_ipl_auction_model.pkl                      # Final trained model (XGBoost)
├── app.py                                         # Streamlit web app
├── requirements.txt                               # Project dependencies
└── .devcontainer/                                 # Dev container config
```

## 🔍 Workflow

1. **EDA** — Explored player performance data to understand distributions, correlations, and outliers.
2. **Feature Engineering** — Cleaned and transformed raw features (batting/bowling stats, experience, categorical fields like Country, Role, and Team Preference) into a model-ready format using scaling and one-hot encoding.
3. **Model Building** — Trained a baseline Linear Regression model, then compared it against Ridge, Lasso, Decision Tree, KNN, Random Forest, Gradient Boosting, and XGBoost — all evaluated on the exact same preprocessing pipeline for a fair comparison.
4. **Evaluation** — Used **Mean Absolute Error (MAE)** as the primary metric, since it's interpretable directly in ₹ Cr and less sensitive to skew from high-value players.
5. **Hyperparameter Tuning** — Tuned the best-performing model using `GridSearchCV` (5-fold cross-validation).
6. **Deployment** — Packaged the final model into an interactive **Streamlit** app for real-time price predictions.

## 🏆 Results

| Model | MAE (₹ Cr) |
|---|---|
| Linear Regression (baseline) | ~1.07 |
| **XGBoost (final model)** | **~1.00** |

**R² Score:** ~0.84

XGBoost outperformed all other algorithms and was selected as the final model.

## 🖥️ App Features

The Streamlit app (`app.py`) takes the following inputs and returns a predicted auction price:

- Player Name, Age, Country, Role
- Matches Played, Experience (Yrs)
- Runs, Strike Rate, Wickets, Economy, Average
- Team Preference

## ⚙️ Tech Stack

- **Language:** Python
- **Data & ML:** Pandas, NumPy, Scikit-Learn, XGBoost
- **Visualization:** Matplotlib, Seaborn
- **Model Tuning:** GridSearchCV
- **Deployment:** Streamlit

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/pavansaividadala/IPL-Auction-Price-Prediction.git
cd IPL-Auction-Price-Prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

## 📊 Dataset

The dataset includes historical IPL player performance data — batting stats, bowling stats, experience, role, country, and team preference — used to train and evaluate the pricing model.

## 🔮 Future Improvements

- Incorporate more recent auction data for better generalization
- Add SHAP-based explainability to show which features drive each prediction
- Deploy on a cloud platform (e.g. Streamlit Community Cloud / AWS) for public access

## 🙋 Author

**Pavan Sai**
Aspiring Data Science Engineer | Python · SQL · Machine Learning

---
⭐ If you found this project useful, consider giving it a star!
