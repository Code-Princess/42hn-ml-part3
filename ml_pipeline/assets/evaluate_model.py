from dagster import asset
from sklearn.linear_model import LinearRegression
from ml_pipeline.utils.eval_metrics import compute_eval_metrics

@asset
def eval_lin_reg(lin_reg_model: LinearRegression, test_data: tuple) -> dict:
    """
    
    Args:
        lin_reg_model: 
        train_and_test_data: 

    Returns: {'rmse': rmse, 'mae': mae, 'r2': r2}

    """
    _, X_test, _, y_test = test_data
    return compute_eval_metrics(lin_reg_model, test_data)


















