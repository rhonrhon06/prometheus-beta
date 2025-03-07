def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.
    Note: Comparison is strictly case-sensitive.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Strict case-sensitive matching
    if len(str1) != len(str2):
        return ""
    
    # Create dynamic programming matrix
    m = len(str1)
    # Initialize matrix with zeros
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    
    # Build the LCS matrix
    max_len = 0
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            # Strict case-sensitive matching
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0
    
    # If no full match, return empty string
    if max_len != m:
        return ""
    
    # Backtrack to find the LCS
    lcs = []
    for i in range(1, m + 1):
        if dp[i][i] == m:
            lcs = list(str1)
            break
    
    return ''.join(lcs)