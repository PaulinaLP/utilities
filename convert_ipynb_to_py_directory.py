import os
from nbconvert import PythonExporter
from nbformat import read


def convert_ipynb_to_py(ipynb_file, py_file):
    """
    Convert an IPython Notebook (.ipynb) file to a Python (.py) file.
    """
    with open(ipynb_file, 'r', encoding='utf-8') as nb_file:
        notebook = read(nb_file, as_version=4)

    python_exporter = PythonExporter()
    (body, resources) = python_exporter.from_notebook_node(notebook)

    with open(py_file, 'w', encoding='utf-8') as py_file:
        py_file.write(body)


def convert_all_ipynb_to_py(directory):
    """
    Convert all IPython Notebook (.ipynb) files in a directory and its subdirectories to Python (.py) files.
    """
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.ipynb'):
                print(file_name)

                ipynb_path = os.path.join(root, file_name)
                py_path = os.path.splitext(ipynb_path)[0] + '.py'
                convert_ipynb_to_py(ipynb_path, py_path)
                print(f"Converted: {os.path.relpath(ipynb_path, directory)} to {os.path.basename(py_path)}")
