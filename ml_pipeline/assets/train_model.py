import pandas as pd
from dagster import asset, AssetOut, multi_asset, Output, OpExecutionContext
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBRegressor

@multi_asset(
    outs={"train_data": AssetOut(),
          "test_data": AssetOut()
          }
)
def split_data(bikes_features: pd.DataFrame):
    X = bikes_features.drop(columns=['cnt'])
    y = bikes_features['cnt']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    train_data = (X_train, y_train)
    test_data = (X_test, y_test)
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    yield Output(train_data, output_name="train_data")
    yield Output(test_data, output_name="test_data")

@asset(required_resource_keys={"mlflow_resrc"})
def lin_reg_model(context: OpExecutionContext, train_data: tuple) -> LinearRegression:
    """

    Args:
        context:
        train_data:

    Returns: linear regression model

    """
    mlflow = context.resources.mlflow_resrc
    X_train, y_train = train_data
    with mlflow.start_run(run_name="Linear Regression Training"):
        model = LinearRegression()
        model.fit(X_train, y_train)
        print("Linear Regression Model Trained")
        context.log.info("Linear Regression Model Trained")
    return model

@asset(required_resource_keys={"mlflow_resrc"})
def rand_forest_model(context: OpExecutionContext, train_data: tuple) -> RandomForestRegressor:
    """

    Args:
        context:
        train_data:

    Returns: random forest regression model

    """
    mlflow = context.resources.mlflow_resrc
    X_train, y_train = train_data
    with mlflow.start_run(run_name="Random Forest Regression Training"):
        model = RandomForestRegressor(random_state=42)
        param_grid = {
            'n_estimators': [100, 200],
            'max_depth': [10, 20],
        }
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
        grid_search.fit(X_train, y_train)
        print("Random Forest Model Trained")
        context.log.info("Random Forest Model Trained")
    return grid_search.best_estimator_

@asset(required_resource_keys={"mlflow_resrc"})
def XGBoost_model(context: OpExecutionContext, train_data: tuple) -> XGBRegressor:
    """
    
    Args:
        context: 
        train_data: 

    Returns: XGBoost regression model

    """
    mlflow = context.resources.mlflow_resrc
    X_train, y_train = train_data
    with mlflow.start_run(run_name="XGBoost Regression Training"):
        model = XGBRegressor(random_state=42)
        # XGBoost with GridSearch
        param_grid = {
            'n_estimators': [100, 200],
            'learning_rate': [0.05, 0.1],
            'max_depth': [3, 5]
        }
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
        grid_search.fit(X_train, y_train)
        print("XGBoost Model Trained")
        context.log.info("XGBoost Model Trained")
    return grid_search.best_estimator_