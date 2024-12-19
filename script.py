import ast

def get_classes_and_functions(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    classes = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Get all function names within the class
            functions = [
                n.name for n in node.body if isinstance(n, ast.FunctionDef)
            ]
            classes[node.name] = functions
    return classes

# Example usage:
file_path = "std/io.py"  # Replace with the path to your file
classes_and_functions = get_classes_and_functions(file_path)
print(classes_and_functions)
for cls, funcs in classes_and_functions.items():
    print(f"Class '{cls}' has functions: {funcs}")