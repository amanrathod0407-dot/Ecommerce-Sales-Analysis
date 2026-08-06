import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    # Base paths check
    possible_paths = [
        os.path.join("..", "data", "raw", "SampleSuperstore.csv"),
        os.path.join("data", "raw", "SampleSuperstore.csv"),
        "SampleSuperstore.csv"
    ]
    
    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break
            
    if not file_path:
        st.error("Dataset Error: `SampleSuperstore.csv` nahi mila. Data path check karein!")
        st.stop()

    # UTF-8 decoding issue fix karne ke liye encoding parameters add kiye hain
    try:
        df = pd.read_csv(file_path, encoding='windows-1252')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin1')
    
    # Cleaning & Processing
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['Year'] = df['Order Date'].dt.year
        df['Month_Year'] = df['Order Date'].dt.to_period('M').astype(str)
    
    return df