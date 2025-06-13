import os


def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = "."

    try:
        working_dir_abs = os.path.abspath(working_directory)
        directory_dir_abs = os.path.abspath(os.path.join(working_directory, directory))

        if not directory_dir_abs.startswith(working_dir_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            if os.path.isdir(directory_dir_abs):
                result_str = ""
                contents = os.listdir(directory_dir_abs)

                for content in contents:
                    content_path = os.path.join(directory_dir_abs, content)

                    try:
                        result_str += f"- {content}: file_size={os.path.getsize(content_path)} bytes, is_dir={os.path.isdir(content_path)}\n"
                    except Exception as error:
                        result_str += (
                            f"- {content} file_size=Unknow bytes, is_dir=Unknow"
                        )
            else:
                return f'Error: "{directory}" is not a directory'

        return result_str
    except Exception as error:
        return f"Error: {error}"
