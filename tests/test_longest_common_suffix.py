import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_basic_common_suffix():
    """Test finding a common suffix among multiple strings."""
    assert find_longest_common_suffix(["flower", "power", "tower"]) == "ower"

def test_single_string():
    """Test when only one string is provided."""
    assert find_longest_common_suffix(["hello"]) == "hello"

def test_no_common_suffix():
    """Test when no common suffix exists."""
    assert find_longest_common_suffix(["abc", "def", "ghi"]) == ""

def test_empty_string_in_list():
    """Test behavior with an empty string in the list."""
    assert find_longest_common_suffix(["abc", "", "dc"]) == ""

def test_full_match():
    """Test when all strings are identical."""
    assert find_longest_common_suffix(["abc", "abc", "abc"]) == "abc"

def test_invalid_input_not_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_empty_list():
    """Test raising ValueError for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_common_suffix([])

def test_non_string_elements():
    """Test raising TypeError for non-string list elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["abc", 123, "def"])

def test_different_length_strings():
    """Test finding common suffix with strings of different lengths."""
    assert find_longest_common_suffix(["longer", "short"]) == ""

def test_partial_suffix():
    """Test finding a partial common suffix."""
    assert find_longest_common_suffix(["runner", "bummer", "plumber"]) == "er"