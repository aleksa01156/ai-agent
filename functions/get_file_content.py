import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        # 1. Path Validation (Security Guardrails)
        working_dir_abs = os.path.abspath(working_directory)
        # Normalize the path to handle ".." or absolute path injections
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Check if target is inside working directory
        if os.path.commonpath([working_dir_abs, target_file_path]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # 2. Check if the file exists and is a regular file
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # 3. Read the file with truncation logic
        with open(target_file_path, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS)
            
            # Check if there is more data left in the file
            if f.read(1):
                content += f'\n\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return content

    except Exception as e:
        return f"Error: {str(e)}"