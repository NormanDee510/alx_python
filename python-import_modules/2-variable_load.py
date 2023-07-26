import importlib.util

def import_variable_from_file(filepath, variable_name):
    spec = importlib.util.spec_from_file_location("variable_module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, variable_name):
        return getattr(module, variable_name)
    else:
        return None

if __name__ == "__main__":
    filepath = "variable_load_2.py"
    variable_name = "a"

    a = import_variable_from_file(filepath, variable_name)
    if a is not None:
        print(f"a = {a}")
    else:
        print(f"a missing")
