import pytest
from src.palindrome_substrings import find_palindromic_substrings

def test_empty_string():
    assert find_palindromic_substrings("") == []

def test_single_character():
    result = find_palindromic_substrings("a")
    assert result == ["a"]

def test_simple_palindrome():
    result = find_palindromic_substrings("racecar")
    expected = ["r", "a", "c", "e", "racecar", "aceca", "cec"]
    assert sorted(result, key=len) == sorted(expected, key=len)

def test_multiple_palindromes():
    result = find_palindromic_substrings("aabbaa")
    expected = ["a", "b", "aa", "bb", "aabbaa"]
    assert sorted(result, key=len) == sorted(expected, key=len)

def test_no_palindromes():
    result = find_palindromic_substrings("abcd")
    expected = ["a", "b", "c", "d"]
    assert sorted(result) == sorted(expected)

def test_complex_string():
    result = find_palindromic_substrings("abaxyzzyxf")
    expected = ["a", "b", "x", "y", "z", "aba", "xyzyx", "zz"]
    assert sorted(result, key=len) == sorted(expected, key=len)