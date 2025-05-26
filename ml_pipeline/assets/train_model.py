import pandas as pd
from dagster import asset, AssetOut, multi_asset, Output
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBRegressor

# @multi_asset(
#     outs={"X_train": AssetOut(),
#           "X_test": AssetOut(),
#           "y_train": AssetOut(),
#           "y_test": AssetOut()
#           }
# )
# def split_data(bikes_features: pd.DataFrame):
#     X = bikes_features.drop(columns=['cnt'])
#     y = bikes_features['cnt']
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     print("X_train shape:", X_train.shape)
#     print("X_test shape:", X_test.shape)
#     yield Output(X_train, output_name="X_train")
#     yield Output(X_test, output_name="X_test")
#     yield Output(y_train, output_name="y_train")
#     yield Output(y_test, output_name="y_test")

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

@asset
def lin_reg_model(train_data: tuple) -> LinearRegression:
    """
    
    Args:
        train_data: 

    Returns: linear regression model

    """
    X_train, y_train = train_data
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Linear Regression Model Trained")
    return model

@asset
def rand_forest_model(train_data: tuple) -> RandomForestRegressor:
    """

    Args:
        train_data: 

    Returns: random forest regression model

    """
    X_train, y_train = train_data
    model = RandomForestRegressor(random_state=42)
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20],
    }
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
    grid_search.fit(X_train, y_train)
    print("Random Forest Model Trained")
    return grid_search.best_estimator_

@asset
def XGBoost_model(train_data: tuple) -> XGBRegressor:
    """

    Args:
        train_data:

    Returns: XGBoost regression model

    """
    X_train, y_train = train_data
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
    return grid_search.best_estimator_