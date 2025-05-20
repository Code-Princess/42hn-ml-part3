import pandas as pd
from dagster import asset

@asset
def load_data() -> pd.DataFrame:
    file_path = '../../bike_sharing_dataset/hour.csv'
    data = pd.read_csv(file_path)
    return data
