import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_basic():
    """Test basic functionality of Burrows-Wheeler Transform"""
    input_string = "banana"
    expected_bwt = "annb$aa"
    assert burrows_wheeler_transform(input_string) == expected_bwt

def test_burrows_wheeler_inverse():
    """Test that inverse transform recovers original string"""
    input_string = "banana"
    bwt = burrows_wheeler_transform(input_string)
    assert inverse_burrows_wheeler_transform(bwt) == input_string

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
    bwt = burrows_wheeler_transform(input_string)
    assert inverse_burrows_wheeler_transform(bwt) == input_string

def test_burrows_wheeler_single_char():
    """Test with a single character input"""
    input_string = "a"
    bwt = burrows_wheeler_transform(input_string)
    assert bwt == "a$"
    assert inverse_burrows_wheeler_transform(bwt) == input_string