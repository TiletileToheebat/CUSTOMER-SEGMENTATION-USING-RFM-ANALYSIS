# 🛍️ Customer Segmentation Using RFM Analysis & KMeans Clustering

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This project segments customers using **Recency, Frequency, and Monetary (RFM)** metrics, then applies **KMeans Clustering** to identify meaningful groups (e.g., VIPs, loyal customers, at-risk customers). Deployed as an interactive **Streamlit app**.
---
## 🔍 What It Does
- 🔄 **Loads** and cleans retail transaction data.
- 📊 **Calculates RFM** metrics per customer.
- 🔢 **Clusters** customers with KMeans based on RFM scores.
- 🧠 **Labels** customer segments (e.g., VIP, Loyal, Sleeping).
- 📈 **Visualizes** RFM distributions and cluster insights.
- 💻 **Interactive** dashboard lets users query individual customers by ID.
---
## 📂 Project Structure
CUSTOMER-SEGMENTATION-USING-RFM-ANALYSIS/│
├── Content/ # Contains ZIP dataset
├── .gitignore # Ignores venv and system files
├── customer_rfm.ipynb # Jupyter Notebook for exploration
├── customer_rfm.py # Streamlit App
├── customer_with_clusters.csv# Final clustered dataset
├── requirements.txt # Python dependencies
└── README.md # You're here
---
## ⚙️ How to Run Locally
1. **Clone the repo**
```bash
git clone https://github.com/TiletileToheebat/CUSTOMER-SEGMENTATION-USING-RFM-ANALYSIS.git
cd CUSTOMER-SEGMENTATION-USING-RFM-ANALYSIS

