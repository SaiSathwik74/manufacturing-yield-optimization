import streamlit as st
import pandas as pd

df = pd.read_csv("../data/raw/manufacturing_data.csv")

st.title("Manufacturing Yield Dashboard")
st.metric("Average Yield (%)", round(df["yield_percent"].mean(), 2))
st.metric("Avg Downtime (min)", round(df["downtime_minutes"].mean(), 2))
st.line_chart(df["yield_percent"].sample(500))
