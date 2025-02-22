def find_palindromic_substrings(s):
    """
    Find all palindromic substrings in a given string.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list: A list of all unique palindromic substrings, sorted by length
    """
    if not s:
        return []
    
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
    
    # Convert to sorted list, with preference for shorter palindromes first
    return sorted(list(palindromes), key=len)