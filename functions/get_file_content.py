import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):

    try: 
        root = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))
        root_with_sep = root + os.sep

        if not (target == root or target.startswith(root_with_sep)):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        

        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        #         file  operation  optional encoding
        with open(target, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS)
            return content

    except OSError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"