def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.
    
    Args:
        words (List[str]): A list of strings to check for palindrome pairs
    
    Returns:
        List[List[int]]: A list of pairs of indices where words[i] + words[j] is a palindrome
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip same index
            if i == j:
                continue
            
            # Check if concatenated strings form a palindrome
            concatenated = words[i] + words[j]
            if is_palindrome(concatenated):
                result.append([i, j])
    
    return result