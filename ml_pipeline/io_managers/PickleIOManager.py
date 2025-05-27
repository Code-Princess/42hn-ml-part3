import os
import pickle
from dagster import IOManager, io_manager, OutputContext, InputContext

class PickleIOManager(IOManager):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def handle_output(self, context: OutputContext, obj):
        file_name = f"{'_'.join(context.asset_key.path)}.pkl"
        output_path = os.path.join(self.base_path, file_name)

        os.makedirs(self.base_path, exist_ok=True)

        with open(output_path, "wb") as f:
            pickle.dump(obj, f)

        context.log.info(f"Stored Pickle output to {output_path}")

    def load_input(self, context: InputContext):
        file_name = f"{'_'.join(context.asset_key.path)}.pkl"
        input_path = os.path.join(self.base_path, file_name)

        with open(input_path, "rb") as f:
            return pickle.load(f)


@io_manager(config_schema={"base_path": str})
def pickle_io_manager(init_context):
    return PickleIOManager(base_path=init_context.resource_config["base_path"])
