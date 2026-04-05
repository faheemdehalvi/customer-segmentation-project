import os
import subprocess
import sys

# Install kagglehub if not already installed
try:
    import kagglehub
except ImportError:
    print("Installing kagglehub...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "kagglehub"])
    import kagglehub

import pandas as pd
import shutil

print("Downloading Online Retail dataset from Kaggle...")
# Download the dataset
path = kagglehub.dataset_download("vijayuv/onlineretail")
print(f"Dataset downloaded to: {path}")

# List files in the downloaded directory
print("\nFiles in downloaded dataset:")
for file in os.listdir(path):
    print(f"  - {file}")

# Find the CSV file
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
if csv_files:
    source_csv = os.path.join(path, csv_files[0])
    print(f"\nProcessing: {csv_files[0]}")
    
    # Load the dataset (using latin-1 encoding for special characters like £)
    df = pd.read_csv(source_csv, encoding='latin-1')
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
    # Save to project's data/raw folder
    dest_path = "data/raw/online_retail.csv"
    df.to_csv(dest_path, index=False)
    print(f"\n✅ Dataset saved to: {dest_path}")
    print(f"Total records: {len(df)}")
else:
    print("No CSV files found in the downloaded dataset!")
