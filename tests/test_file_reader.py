"""
Unit tests for the file_reader module.

This module contains comprehensive tests for the read_text_file function,
covering various scenarios and edge cases.
"""

import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_existing_file():
    """Test reading contents of an existing text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_read_non_existent_file():
    """Test reading a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_text_file("/path/to/non/existent/file.txt")

def test_read_file_with_different_encoding():
    """Test reading a file with a specific encoding."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='latin-1', delete=False) as temp_file:
        temp_file.write("Héllo, wörld!")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name, encoding='latin-1')
            assert content == "Héllo, wörld!"
        finally:
            os.unlink(temp_file.name)

def test_read_file_with_invalid_encoding():
    """Test reading a file with an invalid encoding raises an error."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Some content")
        temp_file.close()
        
        try:
            with pytest.raises(LookupError):
                read_text_file(temp_file.name, encoding='invalid_encoding')
        finally:
            os.unlink(temp_file.name)