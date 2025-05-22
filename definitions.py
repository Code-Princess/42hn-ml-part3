from dagster import Definitions, load_assets_from_package_module
import ml_pipeline.assets

defs = Definitions(
    assets=(
            load_assets_from_package_module(ml_pipeline.assets)
    )
)