import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome("a") == True  # Single character is a palindrome

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_case_insensitive():
    """Test that palindrome check is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaCeCaR") == True

def test_with_punctuation():
    """Test palindromes with punctuation and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])

def test_special_characters():
    """Test palindromes with special characters."""
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True