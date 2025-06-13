import os

MAX_CHARS_READ = 10000


def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    file_path_absolute = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path_absolute.startswith(working_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_path_absolute):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(file_path_absolute, "r") as file:
            file_content_string = file.read(MAX_CHARS_READ)
            is_remaining_content = file.read(1)

            if is_remaining_content != "":
                file_content_string += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )

            return file_content_string
    except Exception as error:
        return f"Error: {error}"
