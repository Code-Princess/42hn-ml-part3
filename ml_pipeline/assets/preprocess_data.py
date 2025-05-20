import pandas as pd
from dagster import asset
from sklearn.preprocessing import StandardScaler


@asset
def preprocess_data(load_data: pd.DataFrame) -> pd.DataFrame:
    target = load_data['cnt']
    features = load_data.drop(['cnt', 'instant', 'dteday', 'casual', 'registered'], axis=1)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    df_features = pd.DataFrame(scaled_features, columns=features.columns)
    df_features['cnt'] = target.values
    return df_features