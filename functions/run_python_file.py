import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        
        # Determine the correct path to check
        # If file_path is already "calculator/main.py", use it as is.
        # If it's just "main.py", join it with "calculator/".
        if file_path.startswith(working_directory):
            check_path = file_path
        else:
            check_path = os.path.join(working_directory, file_path)
            
        abs_file_path = os.path.abspath(check_path)

        # 1. Security Check
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 2. Existence Check
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # 3. Extension Check
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # 4. Command building & Execution
        command = ["python", abs_file_path] # Use "python3" if on standard Ubuntu
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        # 5. Build Output String (Strictly matching test expectations)
        output_parts = []
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        output_parts.append(f"STDOUT:\n{result.stdout}")
        output_parts.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"