import streamlit as st
import pandas as pd

st.title("Exam1sridharreddy")

@st.cache
def load_data():
    return pd.read_csv(Clean_df.csv)

data = load_data()

st.write("Here is the data from the CSV file:")
st.dataframe(data)
