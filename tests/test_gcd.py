import pytest
from src.gcd import euclidean_gcd

def test_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1

def test_gcd_zero():
    """Test GCD involving zero"""
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5
    assert euclidean_gcd(0, 0) == 0

def test_gcd_negative_numbers():
    """Test GCD of negative numbers"""
    assert euclidean_gcd(-48, 18) == 6
    assert euclidean_gcd(48, -18) == 6
    assert euclidean_gcd(-48, -18) == 6

def test_gcd_same_number():
    """Test GCD of the same number"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(0, 0) == 0

def test_gcd_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        euclidean_gcd(4.5, 3)
    with pytest.raises(TypeError):
        euclidean_gcd("10", 5)
    with pytest.raises(TypeError):
        euclidean_gcd([10], 5)