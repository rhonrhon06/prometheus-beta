import pytest
from src.even_number_processor import remove_even_numbers_and_sum

def test_remove_even_numbers_and_sum_basic():
    """Test basic functionality with mixed even and odd numbers."""
    assert remove_even_numbers_and_sum([1, 2, 3, 4, 5, 6]) == 12

def test_remove_even_numbers_and_sum_only_even():
    """Test with only even numbers."""
    assert remove_even_numbers_and_sum([2, 4, 6, 8]) == 20

def test_remove_even_numbers_and_sum_only_odd():
    """Test with only odd numbers."""
    assert remove_even_numbers_and_sum([1, 3, 5, 7]) == 0

def test_remove_even_numbers_and_sum_empty_list():
    """Test with an empty list."""
    assert remove_even_numbers_and_sum([]) == 0

def test_remove_even_numbers_and_sum_negative_numbers():
    """Test with negative numbers."""
    assert remove_even_numbers_and_sum([-1, -2, 3, 4, -5, 6]) == -2 + 4 + 6

def test_remove_even_numbers_and_sum_invalid_input_non_list():
    """Test invalid input (non-list)."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_even_numbers_and_sum("not a list")

def test_remove_even_numbers_and_sum_invalid_input_non_integers():
    """Test invalid input (non-integers in list)."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_even_numbers_and_sum([1, 2, "3", 4])