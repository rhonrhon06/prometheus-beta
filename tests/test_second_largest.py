import pytest
from src.second_largest import find_second_largest

def test_normal_array():
    """Test finding second largest in a normal array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_with_duplicates():
    """Test finding second largest with duplicate elements."""
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([5, 5, 7, 7, 9, 9]) == 7

def test_negative_numbers():
    """Test finding second largest with negative numbers."""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([-10, 0, -5, 5, 10]) == 5

def test_error_cases():
    """Test error cases."""
    # Empty array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])
    
    # Single element array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])
    
    # Array with only duplicate single value
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1, 1, 1])

def test_large_numbers():
    """Test with large numbers."""
    assert find_second_largest([10**6, 10**9, 10**3]) == 10**6