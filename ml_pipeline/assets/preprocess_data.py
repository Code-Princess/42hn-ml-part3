import pandas as pd
from dagster import asset
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


@asset
def bikes_features(bikes_data: pd.DataFrame) -> pd.DataFrame:
    """

    Args:
        load_data: original data

    Returns: preprocessed data

    """
    numerical_features = ['temp', 'hum', 'windspeed']
    categorical_features = ['season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit']
    X = bikes_data[categorical_features + numerical_features]
    target = bikes_data['cnt']

    preprocessor = ColumnTransformer(transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ])
    X_preprocessed = preprocessor.fit_transform(X)
    cat_columns = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)
    all_columns = numerical_features + list(cat_columns)

    df_features = pd.DataFrame(X_preprocessed, columns=all_columns, index=bikes_data.index)
    df_features['cnt'] = target.values
    print(df_features.head())
    return df_features