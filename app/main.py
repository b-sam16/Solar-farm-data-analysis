import sys
from pathlib import Path

# Add this part before any other Streamlit or other code
sys.path.append(str(Path(__file__).resolve().parent.parent))
import streamlit as st  

# Now set the page config as the first Streamlit command
st.set_page_config(page_title="Solar Farm Dashboard", layout="wide")

# Then you can import your other modules
from app.utils import load_combined_data, generate_summary_statistics

import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  

# Header  
st.title("🌞 Solar Farm Data Dashboard")  

# Load data  
data = load_combined_data()  

# Sidebar  
st.sidebar.header("Filters")  
selected_country = st.sidebar.selectbox("Select a Country", options=["All"] + list(data["Country"].unique()))  
if selected_country != "All":  
    data = data[data["Country"] == selected_country]  

# Main Content  
st.header(f"Insights for {selected_country if selected_country != 'All' else 'All Countries'}")  

# Section 1: Summary Statistics  
st.subheader("Summary Statistics")  
summary_stats = generate_summary_statistics(data)  
st.dataframe(summary_stats)  

# Section 2: Time Series Plot  
st.subheader("GHI Over Time")  
plt.figure(figsize=(12, 6))  
sns.lineplot(data=data, x="Timestamp", y="GHI", hue="Country")  
plt.title("GHI Over Time")  
plt.xticks(rotation=45)  
st.pyplot(plt)  

# Section 3: Correlation Analysis
st.subheader("Correlation Analysis")
# Select only numeric columns for correlation calculation
numeric_data = data.select_dtypes(include=[float, int])
correlation_matrix = numeric_data.corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
st.pyplot(plt)
