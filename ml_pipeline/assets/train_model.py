import pandas as pd
from dagster import asset
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBRegressor


@asset
def train_data(bikes_features: pd.DataFrame) -> tuple:
    """

    Args:
        bikes_features:

    Returns: train data

    """
    X = bikes_features.drop(columns=['cnt'])
    y = bikes_features['cnt']
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_train.shape)
    return  X_train, _, y_train, _

@asset
def test_data(bikes_features: pd.DataFrame) -> tuple:
    """

    Args:
        bikes_features:

    Returns: test data

    """
    X = bikes_features.drop(columns=['cnt'])
    y = bikes_features['cnt']
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_test.shape)
    return  _, X_test, _, y_test

@asset
def lin_reg_model(train_data: tuple) -> LinearRegression:
    """
    
    Args:
        split_data: 

    Returns: linear regression model

    """
    X_train, _, y_train, _ = train_data
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Linear Regression Model Trained")
    return model

@asset
def rand_forest_model(train_data: tuple) -> RandomForestRegressor:
    """

    Args:
        train_data: 

    Returns: random forest model

    """
    X_train, _, y_train, _ = train_data
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

    Returns: XGBoost model

    """
    X_train, _, y_train, _ = train_data
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