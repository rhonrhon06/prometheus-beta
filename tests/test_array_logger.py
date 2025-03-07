import pytest
from src.array_logger import log_array_as_table

def test_log_array_as_table_basic():
    """Test logging a basic array of integers."""
    arr = [1, 2, 3]
    result = log_array_as_table(arr)
    
    # Check key components of the table
    assert '| Index |  Value  |' in result
    assert '| 0     |   1     |' in result
    assert '| 1     |   2     |' in result
    assert '| 2     |   3     |' in result

def test_log_array_as_table_mixed_types():
    """Test logging an array with mixed types."""
    arr = [1, 'hello', True, 3.14]
    result = log_array_as_table(arr)
    
    # Check key components of the table
    assert '| Index |   Value   |' in result
    assert '| 0     |    1      |' in result
    assert '| 1     |  hello    |' in result
    assert '| 2     |   True    |' in result
    assert '| 3     |   3.14    |' in result

def test_log_array_as_table_empty():
    """Test logging an empty array."""
    arr = []
    result = log_array_as_table(arr)
    
    assert result == "Empty table"

def test_log_array_as_table_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        log_array_as_table("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        log_array_as_table(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        log_array_as_table(None)