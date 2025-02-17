import pytest
from datetime import datetime
from src.timestamp_converter import timestamp_to_human_readable

def test_valid_timestamp():
    # Test a known timestamp
    timestamp = 1640995200  # January 1, 2022 00:00:00 UTC
    assert timestamp_to_human_readable(timestamp) == "January 01, 2022"

def test_float_timestamp():
    # Test with float timestamp
    timestamp = 1640995200.5  # Slightly after January 1, 2022
    assert timestamp_to_human_readable(timestamp) == "January 01, 2022"

def test_invalid_type():
    # Test invalid input types
    with pytest.raises(TypeError):
        timestamp_to_human_readable("not a timestamp")
    
    with pytest.raises(TypeError):
        timestamp_to_human_readable(None)

def test_invalid_timestamp():
    # Test extremely large or negative timestamp
    with pytest.raises(ValueError):
        timestamp_to_human_readable(999999999999999999)
    
    with pytest.raises(ValueError):
        timestamp_to_human_readable(-999999999999999999)

def test_zero_timestamp():
    # Test Unix epoch start
    assert timestamp_to_human_readable(0) == "January 01, 1970"