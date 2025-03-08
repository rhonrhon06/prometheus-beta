import pytest
from src.substring_reversal import reverse_substring

def test_basic_substring_reversal():
    """Test basic substring reversal"""
    assert reverse_substring("hello world", 0, 5) == "olleh world"
    assert reverse_substring("hello world", 6, 11) == "hello dlrow"

def test_partial_substring_reversal():
    """Test reversing a portion of the string"""
    assert reverse_substring("python programming", 7, 17) == "python gnimmargorp"

def test_single_character_substring():
    """Test reversing a single character substring"""
    assert reverse_substring("abcde", 2, 3) == "abcde"

def test_full_string_reversal():
    """Test reversing the entire string"""
    assert reverse_substring("reverse", 0, 7) == "esrever"

def test_empty_string():
    """Test empty string handling"""
    assert reverse_substring("", 0, 0) == ""

def test_invalid_indices_raises_error():
    """Test that invalid indices raise ValueError"""
    with pytest.raises(ValueError, match="Invalid substring indices"):
        reverse_substring("test", -1, 4)
    with pytest.raises(ValueError, match="Invalid substring indices"):
        reverse_substring("test", 0, 5)
    with pytest.raises(ValueError, match="Invalid substring indices"):
        reverse_substring("test", 3, 2)

def test_invalid_input_type():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_substring(123, 0, 3)