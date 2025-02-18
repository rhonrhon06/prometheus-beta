def gcd_recursive(a, b):
    """
    Helper function to calculate Greatest Common Divisor recursively using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Greatest Common Divisor of a and b
    """
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: GCD(a, b) = GCD(b, a % b)
    return gcd_recursive(b, a % b)

def least_common_multiple_recursive(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers using recursion.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    # Validate inputs
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # LCM(a, b) = |a * b| / GCD(a, b)
    return abs(a * b) // gcd_recursive(a, b)