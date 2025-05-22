import numpy as np
from dagster import asset
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

@asset
def eval_metrics(lin_reg_model: LinearRegression, train_and_test_data: tuple) -> dict:
    """
    
    Args:
        lin_reg_model: 
        train_and_test_data: 

    Returns: {'rmse': rmse, 'mae': mae, 'r2': r2}

    """
    X_train, X_test, y_train, y_test = train_and_test_data
    y_preds = lin_reg_model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_preds))
    mae = mean_absolute_error(y_test, y_preds)
    r2 = r2_score(y_test, y_preds)
    eval_metrics = {'rmse': rmse, 'mae': mae, 'r2': r2}
    print(eval_metrics)
    return eval_metrics
