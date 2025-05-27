import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from zipfile import ZipFile

# PAGE CONFIG
st.set_page_config(page_title="Customer Segmentation RFM", layout="wide")

st.title("🛍️🛒 Customer Segmentation Using RFM Analysis")

uploaded_zip = st.file_uploader("Upload ZIP file with your data (CSV inside)", type=["zip"])

def wrangle_data(df):
    df_clean = df.copy()
    df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'], errors='coerce')
    df_clean.dropna(subset=['CustomerID'], inplace=True)
    df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]
    df_clean.drop_duplicates(inplace=True)
    df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['UnitPrice']
    df_clean['CustomerID'] = df_clean['CustomerID'].astype(int)
    df_clean.reset_index(drop=True, inplace=True)
    return df_clean

if uploaded_zip:
    with ZipFile(uploaded_zip) as zip_file:
        csv_files = [f for f in zip_file.namelist() if f.endswith('.csv')]
        if not csv_files:
            st.error("No CSV found inside the ZIP.")
            st.stop()
        with zip_file.open(csv_files[0]) as csvfile:
            df = pd.read_csv(csvfile, encoding='latin-1')

    df_clean = wrangle_data(df)

    # Compute RFM
    reference_date = df_clean['InvoiceDate'].max() + pd.Timedelta(days=1)
    rfm = df_clean.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (reference_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    }).reset_index()
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

    # Scale for clustering
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

    # KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

    cluster_names = {2: "VIP Customers", 0: "Loyal Customers", 1: "Sleeping Customers"}
    rfm['ClusterName'] = rfm['Cluster'].map(cluster_names)

    # Merge cluster info to original cleaned df
    df_with_clusters = df_clean.merge(rfm, on='CustomerID', how='left')

    # -- TABS --
    tab_overview, tab_customer, tab_summary, tab_viz = st.tabs(
        ["📄 Overview", "👤 Customer Details", "📋 Cluster Summary", "📊 Data Visualization"]
    )

    with tab_overview:
        st.header("Customer Segmentation Overview")
        st.markdown("""
        This app segments customers based on Recency, Frequency, and Monetary (RFM) metrics, using KMeans clustering.
        
        - **Recency:** Days since last purchase
        - **Frequency:** Number of purchases
        - **Monetary:** Total spending
        
        Use the tabs to explore individual customers, see summary statistics, or explore data visualizations.
        """)

    with tab_customer:
        st.header("Customer Transaction & RFM Details")

        selected_id = st.selectbox("Select CustomerID", rfm['CustomerID'].sort_values())

        if selected_id:
            customer_rfm = rfm[rfm['CustomerID'] == selected_id].iloc[0]
            st.markdown(f"### Customer ID: {selected_id}")
            st.markdown(f"**Cluster:** {customer_rfm['ClusterName']}")
            st.markdown(f"- Recency (days since last purchase): {customer_rfm['Recency']}")
            st.markdown(f"- Frequency (purchase count): {customer_rfm['Frequency']}")
            st.markdown(f"- Monetary (total spend): ${customer_rfm['Monetary']:.2f}")

            st.subheader("Transactions")
            cust_transactions = df_with_clusters[df_with_clusters['CustomerID'] == selected_id]
            st.dataframe(cust_transactions[['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'TotalPrice']])

    with tab_summary:
        st.header("Cluster Summary & Insights")

        cluster_summary = rfm.groupby('ClusterName').agg({
            'Recency': 'mean',
            'Frequency': 'mean',
            'Monetary': ['mean', 'count']
        }).round(2)
        cluster_summary.columns = ['Recency Mean', 'Frequency Mean', 'Monetary Mean', 'Customer Count']
        cluster_summary = cluster_summary.sort_values('Customer Count', ascending=False)

        st.dataframe(cluster_summary)

        st.markdown("### Insights:")
        st.markdown("""
        - **VIP Customers:** Low recency, high frequency, and very high monetary value.
        - **Loyal Customers:** Moderate recency and frequency with good spending.
        - **Sleeping Customers:** High recency (haven't purchased recently), low frequency, and low monetary value.
        """)

    with tab_viz:
        st.header("Data Visualizations")

        st.subheader("RFM Metrics Distribution by Cluster")
        sns.set(style="whitegrid")
        fig = sns.pairplot(rfm, hue='ClusterName', palette='Set2', markers=["o", "s", "D"])
        st.pyplot(fig)

        st.subheader("Elbow Method to Find Optimal Clusters")
        wcss = []
        for i in range(1, 11):
            km = KMeans(n_clusters=i, random_state=42)
            km.fit(rfm_scaled)
            wcss.append(km.inertia_)
        fig2, ax2 = plt.subplots()
        ax2.plot(range(1, 11), wcss, marker='o')
        ax2.set_xlabel('Number of Clusters')
        ax2.set_ylabel('WCSS')
        ax2.set_title('Elbow Method')
        st.pyplot(fig2)

else:
    st.info("Please upload a ZIP file containing the customer transactions CSV to proceed.")
