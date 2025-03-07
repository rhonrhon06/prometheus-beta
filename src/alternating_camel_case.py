def to_alternating_camel_case(s: str) -> str:
    """
    Convert a string to alternating camel case.
    
    Args:
        s (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating camel case.
    
    Raises:
        TypeError: If input is not a string.
        
    Examples:
        >>> to_alternating_camel_case("hello world")
        'hElLoWoRlD'
        >>> to_alternating_camel_case("python is awesome")
        'pYtHoNiSaWeSoMe'
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphabetic characters and split
    chars = [c for c in s if c.isalpha()]
    
    # If empty string or no chars, return empty string
    if not chars:
        return ""
    
    # Convert to alternating case
    return ''.join(
        c.upper() if idx % 2 == 1 else c.lower() 
        for idx, c in enumerate(chars)
    )