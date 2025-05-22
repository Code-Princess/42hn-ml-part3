import pandas as pd
from dagster import asset
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

@asset
def train_and_test_data(bikes_features: pd.DataFrame) -> tuple:
    """

    Args:
        bikes_features:

    Returns: train and test data

    """
    X = bikes_features.drop(columns=['cnt'])
    y = bikes_features['cnt']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_train.shape, X_test.shape)
    return  X_train, X_test, y_train, y_test

@asset
def lin_reg_model(train_and_test_data: tuple) -> LinearRegression:
    """
    
    Args:
        split_data: 

    Returns: training model

    """
    X_train, X_test, y_train, y_test = train_and_test_data
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Linear Regression Model Trained")
    return model