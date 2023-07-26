import importlib.util

def import_variable_from_file(filepath, variable_name):
    spec = importlib.util.spec_from_file_location("variable_module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, variable_name)

if __name__ == "__main__":
    filepath = "variable_load_2.py"
    variable_name = "a"

    a = import_variable_from_file(filepath, variable_name)
    print(a)
