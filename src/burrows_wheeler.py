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
    
    # Compute first column by sorting
    first_column = sorted(bwt_string)
    
    # Initialize reconstruction
    n = len(bwt_string)
    next_char = [0] * n
    
    # Create mapping to reconstruct the original string
    for i in range(n):
        next_char[i] = first_column.index(bwt_string[i])
        first_column[next_char[i]] = ''
    
    # Reconstruct the original string
    result = [''] * n
    j = 0
    for i in range(n-1, -1, -1):
        result[i] = bwt_string[j]
        j = next_char[j]
    
    # Remove terminator and join
    original = ''.join(result).rstrip('$')
    
    return original