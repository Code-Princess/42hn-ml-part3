import pandas as pd
from dagster import asset
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

from ml_pipeline.utils.eval_metrics import compute_eval_metrics

@asset
def eval_lin_reg(lin_reg_model: LinearRegression, test_data: tuple) -> dict:
    """

    Args:
        lin_reg_model:
        test_data:

    Returns: eval_metrics

    """
    X_test, y_test = test_data
    return compute_eval_metrics(lin_reg_model, X_test, y_test)

@asset
def eval_rand_forest(rand_forest_model: RandomForestRegressor, test_data: tuple) -> dict:
    """
    
    Args:
        rand_forest_model: 
        test_data: 

    Returns: eval_metrics

    """
    X_test, y_test = test_data
    return compute_eval_metrics(rand_forest_model, X_test, y_test)

@asset
def eval_XGBoost(XGBoost_model: XGBRegressor, test_data: tuple) -> dict:
    """
    
    Args:
        XGBoost_model: 
        test_data: 

    Returns: eval_metrics

    """
    X_test, y_test = test_data
    return compute_eval_metrics(XGBoost_model, X_test, y_test)



















