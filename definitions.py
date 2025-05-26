import mlflow
from dagster import Definitions, load_assets_from_package_module
import ml_pipeline.assets
from ml_pipeline.resources.mlflow_resrc import mlflow_resrc

defs = Definitions(
    assets=load_assets_from_package_module(ml_pipeline.assets),
    resources={
        "mlflow_resrc": mlflow_resrc.configured({
        "tracking_uri": "http://localhost:5000",
        "experiment_name": "BikeSharing"
        })
    }
)