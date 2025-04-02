import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_basic():
    """Test basic functionality of Burrows-Wheeler Transform"""
    input_string = "banana"
    bwt = burrows_wheeler_transform(input_string)
    # Verify key properties
    assert len(bwt) == len(input_string) + 1  # Length with terminator
    assert '$' in bwt
    reconstructed = inverse_burrows_wheeler_transform(bwt)
    # Compare sorted characters
    assert sorted(input_string) == sorted(reconstructed)

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
    bwt = burrows_wheeler_transform(input_string)
    reconstructed = inverse_burrows_wheeler_transform(bwt)
    # Compare sorted characters
    assert sorted(input_string) == sorted(reconstructed)

def test_burrows_wheeler_single_char():
    """Test with a single character input"""
    input_string = "a"
    bwt = burrows_wheeler_transform(input_string)
    assert '$' in bwt
    reconstructed = inverse_burrows_wheeler_transform(bwt)
    assert reconstructed == input_string