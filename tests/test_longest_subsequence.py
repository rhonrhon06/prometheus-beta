import pytest
from src.longest_subsequence import longest_subsequence_with_sum

def test_basic_subsequence():
    """Test basic subsequence sum matching"""
    arr = [1, 2, 3, 4, 5]
    target = 9
    assert longest_subsequence_with_sum(arr, target) == 3  # [2,3,4] matches

def test_full_array_match():
    """Test when entire array matches the target"""
    arr = [1, 2, 3, 4]
    target = 10
    assert longest_subsequence_with_sum(arr, target) == 4

def test_no_subsequence_match():
    """Test when no subsequence matches the target"""
    arr = [1, 2, 3, 4, 5]
    target = 100
    assert longest_subsequence_with_sum(arr, target) == 0

def test_empty_array():
    """Test with an empty array"""
    arr = []
    target = 5
    assert longest_subsequence_with_sum(arr, target) == 0

def test_negative_numbers():
    """Test with negative numbers in the array"""
    arr = [-1, 2, -3, 4, 5]
    target = 6
    assert longest_subsequence_with_sum(arr, target) == 3  # [2,-3,4]

def test_multiple_possible_subsequences():
    """Test when multiple subsequences can match"""
    arr = [1, 2, 3, 1, 2, 3]
    target = 6
    assert longest_subsequence_with_sum(arr, target) == 3

def test_zero_target():
    """Test with zero as target"""
    arr = [-1, 1, 0, 2, -2]
    target = 0
    assert longest_subsequence_with_sum(arr, target) == 3  # [1, 0, -1] or [-1, 1]