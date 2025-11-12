import os

def get_files_info(working_directory, directory = "."):

    try: 
        
        root = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, directory))

        root_with_sep = root + os.sep
        if not (target == root or target.startswith(root_with_sep)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target):
            return f'Error: "{target}" is not a directory'

        names = os.listdir(target) # getting the file/folder names in the target directory

        #preparing each line
        lines = []
        for name in names:
            p = os.path.join(target, name) # getting the full path of each file/folder

            #getting file_size:

            size = os.path.getsize(p) 
            is_dir = os.path.isdir(p)

            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        
        return "\n".join(lines)
    
    except OSError as e:
        return f"Error: {e}"
    
    except Exception as e:
        return f"Error: {e}"
    
# this is the format we are looking for:

# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False