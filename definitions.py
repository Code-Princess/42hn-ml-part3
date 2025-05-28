from dagster import Definitions, load_assets_from_package_module, define_asset_job
import ml_pipeline.assets
from ml_pipeline.io_managers.DataFrameIOManager import DataFrameIOManagerFactory
from ml_pipeline.io_managers.JsonIOManager import json_io_manager
from ml_pipeline.io_managers.PickleIOManager import pickle_io_manager
from ml_pipeline.resources.mlflow_resrc import mlflow_resrc

bike_job = define_asset_job("bike_job", selection="*")

defs = Definitions(
    assets=load_assets_from_package_module(ml_pipeline.assets),
    jobs=[bike_job],
    resources={
        # "mlflow_resrc": mlflow_resrc.configured({
        #     "tracking_uri": "http://localhost:5000",
        #     "experiment_name": "BikeSharing"
        # }),
        "mlflow_resrc": mlflow_resrc,
        "io_manager": DataFrameIOManagerFactory(base_path="storage/data"),  # base_path set via YAML
        "pickle_io_manager": pickle_io_manager,      # ✅ YAML config applies
        "json_io_manager": json_io_manager,          # ✅ YAML config applies
    }
)
