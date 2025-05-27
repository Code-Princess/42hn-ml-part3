import os
import json
from dagster import IOManager, io_manager, OutputContext, InputContext

class JsonIOManager(IOManager):
    def handle_output(self, context: OutputContext, obj):
        base_path = "storage"
        filename = f"{'_'.join(context.asset_key.path)}.json"
        output_path = os.path.join(base_path, filename)

        os.makedirs(base_path, exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(obj, f)

        context.log.info(f"Stored JSON output to {output_path}")

    def load_input(self, context: InputContext):
        base_path = "storage"
        filename = f"{'_'.join(context.asset_key.path)}.json"
        input_path = os.path.join(base_path, filename)

        with open(input_path, "r") as f:
            return json.load(f)


@io_manager
def json_io_manager():
    return JsonIOManager()
