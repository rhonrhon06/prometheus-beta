import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_ascending():
    """Test finding missing numbers in an ascending array."""
    assert find_missing_numbers([1, 3, 5, 7]) == [2, 4, 6]

def test_missing_numbers_descending():
    """Test finding missing numbers in a descending array."""
    assert find_missing_numbers([7, 5, 3, 1]) == [6, 4, 2]

def test_missing_numbers_no_gaps():
    """Test array with no missing numbers."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_missing_numbers_large_gaps():
    """Test array with large gaps between numbers."""
    assert find_missing_numbers([1, 10]) == list(range(2, 10))

def test_large_range_single_missing():
    """Test large range with a single missing number."""
    arr = [x for x in range(1, 11) if x != 5]
    assert find_missing_numbers(arr) == [5]

def test_invalid_input_empty_list():
    """Test handling of empty list."""
    with pytest.raises(ValueError):
        find_missing_numbers([])

def test_invalid_input_non_positive():
    """Test handling of non-positive integers."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, -3, 4])

def test_single_element_array():
    """Test array with a single element."""
    assert find_missing_numbers([5]) == list(range(1, 5))

def test_min_max_order():
    """Test that the order of min and max values is preserved."""
    ascending = find_missing_numbers([1, 3, 5, 7])
    descending = find_missing_numbers([7, 5, 3, 1])
    assert ascending == [2, 4, 6]
    assert descending == [6, 4, 2]