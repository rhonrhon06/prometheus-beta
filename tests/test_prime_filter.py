import pytest
from src.prime_filter import filter_primes

def test_basic_prime_filtering():
    """Test filtering a list with mixed prime and non-prime numbers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected

def test_empty_list():
    """Test filtering an empty list."""
    assert filter_primes([]) == []

def test_no_primes():
    """Test a list with no prime numbers."""
    input_list = [1, 4, 6, 8, 9, 10]
    assert filter_primes(input_list) == []

def test_only_primes():
    """Test a list containing only prime numbers."""
    input_list = [2, 3, 5, 7, 11, 13]
    assert filter_primes(input_list) == input_list

def test_negative_numbers():
    """Test filtering with negative numbers."""
    input_list = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]
    expected = [2, 3, 5]
    assert filter_primes(input_list) == expected

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_primes("not a list")

def test_non_integer_elements():
    """Test that non-integer elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_primes([1, 2, 3, "four", 5])

def test_large_primes():
    """Test filtering with larger prime numbers."""
    input_list = [97, 100, 541, 1000, 1009]
    expected = [97, 541, 1009]
    assert filter_primes(input_list) == expected