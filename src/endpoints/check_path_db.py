from pathlib import Path
import os

def check_path_permission(path):
    # Create a Path object from the given path
    path_obj = Path(path)
    
    # Get the parent directory (folder) of the file
    folder_path = path_obj.parent
    
    # Check if the path exists
    if not folder_path.exists():
        return False,f"The path '{folder_path}' does not exist."
    
    # Check if the path is a directory
    if not folder_path.is_dir():
        return False, f"The path '{path}' is not a directory."
    
    return True, None

