import pandas as pd

def load_data(file_path):
    """
    Load customer data from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    DataFrame: A pandas DataFrame containing the customer data.
    """
    data = pd.read_csv(file_path)
    return data

def clean_data(df):
    """
    Clean the customer DataFrame by handling missing values and removing cancelled orders.
    
    Parameters:
    df (DataFrame): The DataFrame containing customer data.
    
    Returns:
    DataFrame: A cleaned pandas DataFrame.
    """
    # Drop rows with missing values
    df = df.dropna()
    
    # Remove cancelled orders (assuming 'OrderStatus' is a column in the dataset)
    df = df[df['OrderStatus'] != 'Cancelled']
    
    return df

def preprocess_data(file_path):
    """
    Load and clean the customer data.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    DataFrame: A cleaned pandas DataFrame ready for analysis.
    """
    df = load_data(file_path)
    cleaned_df = clean_data(df)
    return cleaned_df