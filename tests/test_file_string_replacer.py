"""
Tests for file string replacement functionality.
"""

import os
import pytest
import tempfile

from src.file_string_replacer import replace_string_in_file

def test_replace_string_basic():
    """Test basic string replacement."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello world, hello universe")
        temp_file.close()
        
        try:
            replacements = replace_string_in_file(temp_file.name, "hello", "hi")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
            
            assert replacements == 2
            assert content == "Hello world, hi universe"
        finally:
            os.unlink(temp_file.name)

def test_replace_string_case_sensitive():
    """Test case-sensitive replacement."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello HELLO hello")
        temp_file.close()
        
        try:
            replacements = replace_string_in_file(temp_file.name, "hello", "hi")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
            
            assert replacements == 1
            assert content == "Hello HELLO hi"
        finally:
            os.unlink(temp_file.name)

def test_replace_string_no_replacements():
    """Test when no replacements are made."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Original text")
        temp_file.close()
        
        try:
            replacements = replace_string_in_file(temp_file.name, "missing", "replacement")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
            
            assert replacements == 0
            assert content == "Original text"
        finally:
            os.unlink(temp_file.name)

def test_replace_with_empty_new_string():
    """Test replacement with an empty new string."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Remove this text completely")
        temp_file.close()
        
        try:
            replacements = replace_string_in_file(temp_file.name, "Remove", "")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
            
            assert replacements == 1
            assert content == " this text completely"
        finally:
            os.unlink(temp_file.name)

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("/path/to/nonexistent/file.txt", "old", "new")

def test_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        replace_string_in_file(123, "old", "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", 123, "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", "old", 123)

def test_empty_old_string():
    """Test handling of empty old string."""
    with pytest.raises(ValueError):
        replace_string_in_file("file.txt", "", "new")