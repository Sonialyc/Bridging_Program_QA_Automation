import os
import sys

# Get the path of the parent directory of the current file (i.e., this file)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Insert the project root directory into the beginning of the Python path
sys.path.insert(0, project_root)
