import pandas as pd
from dagster import asset
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

from ml_pipeline.utils.eval_metrics import compute_eval_metrics

@asset(io_manager_key="json_io_manager")
def eval_lin_reg(lin_reg_model: LinearRegression, test_data: pd.DataFrame) -> dict:
    """
    
    Args:
        lin_reg_model: 
        test_data: 

    Returns: metrics

    """
    # Separate features and target from the combined DataFrame
    X_test = test_data.drop(columns=['cnt'])
    y_test = test_data['cnt']
    return compute_eval_metrics(lin_reg_model, X_test, y_test)

@asset(io_manager_key="json_io_manager")
def eval_rand_forest(rand_forest_model: RandomForestRegressor, test_data: pd.DataFrame) -> dict:
    """

    Args:
        rand_forest_model:
        test_data:

    Returns: metrics

    """
    # Separate features and target from the combined DataFrame
    X_test = test_data.drop(columns=['cnt'])
    y_test = test_data['cnt']
    return compute_eval_metrics(rand_forest_model, X_test, y_test)

@asset(io_manager_key="json_io_manager")
def eval_XGBoost(XGBoost_model: XGBRegressor, test_data: pd.DataFrame) -> dict:
    """
    
    Args:
        XGBoost_model: 
        test_data: 

    Returns: metrics

    """
    # Separate features and target from the combined DataFrame
    X_test = test_data.drop(columns=['cnt'])
    y_test = test_data['cnt']
    return compute_eval_metrics(XGBoost_model, X_test, y_test)



















