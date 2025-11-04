## Change to the current directory
import os
from pathlib import Path
wd = str(Path.cwd()) + "\\"
print(f"Working directory: {wd}")

## test_data_loader.py
pip install --no-cache-dir git+https://github.com/ElvisCasco/process_data.git