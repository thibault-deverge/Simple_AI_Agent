import os


def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    file_path_absolute = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path_absolute.startswith(working_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working director'

    try:
        with open(file_path_absolute, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as error:
        return f"Error: {error}"
