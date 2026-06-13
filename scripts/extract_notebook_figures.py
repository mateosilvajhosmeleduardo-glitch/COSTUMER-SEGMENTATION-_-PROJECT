"""Extract embedded PNG outputs from the project notebook.

This script does not generate new charts. It only reads the PNG outputs already stored
inside the executed notebook and saves them as files under assets/figures/.
"""

from __future__ import annotations

import base64
import nbformat
from pathlib import Path

NOTEBOOK = Path("notebooks/credit_card_customer_segmentation.ipynb")
OUTPUT_DIR = Path("assets/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

nb = nbformat.read(NOTEBOOK, as_version=4)
count = 0
for cell_index, cell in enumerate(nb.cells):
    if cell.cell_type != "code":
        continue
    for output_index, output in enumerate(cell.get("outputs", [])):
        data = output.get("data", {})
        if "image/png" not in data:
            continue
        count += 1
        file_path = OUTPUT_DIR / f"{count:02d}_notebook_cell_{cell_index}_output_{output_index}.png"
        file_path.write_bytes(base64.b64decode(data["image/png"]))

print(f"Extracted {count} figures from {NOTEBOOK}")
