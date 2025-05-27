import os
import pickle
from dagster import IOManager, io_manager, OutputContext, InputContext

class PickleIOManager(IOManager):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def handle_output(self, context: OutputContext, obj):
        # Compose file path based on step key and output name
        file_name = f"{context.step_key}_{context.name}.pkl"
        output_path = os.path.join(self.base_path, file_name)

        # Ensure directory exists
        os.makedirs(self.base_path, exist_ok=True)

        with open(output_path, "wb") as f:
            pickle.dump(obj, f)

        # Store file path in metadata for downstream
        context.add_output_metadata({"path": output_path})

    def load_input(self, context: InputContext):
        # Get the path from upstream metadata
        upstream_metadata = context.upstream_output.metadata
        input_path = upstream_metadata["path"]

        with open(input_path, "rb") as f:
            return pickle.load(f)

@io_manager(config_schema={"base_path": str})
def pickle_io_manager(init_context):
    return PickleIOManager(base_path=init_context.resource_config["base_path"])
