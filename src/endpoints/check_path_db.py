from pathlib import Path

def check_path_permission(path):
    # Create a Path object from the given path
    path_obj = Path(path)
    
    # Check if the path exists
    if not path_obj.exists():
        return False,f"The path '{path}' does not exist."
    
    # Check if the path is a directory
    elif not path_obj.is_dir():
        return False, f"The path '{path}' is not a directory."
    
    # Check if we have write permission in the directory
    elif not path_obj.is_writable():
        return False, f"No write permission in the directory '{path}'."
    
    # If everything is fine, return True
    return True, None

# Example usage
# database_path = "D:\\address_book\\test.db"
# if check_path_permission(database_path):
#     print(f"Permission check passed for '{database_path}'.")
#     # Now you can proceed with creating the SQLite database in this directory
# else:
#     print(f"Permission check failed for '{database_path}'.")
    # Handle the case where permission check failed
