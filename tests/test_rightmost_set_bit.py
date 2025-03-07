import pytest
from src.rightmost_set_bit import find_rightmost_set_bit

def test_typical_cases():
    """Test various typical scenarios with different bit positions."""
    assert find_rightmost_set_bit(18) == 2   # Binary: 10010
    assert find_rightmost_set_bit(16) == 5   # Binary: 10000
    assert find_rightmost_set_bit(7) == 1    # Binary: 111
    assert find_rightmost_set_bit(8) == 4    # Binary: 1000

def test_edge_cases():
    """Test edge cases like 0, 1, and powers of 2."""
    assert find_rightmost_set_bit(0) == 0    # No set bits
    assert find_rightmost_set_bit(1) == 1    # Lowest bit is set
    assert find_rightmost_set_bit(2) == 2    # Second bit is set
    assert find_rightmost_set_bit(2**10) == 11  # Large power of 2

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        find_rightmost_set_bit("not an int")
    with pytest.raises(TypeError):
        find_rightmost_set_bit(3.14)
    with pytest.raises(TypeError):
        find_rightmost_set_bit(None)

def test_negative_numbers():
    """Test behavior with negative numbers."""
    assert find_rightmost_set_bit(-1) == 1   # Negative numbers handled
    assert find_rightmost_set_bit(-8) == 4   # Handles negative powers of 2