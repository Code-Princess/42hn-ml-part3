import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def compute_eval_metrics(model, X_test, y_test) -> dict:
    y_preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_preds))
    mae = mean_absolute_error(y_test, y_preds)
    r2 = r2_score(y_test, y_preds)
    eval_metrics = {'rmse': rmse, 'mae': mae, 'r2': r2}
    print(eval_metrics)
    return eval_metrics