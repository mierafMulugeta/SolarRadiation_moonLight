import pandas as pd
import numpy as np

# Function to load data from an Excel file
def load_data(file_path):
    return pd.read_excel(file_path)

# Function to clean data: Handle missing values and outliers
def clean_data(data):
    # Fill missing values with the median
    data.fillna(data.median(), inplace=True)
    
    # Replace negative values with NaN (for columns where negative values shouldn't exist)
    columns_to_check = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
    data[columns_to_check] = data[columns_to_check].apply(lambda x: x.where(x >= 0, np.nan))
    
    return data
