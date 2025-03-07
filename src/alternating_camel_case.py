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
    
    # Remove extra whitespace, filter out non-alphanumeric chars, and split
    import re
    words = re.sub(r'[^a-zA-Z\s]', '', s.strip()).split()
    
    # If empty string or no words, return empty string
    if not words:
        return ""
    
    # Convert to alternating case
    result = []
    for word in words:
        # Convert each word to alternating case
        converted_word = ''.join(
            c.upper() if idx % 2 == 1 else c.lower() 
            for idx, c in enumerate(word.lower())
        )
        result.append(converted_word)
    
    # Join the converted words
    return ''.join(result)