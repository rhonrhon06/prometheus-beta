import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert counting_sort(input_list) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert counting_sort(input_list) == [1, 2, 3, 4, 5]

def test_duplicate_elements():
    """Test sorting with multiple duplicate elements"""
    input_list = [4, 4, 4, 1, 1, 2, 2]
    assert counting_sort(input_list) == [1, 1, 2, 2, 4, 4, 4]

def test_zero_elements():
    """Test sorting a list with zero elements"""
    input_list = [0, 0, 0, 0]
    assert counting_sort(input_list) == [0, 0, 0, 0]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_non_integer_elements():
    """Test that a TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, 3, "4"])

def test_negative_numbers():
    """Test that a ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([1, 2, -3, 4])