import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_basic():
    """Test basic functionality of Burrows-Wheeler Transform"""
    input_string = "banana"
    result = burrows_wheeler_transform(input_string)
    # Actual result might vary based on stable sorting, but should be reconstructable
    assert inverse_burrows_wheeler_transform(result) == input_string

def test_burrows_wheeler_transform_properties():
    """Test that BWT preserves some key properties"""
    input_string = "banana"
    bwt = burrows_wheeler_transform(input_string)
    # BWT length should match input length
    assert len(bwt) == len(input_string) + 1
    # Should contain terminator
    assert '$' in bwt

def test_burrows_wheeler_empty_input():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform("")

def test_burrows_wheeler_invalid_input():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        burrows_wheeler_transform(123)

def test_inverse_burrows_wheeler_empty_input():
    """Test error handling for empty input in inverse transform"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        inverse_burrows_wheeler_transform("")

def test_inverse_burrows_wheeler_invalid_input():
    """Test error handling for non-string input in inverse transform"""
    with pytest.raises(TypeError, match="Input must be a string"):
        inverse_burrows_wheeler_transform(123)

def test_burrows_wheeler_complex_string():
    """Test with a more complex input string"""
    input_string = "mississippi"
    result = burrows_wheeler_transform(input_string)
    assert inverse_burrows_wheeler_transform(result) == input_string

def test_burrows_wheeler_single_char():
    """Test with a single character input"""
    input_string = "a"
    result = burrows_wheeler_transform(input_string)
    assert result == "a$"
    assert inverse_burrows_wheeler_transform(result) == input_string