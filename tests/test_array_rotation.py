import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to array length"""
    assert rotate_array([1, 2, 3], 3) == [1, 2, 3]

def test_empty_array():
    """Test rotation of empty array"""
    assert rotate_array([], 5) == []

def test_zero_rotation():
    """Test rotation of 0 positions"""
    assert rotate_array([1, 2, 3], 0) == [1, 2, 3]

def test_large_rotation():
    """Test rotation larger than array length"""
    assert rotate_array([1, 2, 3, 4], 6) == [3, 4, 1, 2]

def test_rotation_type_error():
    """Test error for non-integer rotation amount"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_input_type_error():
    """Test error for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)

def test_negative_rotation():
    """Test error for negative rotation"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array([1, 2, 3], -1)

def test_single_element_array():
    """Test rotation of single-element array"""
    assert rotate_array([1], 5) == [1]