import os
import pandas as pd

data_dir= "data"
RAW_FILE="PSCompPars_2026.02.23_07.13.50.csv"
def load_exoplanet_data():
    file_path = os.path.join(data_dir, RAW_FILE)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file {file_path} not found.")
    df= pd.read_csv(file_path,comment="#")
    df=df[df['pl_bmasse'].notna()].copy()
    return df