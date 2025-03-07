import gzip
import os
import shutil

def compress_file(input_path, output_path=None):
    """
    Compress a file using gzip compression.

    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, defaults to input_path + '.gz'

    Returns:
        str: Path to the compressed file

    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
        IsADirectoryError: If input_path is a directory instead of a file
        ValueError: If input_path is empty or None
    """
    # Validate input path
    if not input_path:
        raise ValueError("Input path cannot be empty or None")
    
    # Validate input file exists and is a file
    input_path = os.path.abspath(input_path)
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Input path must be a file, not a directory: {input_path}")

    # Determine output path if not provided
    if output_path is None:
        output_path = input_path + '.gz'
    else:
        output_path = os.path.abspath(output_path)

    try:
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Open input file for reading
        with open(input_path, 'rb') as f_in:
            # Open output file for gzip compression
            with gzip.open(output_path, 'wb') as f_out:
                # Copy contents with buffering
                shutil.copyfileobj(f_in, f_out)
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to compress {input_path}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error during file compression: {str(e)}")