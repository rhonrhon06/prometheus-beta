import os
import pytest
import tempfile
import shutil

from src.file_counter import count_files_in_directory

def test_count_files_in_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert count_files_in_directory(temp_dir) == 0

def test_count_files_with_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        for i in range(5):
            open(os.path.join(temp_dir, f'testfile_{i}.txt'), 'w').close()
        
        assert count_files_in_directory(temp_dir) == 5

def test_count_files_ignores_subdirectories():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files and a subdirectory with a file
        for i in range(3):
            open(os.path.join(temp_dir, f'testfile_{i}.txt'), 'w').close()
        
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        open(os.path.join(temp_dir, 'subdir', 'subfile.txt'), 'w').close()
        
        assert count_files_in_directory(temp_dir) == 3

def test_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        count_files_in_directory('/path/to/nonexistent/directory')

def test_file_instead_of_directory():
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            count_files_in_directory(temp_file.name)

def test_normalize_path_with_trailing_slash():
    with tempfile.TemporaryDirectory() as temp_dir:
        open(os.path.join(temp_dir, 'testfile.txt'), 'w').close()
        
        # Test with and without trailing slash
        assert count_files_in_directory(temp_dir) == count_files_in_directory(temp_dir + '/')