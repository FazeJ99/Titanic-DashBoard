import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("dataset\Titanic Data.csv")
st.dataframe(df)

st.button("Rerun")
