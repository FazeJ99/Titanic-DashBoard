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

# Scatter plot of Age against Fare
st.write("Scatter Chart of Age against Fare")
st.scatter_chart(data=df, x = 'Age' , y = 'Fare')

# Histogram of Age of Survivors
st.write("Histogram of Age of Survivors")
fig = px.histogram(df , x='Age' , color='Survived')
st.plotly_chart(fig)


st.write("Box plot to compare age distribution across different classes")
# Box Plot: To compare age distribution across different classes
fig = px.box(df , y  = 'Age' , color = 'Pclass')
st.plotly_chart(fig)


st.write("Survival Rate of Passengers based on the Ports embarked(Southampton,Cherbourg,Queenstown)")
# Bar Chart: To analyze the survival rate of passengers based on the port they embarked from
fig = px.bar(df , x = 'Embarked' , y = 'Survived')
st.plotly_chart(fig)

