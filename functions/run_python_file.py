import os
import subprocess


def run_python_file(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    file_path_absolute = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path_absolute.startswith(working_dir_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(file_path_absolute):
        return f'Error: File "{file_path}" not found.'

    if file_path_absolute[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result_str = ""
        process = subprocess.run(
            ["python3", file_path_absolute],
            capture_output=True,
            timeout=30,
            cwd=working_dir_abs,
            text=True,
        )

        if process.stdout:
            result_str += f"STDOUT: {process.stdout}"
        if process.stderr:
            result_str += f"STDERR: {process.stderr}"
        if process.returncode != 0:
            result_str += f"Process exited with code {process.returncode}"

        if result_str != "":
            return result_str
        else:
            return "No output produiced."
    except Exception as error:
        return f"Error: executing Python file: {error}"
