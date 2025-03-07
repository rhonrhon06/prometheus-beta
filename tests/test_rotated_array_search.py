import pytest
from src.rotated_array_search import search_rotated_array

def test_search_rotated_array_basic():
    # Basic rotation scenario
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_array(arr, 0) == 4
    assert search_rotated_array(arr, 3) == -1

def test_search_rotated_array_no_rotation():
    # Array with no rotation
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert search_rotated_array(arr, 3) == 2
    assert search_rotated_array(arr, 8) == -1

def test_search_rotated_array_small_arrays():
    # Edge cases with small arrays
    assert search_rotated_array([1], 1) == 0
    assert search_rotated_array([1], 2) == -1
    assert search_rotated_array([], 1) == -1

def test_search_rotated_array_rotation_at_end():
    # Rotation at the end of the array
    arr = [2, 3, 4, 5, 6, 7, 1]
    assert search_rotated_array(arr, 1) == 6
    assert search_rotated_array(arr, 2) == 0

def test_search_rotated_array_invalid_inputs():
    # Test invalid input types
    with pytest.raises(TypeError, match="Input must be a list"):
        search_rotated_array(None, 1)
    
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_rotated_array([1, 2, 3], "target")

def test_search_rotated_array_edge_cases():
    # Multiple rotations
    arr = [5, 6, 7, 8, 1, 2, 3, 4]
    assert search_rotated_array(arr, 8) == 3
    assert search_rotated_array(arr, 1) == 4