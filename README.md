# # 📊 WiDS 5.0 – Equity Classification

## 🧠 Project Overview
This project is part of **WiDS 5.0 (Winter in Data Science)** and focuses on **equity classification using firm-level financial data**.  
The goal is to preprocess raw financial data, engineer meaningful features, and prepare a **model-ready dataset** for classification tasks.

📌 Reference:  
[WiDS 5.0 – Equity Classification (Notion)](https://www.notion.so/WiDS-5-0-Equity-Classification-2b20d7b271c2802ba6e9d198e1551ab4)

---


---

## 🔍 Dataset
- ~1000 firms with ~30 financial variables  
- Numeric values stored as strings  
- Significant missing values and unlabeled variables  

---

## 🧪 EDA & Preprocessing
- Converted all variables to numeric format  
- Analyzed missing values and dropped fully empty columns  
- Applied **median imputation** for robustness  
- Visualized distributions, outliers, and missingness  

---

## 📐 Feature Engineering
Constructed financially meaningful **proxy ratios**:
- Profitability (Profit Margin Proxy)
- Leverage (Leverage Proxy)
- Efficiency (Asset Turnover Proxy)

Handled division-by-zero issues by removing infinite values and stabilizing distributions.

---

## 🔗 Correlation Analysis
- Computed correlation between engineered ratios  
- Identified potential multicollinearity  
- Retained economically interpretable features  

---

## 📦 Output
- Cleaned and model-ready dataset  
- Financial ratios suitable for equity classification models  

---

## 🛠️ Tech Stack
- Python, Pandas, NumPy  
- Matplotlib, Seaborn  
- Jupyter Notebook  

---

## 🎯 Next Steps
- Equity labeling  
- Classification modeling  
- Feature selection & evaluation  

---

