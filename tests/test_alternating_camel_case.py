import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert to_alternating_camel_case("hello world") == "hElLoWoRlD"
    assert to_alternating_camel_case("python is awesome") == "pYtHoNiSaWeSoMe"

def test_single_word():
    """Test conversion of a single word"""
    assert to_alternating_camel_case("hello") == "hElLo"

def test_empty_string():
    """Test empty string input"""
    assert to_alternating_camel_case("") == ""

def test_whitespace_handling():
    """Test handling of extra whitespace"""
    assert to_alternating_camel_case("  hello  world  ") == "hElLoWoRlD"

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        to_alternating_camel_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_camel_case(None)

def test_mixed_case_input():
    """Test input with mixed existing case"""
    assert to_alternating_camel_case("HELLO world") == "hElLoWoRlD"
    assert to_alternating_camel_case("hello WORLD") == "hElLoWoRlD"

def test_special_characters():
    """Test handling of strings with special characters"""
    assert to_alternating_camel_case("hello-world") == "hElLoWoRlD"
    assert to_alternating_camel_case("hello world!") == "hElLoWoRlD"