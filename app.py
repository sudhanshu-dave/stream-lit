import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title("CSV Data Visualizer")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)
    st.write("## Data Preview")
    st.write(data.head())

    # Select a column for visualization
    st.write("## Select Column for Charts")
    column = st.selectbox("Choose a column", data.columns)

    # Plotting options
    st.write("## Visualization Options")
    chart_type = st.selectbox("Select chart type", ["Line Chart", "Bar Chart", "Histogram"])

    if chart_type == "Line Chart":
        st.line_chart(data[column])
    elif chart_type == "Bar Chart":
        st.bar_chart(data[column])

