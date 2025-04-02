import os
import pytest
from src.file_search import search_string_in_file

def test_search_string_in_file():
    # Create a test file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write("Hello world\n")
        f.write("This is a test file\n")
        f.write("Hello again\n")
        f.write("Another line with Hello\n")

    try:
        # Test finding a string
        results = search_string_in_file(test_file_path, 'Hello')
        assert results == [1, 3, 4], "Should find 'Hello' on lines 1, 3, and 4"

        # Test case sensitivity
        results = search_string_in_file(test_file_path, 'hello')
        assert results == [], "Should be case-sensitive"

        # Test string not found
        results = search_string_in_file(test_file_path, 'Python')
        assert results == [], "Should return empty list when string not found"

        # Test full line match
        results = search_string_in_file(test_file_path, 'This is a test file')
        assert results == [2], "Should find exact line match"

    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_search_invalid_inputs():
    # Test file not found
    with pytest.raises(FileNotFoundError):
        search_string_in_file('nonexistent_file.txt', 'test')

    # Test invalid file_path type
    with pytest.raises(TypeError):
        search_string_in_file(123, 'test')

    # Test invalid search_string type
    with pytest.raises(TypeError):
        search_string_in_file('tests/test_file.txt', 123)

def test_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as f:
        pass

    try:
        # Test searching in empty file
        results = search_string_in_file(test_file_path, 'test')
        assert results == [], "Should return empty list for empty file"
    finally:
        # Clean up test file
        os.remove(test_file_path)