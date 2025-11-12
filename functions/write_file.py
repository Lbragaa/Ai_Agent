

import os


def write_file(working_directory, file_path, content):
    try:
        root = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        root_sep = root + os.sep
        if not (target == root or target.startswith(root_sep)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(target):
            os.makedirs(os.path.dirname(target), exist_ok=True)
        
        with open(target, 'w') as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except OSError as e:
        return f'Error: {str(e)}'
    except Exception as e:
        return f'Error: {str(e)}'