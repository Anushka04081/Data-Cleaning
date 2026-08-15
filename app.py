import streamlit as st
import pandas as pd

st.title("Task 01: Data Cleaning & Preprocessing Pipeline")

st.header("1. Raw Data")
raw_df = pd.read_csv('data/employees.csv')
st.dataframe(raw_df)

st.header("2. Cleaned Data")
cleaned_df = pd.read_csv('data/cleaned_employees.csv')
st.dataframe(cleaned_df)

st.success("Data cleaning completed successfully!")
