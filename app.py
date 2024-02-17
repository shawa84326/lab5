import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine("postgresql://coolusername:xxxxxxxx@techin510fffff.postgres.database.azure.com:5432/lab5")

# Load data from the database
query = "SELECT * FROM events"
events_data = pd.read_sql(query, engine)

# Filter controls
category_filter = st.selectbox("Filter by Category", events_data["Category"].unique())
date_range_selector = st.date_input("Select Date Range", [events_data["Date"].min(), events_data["Date"].max()])
location_filter = st.selectbox("Filter by Location", events_data["Location"].unique())
# You can add a weather filter if needed

# Apply filters
filtered_data = events_data[
    (events_data["Category"] == category_filter) &
    (events_data["Date"] >= date_range_selector[0]) &
    (events_data["Date"] <= date_range_selector[1]) &
    (events_data["Location"] == location_filter)
]

# Visualizations
st.bar_chart(filtered_data["Category"].value_counts(), caption="Category Distribution")
st.bar_chart(filtered_data["Date"].dt.month.value_counts(), caption="Monthly Event Distribution")
st.bar_chart(filtered_data["Date"].dt.day_name().value_counts(), caption="Day of the Week Event Distribution")

