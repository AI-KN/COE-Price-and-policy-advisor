import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from data.coe_history import Data_URL
from streamlit_dynamic_filters import DynamicFilters
 
st.header('🔎 COE Data Explorer')
"""This app allows you to visualise historical COE data (From 2010 to current) for better informed decision making. Please feel free to explore the interactive chart and tables!"""

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(Data_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['month'] = pd.to_datetime(data['month'])
    return data


# Create a text element and let the reader know the data is loading.
#data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
#data_load_state.text("Done! (using st.cache_data)")

#if st.checkbox('Show raw data'):
#    st.subheader('Raw data')
#    st.write(data)

st.subheader('COE Premiums by year 📈')
"""Please select a Category using the slide below to view the COE premiums for each period"""
Category_filter = st.select_slider('Category', options=["Category A","Category B","Category C","Category D","Category E"])
filtered_data = data[data['vehicle_class'] == Category_filter]
#hist_values = np.histogram(
#    data['month'].dt.year, bins=14, range=(2010,2024))[0]
st.line_chart(filtered_data,x='month',y='premium')
"*COE bidding was suspended from April 2020 to June 2020 due to the circuit breaker introduced to curb the spread of COVID-19."

st.divider()

st.subheader('Filter the data by period and/or Vehicle Category 📊')
"Please select the Period and Category below to load the corresponding data table. You may select multiple periods and vehicle categories."
dynamic_filters = DynamicFilters(df=data, filters=['month', 'vehicle_class'])
dynamic_filters.display_filters()
dynamic_filters.display_df()

