def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.

    Args:
        strings (list): A list of strings to compare.

    Returns:
        str: The longest common suffix. If no common suffix exists, 
             returns an empty string.

    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty.
    """
    # Validate input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Handle single string case
    if len(strings) == 1:
        return strings[0]
    
    # Ensure all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Handle empty string case
    if any(s == '' for s in strings):
        return ''
    
    # Find the minimum length string to limit suffix search
    min_length = min(len(s) for s in strings)
    
    # Check suffixes from the end
    for i in range(1, min_length + 1):
        # Get potential suffix
        suffix = strings[0][-i:]
        
        # Check if this suffix is common to all strings
        if not all(s.endswith(suffix) for s in strings):
            # If not common, return the previous (longer) suffix
            return strings[0][-i+1:] if i > 1 else ''
    
    # If loop completes, return the shortest possible common suffix
    return strings[0][:min_length]