import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://raw.githubusercontent.com/FazeJ99/titanic-dash/refs/heads/main/dataset/Titanic%20Data.csv")
st.dataframe(df)
df.head()

st.button("Rerun")
# Bar chart of gender(sex) against Passenger class
st.write("Bar Chart of Gender against Passenger Class")
st.bar_chart(data=df, x = 'Sex' , y= 'Pclass')

# Pie chart of Survival status according to Gender 
fig = px.pie(df , values= 'Survived', names='Sex', title="Survival according to Gender")

st.plotly_chart(fig)

st.write("Scatter Chart of Age against Fare")
st.scatter_chart(data=df, x = 'Age' , y = 'Fare')