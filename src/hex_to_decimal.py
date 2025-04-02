def hex_to_decimal(hex_string: str) -> int:
    """
    Convert a hexadecimal string to its decimal (base 10) integer representation.

    Args:
        hex_string (str): A string representing a hexadecimal number.
                          Can be prefixed with '0x' or '0X' or contain only hex digits.
                          Supports both uppercase and lowercase hex digits.

    Returns:
        int: The decimal equivalent of the input hexadecimal number.

    Raises:
        ValueError: If the input string contains invalid hexadecimal characters.
        TypeError: If the input is not a string.
    """
    # Check input type
    if not isinstance(hex_string, str):
        raise TypeError("Input must be a string")
    
    # Remove '0x' or '0X' prefix if present
    hex_string = hex_string.lstrip('0x').lstrip('0X')
    
    # Validate hex string contains only valid hex digits
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")