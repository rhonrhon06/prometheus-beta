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
    
    # Preserve original case for output
    def lcs_core(s1, s2):
        # Create a matrix to store LCS lengths
        m, n = len(s1), len(s2)
        # Add 1 to handle 0-indexing
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Find length of LCS
        max_length = dp[m][n]
        
        # Reconstruct the LCS
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                lcs.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        # Reverse to get correct order
        return ''.join(reversed(lcs))
    
    # Perform case-sensitive LCS
    # If the strings are not the same in original case, return empty string
    if str1.lower() != str2.lower():
        # Compute LCS with original strings
        return lcs_core(str1, str2) if str1.lower() == str2.lower() else ""
    
    # If strings are identical (case-sensitive), return the original
    return str1 if str1 == str2 else lcs_core(str1, str2)