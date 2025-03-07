import os
import gzip
import pytest
import shutil
from src.file_compressor import compress_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = "This is a test file for compression."
    test_file = tmp_path / "sample.txt"
    test_file.write_text(sample_content)
    return str(test_file)

def test_compress_file_default_output(sample_file, tmp_path):
    """Test compression with default output path"""
    compressed_path = compress_file(sample_file)
    
    # Check compressed file exists
    assert os.path.exists(compressed_path)
    assert compressed_path == sample_file + '.gz'
    
    # Verify content can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        decompressed_content = f.read()
    
    with open(sample_file, 'r') as f:
        original_content = f.read()
    
    assert decompressed_content == original_content

def test_compress_file_custom_output(sample_file, tmp_path):
    """Test compression with custom output path"""
    custom_output = str(tmp_path / "compressed_custom.gz")
    compressed_path = compress_file(sample_file, custom_output)
    
    # Check compressed file exists at custom path
    assert os.path.exists(compressed_path)
    assert compressed_path == custom_output
    
    # Verify content can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        decompressed_content = f.read()
    
    with open(sample_file, 'r') as f:
        original_content = f.read()
    
    assert decompressed_content == original_content

def test_compress_nonexistent_file():
    """Test compression of non-existent file"""
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/nonexistent/file.txt')

def test_compress_directory(tmp_path):
    """Test attempting to compress a directory"""
    with pytest.raises(IsADirectoryError):
        compress_file(str(tmp_path))

def test_compress_large_file(sample_file, tmp_path):
    """Test compression of a larger file"""
    # Create a larger file
    large_file = str(tmp_path / "large_sample.txt")
    with open(large_file, 'w') as f:
        f.write("Test content " * 10000)
    
    compressed_path = compress_file(large_file)
    
    # Check compressed file exists
    assert os.path.exists(compressed_path)
    
    # Verify content can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        decompressed_content = f.read()
    
    with open(large_file, 'r') as f:
        original_content = f.read()
    
    assert decompressed_content == original_content