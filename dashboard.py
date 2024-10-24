import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_data = pd.read_csv('data/day.csv')
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_data['season'] = day_data['season'].map(season_mapping)
day_data['day_type'] = day_data['workingday'].map({0: "Weekend", 1: "Working Day"})

st.title('Bike Sharing Analysis Dashboard')

st.header('Average Rentals by Season')
seasonal_data = day_data.groupby('season')['cnt'].mean().reset_index()
fig1, ax1 = plt.subplots()
sns.barplot(x='season', y='cnt', data=seasonal_data, ax=ax1, palette='coolwarm')
st.pyplot(fig1)

st.header('Average Rentals: Weekend vs Working Day')
day_type_data = day_data.groupby('day_type')['cnt'].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(x='day_type', y='cnt', data=day_type_data, palette='pastel')
st.pyplot(fig2)
