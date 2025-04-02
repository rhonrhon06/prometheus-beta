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
    
    # Length of the BWT string
    n = len(bwt_string)
    
    # Compute first column
    first_col = sorted(bwt_string)
    
    # Create mapping from first to last column
    mapping = {}
    for i, char in enumerate(first_col):
        count = 1
        # Count occurrences of the character before this index
        for j in range(i):
            if first_col[j] == char:
                count += 1
        # Find matching character in last column
        match_count = 0
        for j in range(n):
            if bwt_string[j] == char:
                match_count += 1
                if match_count == count:
                    mapping[(char, count)] = j
                    break
    
    # Reconstruct the original string
    result = []
    current = mapping[('$', 1)]  # Start with terminator
    seen_count = {'$': 1}
    
    for _ in range(n - 1):
        char = first_col[current]
        result.append(char)
        
        # Update count for finding next character
        seen_count[char] = seen_count.get(char, 0) + 1
        current = mapping.get((char, seen_count[char]))
    
    # Reverse and return (exclude terminator)
    return ''.join(reversed(result))