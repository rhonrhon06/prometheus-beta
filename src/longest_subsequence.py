def longest_subsequence_with_sum(arr, target):
    """
    Find the length of the longest subsequence in an array with a sum equal to the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
             Returns 0 if no such subsequence exists
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    if not arr:
        return 0
    
    n = len(arr)
    max_length = 0
    
    # Try all possible subsequences
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            
            # If we found a subsequence matching the target
            if current_sum == target:
                max_length = max(max_length, end - start + 1)
            
            # Optimization: If sum exceeds target, break inner loop
            if current_sum > target:
                break
    
    return max_length