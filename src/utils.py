def load_data(file_path):
    import pandas as pd
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def save_data(data, file_path):
    """Save DataFrame to a CSV file."""
    data.to_csv(file_path, index=False)

def summarize_data(data):
    """Return a summary of the DataFrame."""
    return {
        'shape': data.shape,
        'columns': data.columns.tolist(),
        'dtypes': data.dtypes.astype(str).to_dict(),
        'missing_values': data.isnull().sum().to_dict(),
        'head': data.head().to_dict(orient='records')
    }

def transform_data(data, transformations):
    """Apply a series of transformations to the DataFrame."""
    for column, func in transformations.items():
        data[column] = func(data[column])
    return data

def get_summary_statistics(data):
    """Return summary statistics of the DataFrame."""
    return data.describe(include='all').to_dict()