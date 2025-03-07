import pytest
from src.font_logger import FontLogger

def test_default_font_size():
    """Test logging with default font size"""
    result = FontLogger.log("Hello, world!")
    assert "[Font Size 12]" in result

def test_custom_font_size():
    """Test logging with a custom font size"""
    result = FontLogger.log("Large text", 24)
    assert "[Font Size 24]" in result

def test_minimum_font_size():
    """Test logging with minimum allowed font size"""
    result = FontLogger.log("Tiny text", 1)
    assert "[Font Size 1]" in result

def test_maximum_font_size():
    """Test logging with maximum allowed font size"""
    result = FontLogger.log("Huge text", 72)
    assert "[Font Size 72]" in result

def test_invalid_font_size_low():
    """Test raising error for font size below 1"""
    with pytest.raises(ValueError, match="Font size must be between 1 and 72"):
        FontLogger.log("Invalid text", 0)

def test_invalid_font_size_high():
    """Test raising error for font size above 72"""
    with pytest.raises(ValueError, match="Font size must be between 1 and 72"):
        FontLogger.log("Invalid text", 73)

def test_non_integer_font_size():
    """Test raising error for non-integer font size"""
    with pytest.raises(TypeError, match="Font size must be an integer"):
        FontLogger.log("Invalid text", "large")

def test_non_string_message():
    """Test raising error for non-string message"""
    with pytest.raises(TypeError, match="Message must be a string"):
        FontLogger.log(123)