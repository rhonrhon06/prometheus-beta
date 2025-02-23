import lzma
import os

def compress_xz(input_data, compression_level=6):
    """
    Compress data using XZ (LZMA2) compression algorithm.
    
    Args:
        input_data (bytes or str): Data to compress. 
            If str is provided, it will be encoded to UTF-8 bytes.
        compression_level (int, optional): Compression level from 0-9. 
            Defaults to 6 (medium compression).
    
    Returns:
        bytes: Compressed data in XZ format
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If compression level is out of range
    """
    # Validate compression level
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input type
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using LZMA
    return lzma.compress(input_data, preset=compression_level)

def decompress_xz(compressed_data):
    """
    Decompress XZ (LZMA2) compressed data.
    
    Args:
        compressed_data (bytes): Data compressed with XZ algorithm
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        lzma.LZMAError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using LZMA
    return lzma.decompress(compressed_data)