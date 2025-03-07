def find_rightmost_set_bit(n: int) -> int:
    """
    Determine the position of the rightmost set bit in a number.
    
    Args:
        n (int): The input number to check for the rightmost set bit.
    
    Returns:
        int: The position of the rightmost set bit (1-indexed),
             or 0 if no set bit is found (for input 0).
    
    Raises:
        TypeError: If the input is not an integer.
    
    Examples:
        >>> find_rightmost_set_bit(18)  # Binary: 10010 -> rightmost set bit is at position 2
        2
        >>> find_rightmost_set_bit(0)   # No set bits
        0
        >>> find_rightmost_set_bit(1)   # Rightmost bit is at position 1
        1
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle non-positive and zero numbers
    if n == 0:
        return 0
    
    # Take absolute value to handle negative numbers
    n = abs(n)
    
    # Use bitwise operations to find the rightmost set bit
    # We use the property that n & -n isolates the rightmost set bit
    rightmost_bit = n & -n
    
    # Calculate the position by finding the index of the set bit
    position = 1
    while rightmost_bit > 1:
        rightmost_bit >>= 1
        position += 1
    
    return position