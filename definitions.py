import mlflow
from dagster import Definitions, load_assets_from_package_module
import ml_pipeline.assets
from ml_pipeline.io_managers.DataFrameIOManager import DataFrameIOManager, DataFrameIOManagerFactory
from ml_pipeline.io_managers.JsonIOManager import json_io_manager
from ml_pipeline.io_managers.PickleIOManager import pickle_io_manager
from ml_pipeline.resources.mlflow_resrc import mlflow_resrc

defs = Definitions(
    assets=load_assets_from_package_module(ml_pipeline.assets),
    resources={
        "mlflow_resrc": mlflow_resrc.configured({
        "tracking_uri": "http://localhost:5000",
        "experiment_name": "BikeSharing"
        }),
        "io_manager": DataFrameIOManagerFactory(base_path="storage/data"),
        "pickle_io_manager": pickle_io_manager.configured({
            "base_path": "storage/model_pickles"
        }),
        "json_io_manager": json_io_manager.configured({
            "base_path": "storage/evals"
        }),
    }
)