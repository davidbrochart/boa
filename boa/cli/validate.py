from jsonschema import validate
import json5 as json
import os

from rich.console import Console

console = Console()


def schema_dir():
    return os.path.join(os.path.dirname(__file__), "../../schemas")


test_obj = {
    "context": {"variable": 123},
    "package": {"name": "boa", "version": "0.1.0"},
    "source": [{"url": "http://github.com", "sha256": "123123123", "patches": []}],
}


def main():
    with open(os.path.join(schema_dir(), "recipe.v1.json")) as schema_in:
        schema = json.load(schema_in)
    validation_result = validate(instance=test_obj, schema=schema)

    if validation_result is None:
        console.print("[green]Validation OK![/green]")


if __name__ == "__main__":
    main()
