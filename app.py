import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Load CSV data into DataFrame
events_data = pd.read_csv('eventseattle.csv')

# Establish a connection to the PostgreSQL database
engine = create_engine('postgresql://xbmqnounao:12D177O375IC8KO7$@ankit25-lab5-redo-server.postgres.database.azure.com:5432/ankit25-lab5-redo-database')

# Insert data into the PostgreSQL database
events_data.to_sql('events_table', engine, index=False, if_exists='replace')

# Load data from PostgreSQL
query = "SELECT * FROM events_table"
events_data = pd.read_sql(query, engine)

# Features

# 1. Create at least 3 charts
st.title("Seattle Events Data Visualization")

# Chart 1: Most common event categories
st.subheader("Most Common Event Categories")
category_counts = events_data['Type'].value_counts()
st.bar_chart(category_counts)

# Chart 2: Events per month
st.subheader("Events Per Month")
events_data['Date'] = pd.to_datetime(events_data['Date'], errors='coerce')
events_data['Month'] = events_data['Date'].dt.month
monthly_counts = events_data['Month'].value_counts().sort_index()
st.line_chart(monthly_counts)

# Chart 3: Events per day of the week
st.subheader("Events Per Day of the Week")
events_data['Day_of_Week'] = events_data['Date'].dt.day_name()
day_counts = events_data['Day_of_Week'].value_counts()
st.bar_chart(day_counts)

# 2. Create 3 controls for your data
st.sidebar.title("Data Controls")

# Control 1: Dropdown for filtering category
selected_category = st.sidebar.selectbox("Filter by Category", events_data['Type'].unique())

# Control 2: Date range selector for event date
date_range = st.sidebar.date_input("Select Date Range", [events_data['Date'].min(), events_data['Date'].max()])

# Control 3: Filter by location
selected_location = st.sidebar.selectbox("Filter by Location", events_data['Location'].unique())

# Optional: Filter by weather (if available)
# Note: You need to modify your dataset to include weather information

filtered_data = events_data[(events_data['Type'] == selected_category) &
                            (events_data['Date'].between(date_range[0], date_range[1])) &
                            (events_data['Location'] == selected_location)]

# Display filtered data
st.write("Filtered Data:")
st.table(filtered_data)

# Close the database connection
engine.dispose()
