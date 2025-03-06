"""
Module for reading text file contents.

This module provides a function to read the contents of a text file 
with error handling and support for different file encodings.
"""

def read_text_file(file_path, encoding='utf-8'):
    """
    Read and return the contents of a text file.

    Args:
        file_path (str): Path to the text file to be read.
        encoding (str, optional): Encoding of the file. Defaults to 'utf-8'.

    Returns:
        str: Contents of the text file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to read the file.
        IOError: For other input/output related errors.
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read {file_path}.")
    except IOError as e:
        raise IOError(f"An error occurred while reading {file_path}: {str(e)}")