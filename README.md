# 🌐 Wikipedia Data Extractor + Analyzer

This Streamlit app pulls tables from Wikipedia pages and helps you clean, explore, and visualize the data using Pandas and Matplotlib.

## 🎯 Features

- Enter any Wikipedia URL and select a table by index
- Uses `pandas.read_html()` to extract tables
- Automatically cleans column names and fixes data types
- Visualizes selected numeric columns with bar charts

## 🔗 Example Wikipedia URLs

- GDP by Country: https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)
- Inflation Rate: https://en.wikipedia.org/wiki/Inflation_rate

## 🚀 How to Run

Install required packages:

```bash
pip install streamlit pandas matplotlib
```

Run the app:

```bash
streamlit run app/main.py
```

## 📂 Project Structure

- `app/main.py` — Streamlit application
- `data/` — Optional for saving downloaded tables
- `README.md` — Project documentation

Upload a Wikipedia URL, choose a table, and start analyzing like a data wizard! 🧙‍♂️📈