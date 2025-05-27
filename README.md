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

Try it out 👉 [Customer Segmentation App][(https://your-app-name.streamlit.app](https://customer-segmentation-using-rfm-analysis-and-kmeans-clustering.streamlit.app/)

---

## 📂 Project Structure

```

CUSTOMER-SEGMENTATION-USING-RFM-ANALYSIS/
│
├── Content/                   # Contains ZIP dataset
├── .gitignore                # Ignores venv and system files
├── customer\_rfm.ipynb        # Jupyter Notebook for exploration
├── customer\_rfm.py           # Streamlit App
├── customer\_with\_clusters.csv# Final clustered dataset
├── requirements.txt          # Python dependencies
└── README.md                 # You're here

````

---

## ⚙️ How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/TiletileToheebat/CUSTOMER-SEGMENTATION-USING-RFM-ANALYSIS.git
cd CUSTOMER-SEGMENTATION-USING-RFM-ANALYSIS
````

2. **Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Launch the Streamlit app**

```bash
streamlit run customer_rfm.py
```

---

## 🚀 Deployment

You can deploy this app for free using **Streamlit Cloud**:

1. Push this repo to GitHub.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in.
3. Click **"New app"**, select the repo and file (`customer_rfm.py`).
4. Click **Deploy**.

Your app will be live in seconds! 🌍

---

## 📌 Key Features

* **Interactive Segmentation**: Enter customer ID and view their RFM and cluster.
* **Cluster Summary**: Average RFM per group.
* **Visual Dashboard**: Tabbed UI for data and visuals.
* **KMeans Implementation**: Uses `StandardScaler` + elbow method to determine optimal K.

---

## 💡 Notes

* The original dataset is located in the `Content/` folder as a `.zip` file.
* Only positive, completed transactions with valid `CustomerID`s are considered.
* Clusters are named as:

  * `VIP Customers`
  * `Loyal Customers`
  * `Sleeping Customers`

---

## 🧠 Tech Stack

* Python 🐍
* Pandas, NumPy
* Scikit-learn (for KMeans)
* Matplotlib & Seaborn (visuals)
* Streamlit (web app)

---

## 📝 License

This project is open source under the [MIT License](LICENSE).
