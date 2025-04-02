"""
Module for replacing strings in files.
"""
import re

def replace_string_in_file(file_path, old_string, new_string, case_sensitive=True):
    """
    Replace all occurrences of a specific string in a file.

    Args:
        file_path (str): Path to the file to be modified.
        old_string (str): The string to be replaced.
        new_string (str): The string to replace with.
        case_sensitive (bool, optional): Whether replacement should be case-sensitive. 
                                         Defaults to True.

    Returns:
        int: Number of replacements made.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If any of the arguments are not strings.
        ValueError: If old_string is an empty string.
    """
    # Validate input types
    if not all(isinstance(arg, str) for arg in (file_path, old_string, new_string)):
        raise TypeError("All arguments must be strings")
    
    # Validate old_string is not empty
    if not old_string:
        raise ValueError("Old string cannot be empty")
    
    # Read the file contents
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Decide replacement method based on case sensitivity
    if case_sensitive:
        replacements = content.count(old_string)
        modified_content = content.replace(old_string, new_string)
    else:
        # Use custom case-preserving replacement for case-insensitive mode
        def case_preserve_replace(match):
            """Replace string while preserving original case."""
            matched = match.group(0)
            if matched.islower():
                return new_string.lower()
            elif matched.istitle():
                return new_string.title()
            elif matched.isupper():
                return new_string.upper()
            return new_string
        
        pattern = re.compile(re.escape(old_string), re.IGNORECASE)
        modified_content = pattern.sub(case_preserve_replace, content)
        
        # Count replacements
        replacements = len(pattern.findall(content))
    
    # Write back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)
    
    return replacements