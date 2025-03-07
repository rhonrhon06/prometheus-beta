def log_array_as_table(arr):
    """
    Convert an array to a formatted table string for logging.
    
    Args:
        arr (list): The input array to be logged as a table.
    
    Returns:
        str: A formatted table representation of the input array.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return "Empty table"
    
    # Create table header and separator 
    header = f"| Index |   Value   |"
    separator = f"+{'-' * 6}+{'-' * 10}+"
    
    # Build table rows
    rows = [separator, header, separator]
    for index, value in enumerate(arr):
        row = f"| {index:<5} |    {value:<5}    |"
        rows.append(row)
    
    # Add bottom separator
    rows.append(separator)
    
    # Join rows into a single string
    return '\n'.join(rows)