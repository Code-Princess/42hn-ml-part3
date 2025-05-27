import os
import pandas as pd
from dagster import InputContext, OutputContext
from dagster import ConfigurableIOManagerFactory, IOManager

class DataFrameIOManager(IOManager):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def handle_output(self, context: OutputContext, obj: pd.DataFrame):
        output_path = os.path.join(self.base_path, f"{context.asset_key.path[-1]}.csv")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        obj.to_csv(output_path, index=False)
        context.log.info(f"Saved dataframe to {output_path}")

    def load_input(self, context: InputContext) -> pd.DataFrame:
        input_path = os.path.join(self.base_path, f"{context.asset_key.path[-1]}.csv")
        context.log.info(f"Loading dataframe from {input_path}")
        return pd.read_csv(input_path)


class DataFrameIOManagerFactory(ConfigurableIOManagerFactory):
    base_path: str

    def create_io_manager(self, context):
        return DataFrameIOManager(base_path=self.base_path)
