import pytest
from src.rod_cutting import rod_cutting

def test_basic_rod_cutting():
    """Test basic rod cutting scenarios."""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Best cut: 2 + 2
    assert rod_cutting(prices, 6) == 17
    assert rod_cutting(prices, 7) == 18

def test_single_length():
    """Test rod cutting with single length."""
    prices = [3]
    assert rod_cutting(prices, 1) == 3

def test_zero_length():
    """Test rod cutting with zero length."""
    prices = [1, 5, 8]
    assert rod_cutting(prices, 0) == 0

def test_empty_max_length():
    """Test when max length is greater than available prices."""
    prices = [1, 5, 8]
    assert rod_cutting(prices, 5) == 12

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Prices list cannot be empty"):
        rod_cutting([], 5)
    
    with pytest.raises(ValueError, match="Rod length must be non-negative"):
        rod_cutting([1, 2, 3], -1)

def test_no_profit():
    """Test scenario with zero prices."""
    prices = [0, 0, 0]
    assert rod_cutting(prices, 2) == 0