import pytest
from src.hex_to_decimal import hex_to_decimal

def test_basic_hex_conversion():
    """Test basic hexadecimal to decimal conversion."""
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('F') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('FF') == 255
    assert hex_to_decimal('100') == 256

def test_hex_with_prefix():
    """Test hexadecimal strings with '0x' or '0X' prefix."""
    assert hex_to_decimal('0xA') == 10
    assert hex_to_decimal('0XFF') == 255

def test_mixed_case():
    """Test hexadecimal conversion with mixed case."""
    assert hex_to_decimal('a') == 10
    assert hex_to_decimal('Ff') == 255

def test_large_hex_number():
    """Test conversion of larger hexadecimal numbers."""
    assert hex_to_decimal('1A5') == 421
    assert hex_to_decimal('FFFF') == 65535

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('G')
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('1.5')
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('ABC123XYZ')

def test_type_errors():
    """Test error handling for incorrect input types."""
    with pytest.raises(TypeError, match="Input must be a string"):
        hex_to_decimal(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        hex_to_decimal(None)
    with pytest.raises(TypeError, match="Input must be a string"):
        hex_to_decimal([])