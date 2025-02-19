import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_palindrome_pairs_basic():
    # Basic test case with palindrome pairs
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert [0, 1] in result  # "bat" + "tab" forms palindrome
    assert [1, 0] in result  # "tab" + "bat" forms palindrome

def test_palindrome_pairs_empty_list():
    # Test with empty list
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_palindrome_pairs_single_word():
    # Test with single word
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_palindrome_pairs_complete_match():
    # Test with words that fully form palindromes
    words = ["abc", "cba"]
    result = find_palindrome_pairs(words)
    assert [0, 1] in result
    assert [1, 0] in result

def test_palindrome_pairs_no_matches():
    # Test with no palindrome pairs
    words = ["dog", "cat", "bird"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_palindrome_pairs_complex_example():
    # More complex example with multiple palindrome pairs
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    assert len(result) > 0
    # Add specific assertions based on expected pairs