import pytest
from src.number_checker import is_even_or_odd

def test_even_numbers():
    """Test that even numbers are correctly identified."""
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(-4) == 'even'
    assert is_even_or_odd(100) == 'even'

def test_odd_numbers():
    """Test that odd numbers are correctly identified."""
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(-3) == 'odd'
    assert is_even_or_odd(99) == 'odd'

def test_invalid_inputs():
    """Test error handling for invalid input types."""
    # Test float input
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    
    # Test string input
    with pytest.raises(TypeError):
        is_even_or_odd('5')
    
    # Test None input
    with pytest.raises(TypeError):
        is_even_or_odd(None)
    
    # Test list input
    with pytest.raises(TypeError):
        is_even_or_odd([2])