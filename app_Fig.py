#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:27:06 2024

@author: charlesbeck
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('bquxjob_1398a98e_1939337331a.csv')
# Streamlit App
st.title("Log Volume vs Percentage of Total Volume")

# Upload CSV File
#uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

#if uploaded_file is not None:
    # Read the CSV file
#    data = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
st.write("Preview of the Data:")
st.dataframe(data)
    
    # Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['log_volume'], data['percentage_of_total_volume'])
ax.set_xlabel("Log Volume")
ax.set_ylabel("Percentage of Total Volume")
ax.set_title("Log Volume vs Percentage of Total Volume")
ax.grid(True)
    
    # Display the plot in Streamlit
st.pyplot(fig)
