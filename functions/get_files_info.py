import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # 4. Check if it's actually a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        # 5. Iterate through the items in the directory
        output_lines = []
        # listdir gives us just the names of items inside target_dir
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            
            # Get stats
            info = os.stat(item_path)
            size = info.st_size
            is_dir = os.path.isdir(item_path)
            
            # 6. Format the string according to the assignment
            output_lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
            
        return "\n".join(output_lines)

    except Exception as e:
        # Catch-all for any OS errors, permission denied, etc.
        return f"Error: {str(e)}"