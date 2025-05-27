import os
import json
from dagster import IOManager, io_manager, OutputContext, InputContext

class JsonIOManager(IOManager):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def handle_output(self, context: OutputContext, obj):
        filename = f"{'_'.join(context.asset_key.path)}.json"
        output_path = os.path.join(self.base_path, filename)

        os.makedirs(self.base_path, exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(obj, f)

        context.log.info(f"Stored JSON output to {output_path}")

    def load_input(self, context: InputContext):
        filename = f"{'_'.join(context.asset_key.path)}.json"
        input_path = os.path.join(self.base_path, filename)

        with open(input_path, "r") as f:
            return json.load(f)


@io_manager(config_schema={"base_path": str})
def json_io_manager(init_context):
    base_path = init_context.resource_config["base_path"]
    return JsonIOManager(base_path=base_path)
