import pandas as pd
from dagster import asset, OpExecutionContext

@asset(config_schema={"file_path": str})
def bikes_data(context: OpExecutionContext) -> pd.DataFrame:
    """

    Returns: raw data

    """
    # file_path = 'bike_sharing_dataset/hour.csv'
    file_path = context.op_config["file_path"]
    data = pd.read_csv(file_path)
    print(data.head())
    context.log.info(f"Loaded data from {file_path}")
    return data

# @asset
# def bikes_data(context: OpExecutionContext) -> pd.DataFrame:
#     """
# 
#     Returns: raw data
# 
#     """
#     file_path = 'bike_sharing_dataset/hour.csv'
#     data = pd.read_csv(file_path)
#     print(data.head())
#     context.log.info(f"Loaded data from {file_path}")
#     return data