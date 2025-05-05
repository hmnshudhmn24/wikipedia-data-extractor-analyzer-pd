import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Wikipedia Data Extractor + Analyzer")

# Input Wikipedia URL
url = st.text_input("Enter Wikipedia URL:", "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)")
if url:
    try:
        tables = pd.read_html(url)
        st.success(f"✅ Found {len(tables)} tables on the page.")

        # Table selection
        table_index = st.number_input("Select Table Index:", min_value=0, max_value=len(tables)-1, value=0)
        df = tables[table_index]

        # Display raw data
        st.subheader("📋 Raw Table")
        st.write(df.head())

        # Clean column names
        df.columns = [str(col).strip().replace("\n", " ") for col in df.columns]

        # Type fixing
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='ignore')

        st.subheader("🧹 Cleaned Table")
        st.write(df.head())

        # Plotting options
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if len(numeric_cols) >= 2:
            x_col = st.selectbox("Select X-axis column:", numeric_cols)
            y_col = st.selectbox("Select Y-axis column:", numeric_cols, index=1)
            st.subheader("📈 Plot")
            fig, ax = plt.subplots()
            df.plot(x=x_col, y=y_col, kind='bar', ax=ax)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Failed to load tables: {e}")