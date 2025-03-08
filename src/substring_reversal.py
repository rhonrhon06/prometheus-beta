def reverse_substring(text: str, start: int, end: int) -> str:
    """
    Reverse a specific substring within a given string without using built-in reverse methods.

    Args:
        text (str): The original input string
        start (int): The starting index of the substring to reverse (inclusive)
        end (int): The ending index of the substring to reverse (exclusive)

    Returns:
        str: A new string with the specified substring reversed

    Raises:
        ValueError: If start or end indices are out of bounds
        ValueError: If start index is greater than end index
    """
    # Validate input indices
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if start < 0 or end > len(text) or start > end:
        raise ValueError("Invalid substring indices")
    
    # Convert string to list for manipulation
    chars = list(text)
    
    # Reverse the substring in-place
    while start < end - 1:
        chars[start], chars[end - 1] = chars[end - 1], chars[start]
        start += 1
        end -= 1
    
    # Convert back to string
    return ''.join(chars)