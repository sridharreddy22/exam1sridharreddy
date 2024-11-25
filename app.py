import streamlit as st
import pandas as pd

# App title
st.title("Exam1sridharreddy")

# Load the data from CSV
@st.cache
def load_data():
    # Correctly specify the file name as a string
    return pd.read_csv("clean_df.csv")  # Make sure the file name matches the uploaded CSV

# Load the data
try:
    data = load_data()
    st.write("Here is the data from the CSV file:")
    st.dataframe(data)
except FileNotFoundError:
    st.error("The file 'Clean_df.csv' was not found. Please ensure it is uploaded correctly.")
