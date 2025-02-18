import pytest
from src.lcm_recursive import least_common_multiple_recursive, gcd_recursive

def test_gcd_recursive():
    """Test the helper GCD recursive function."""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 23) == 1
    assert gcd_recursive(100, 75) == 25

def test_lcm_recursive_basic():
    """Test basic LCM calculations."""
    assert least_common_multiple_recursive(4, 6) == 12
    assert least_common_multiple_recursive(21, 6) == 42
    assert least_common_multiple_recursive(17, 23) == 391

def test_lcm_recursive_same_number():
    """Test LCM when both numbers are the same."""
    assert least_common_multiple_recursive(5, 5) == 5
    assert least_common_multiple_recursive(100, 100) == 100

def test_lcm_recursive_one_number_multiple():
    """Test LCM when one number is a multiple of the other."""
    assert least_common_multiple_recursive(4, 8) == 8
    assert least_common_multiple_recursive(7, 14) == 14
    assert least_common_multiple_recursive(15, 45) == 45

def test_lcm_recursive_coprime():
    """Test LCM for coprime numbers."""
    assert least_common_multiple_recursive(17, 23) == 391
    assert least_common_multiple_recursive(11, 13) == 143

def test_lcm_recursive_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        least_common_multiple_recursive(0, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        least_common_multiple_recursive(5, -3)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        least_common_multiple_recursive(-10, -5)