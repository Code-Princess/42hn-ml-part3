import pandas as pd
from dagster import asset

@asset
def bikes_data() -> pd.DataFrame:
    """
    
    Returns: raw data

    """
    file_path = 'bike_sharing_dataset/hour.csv'
    data = pd.read_csv(file_path)
    print(data.head())
    return data
