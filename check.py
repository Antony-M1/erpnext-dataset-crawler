"""
    README:
    
    This file is basically used to check the all file format stored in the `temp` folder is correct or not.
    To run this file using this command.
    
    ```py
    python check.py
    ```
"""

import json
import traceback
import os


def check_jsonl_files(file_bath):
    """
        This funtion checkes the `.jsonl` file type and the order is correct.
    """
    
    with open(file_bath, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                # Parse each line as JSON data
                data = json.loads(line)
            except:
                traceback.print_exc(line_number, line_number, file_bath)
                raise ("Data error: " + line_number)
    print("All File Okay ✅✅✅")


# Path to the folder containing JSONL files
folder_path = "./temp"

# Get the file paths of all .jsonl files in the folder
jsonl_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".jsonl")]

# Print the file paths
for jsonl_file in jsonl_files:
    check_jsonl_files(jsonl_file)
