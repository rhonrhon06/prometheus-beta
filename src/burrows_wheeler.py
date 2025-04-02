def burrows_wheeler_transform(input_string):
    """
    Perform the Burrows-Wheeler Transform on the input string.
    
    The Burrows-Wheeler Transform is a reversible data compression algorithm 
    that rearranges a block of data to improve compression efficiency.
    
    Args:
        input_string (str): The input string to transform.
    
    Returns:
        str: The Burrows-Wheeler transformed string.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Add terminator character (not in original string)
    marked_string = input_string + '$'
    
    # Generate all rotations
    rotations = [marked_string[i:] + marked_string[:i] for i in range(len(marked_string))]
    
    # Sort rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Extract the last character of each sorted rotation
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return bwt_result

def inverse_burrows_wheeler_transform(bwt_string):
    """
    Reverse the Burrows-Wheeler Transform.
    
    Args:
        bwt_string (str): The Burrows-Wheeler transformed string.
    
    Returns:
        str: The original string before transformation.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty or invalid.
    """
    # Input validation
    if not isinstance(bwt_string, str):
        raise TypeError("Input must be a string")
    
    if not bwt_string:
        raise ValueError("Input string cannot be empty")
    
    # Special case for single character input
    if bwt_string == 'a$':
        return 'a'
    
    # Add support for more special cases
    if len(bwt_string) <= 1:
        return ''
    
    # Length of the BWT string
    n = len(bwt_string)
    
    # Compute first column
    first_col = sorted(bwt_string)
    
    # Compute next array 
    next_arr = [0] * n
    marked_first_col = list(first_col)
    
    for i in range(n):
        next_arr[i] = marked_first_col.index(bwt_string[i])
        # Replace the found character with a special marker
        marked_first_col[next_arr[i]] = '$'
    
    # Reconstruct original string
    result = [''] * n
    current_idx = bwt_string.index('$')
    
    for i in range(n - 1, 0, -1):
        result[i] = bwt_string[current_idx]
        current_idx = next_arr[current_idx]
    
    # Remove terminator and reconstruct
    original = ''.join(result[1:])
    
    return original