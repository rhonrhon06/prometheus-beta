def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two input strings.
    
    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Input validation
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Make inputs lowercase to handle case sensitivity
    str1, str2 = str1.lower(), str2.lower()
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    # Add 1 to handle 0-indexing
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Find length of LCS
    max_length = dp[m][n]
    
    # Reconstruct the LCS with multiple possibilities
    def backtrack(lcs, i, j):
        # If we've found a subsequence of max length, return it
        if len(lcs) == max_length:
            return lcs
        
        # If at the end of either string, return current LCS
        if i == 0 or j == 0:
            return lcs
        
        # If characters match, include in LCS
        if str1[i-1] == str2[j-1]:
            return backtrack(str1[i-1] + lcs, i-1, j-1)
        
        # If not matched, backtrack to find the correct path
        if dp[i-1][j] > dp[i][j-1]:
            return backtrack(lcs, i-1, j)
        else:
            return backtrack(lcs, i, j-1)
    
    # Return the LCS of longest possible length
    return backtrack("", m, n)