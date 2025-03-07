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
    
    # Determine column width based on longest string representation
    col_width = max(len(str(item)) for item in arr) + 2
    
    # Create table header and separator
    header = f"| Index |  {'Value':^{col_width}}  |"
    separator = f"+{'-' * 6}+{'-' * (col_width + 4)}+"
    
    # Build table rows
    rows = [separator, header, separator]
    for index, value in enumerate(arr):
        row = f"| {index:^5} |  {str(value):^{col_width}}  |"
        rows.append(row)
    
    # Add bottom separator
    rows.append(separator)
    
    # Join rows into a single string
    return '\n'.join(rows)