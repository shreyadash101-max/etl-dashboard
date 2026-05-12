import streamlit as st
import sqlite3
import pandas as pd


# PAGE CONFIG
st.set_page_config(page_title="ETL Dashboard", layout="wide")


# TITLE
st.title("📊 ETL Data Dashboard")


# LOAD DATA (SQLite stays)
conn = sqlite3.connect('data/etl.db')
df = pd.read_sql('SELECT * FROM data', conn)
conn.close()


# DATA PREVIEW
st.subheader("📋 Data Preview")
st.dataframe(df)


# DATA PREP
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])


# KPI SECTION (NEW)
st.subheader("📈 Key Metrics")

col1, col2 = st.columns(2)

if 'sales' in df.columns:
    col1.metric("Total Sales", f"{df['sales'].sum():,.0f}")
    col2.metric("Average Sales", f"{df['sales'].mean():,.2f}")


# CHARTS (BETTER LAYOUT)
st.subheader("📊 Visualizations")

col1, col2 = st.columns(2)

# Sales Trend
if 'date' in df.columns and 'sales' in df.columns:
    with col1:
        st.markdown("### Sales Trend")
        st.line_chart(df.set_index('date')['sales'])

# Sales Category Distribution
if 'sales_category' in df.columns:
    with col2:
        st.markdown("### Sales Category Distribution")
        st.bar_chart(df['sales_category'].value_counts())

# NEW CHART 
st.subheader("📊 Distribution of Sales")

if 'sales' in df.columns:
    st.bar_chart(df['sales'].value_counts())