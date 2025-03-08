import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test edge cases with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_partial_match():
    """Test partial matches"""
    # Note: There can be multiple valid LCS for some inputs
    # So we'll check multiple possible correct answers
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    assert result in ["BCBA", "BDAB"]

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_type_errors():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "ABC")

def test_unicode_strings():
    """Test LCS with unicode strings"""
    assert longest_common_subsequence("こんにちは", "こんばんは") == "こんは"