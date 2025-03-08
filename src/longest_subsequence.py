def longest_subsequence_with_sum(arr, target):
    """
    Find the length of the longest subsequence in an array with a sum equal to the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
             Returns 0 if no such subsequence exists
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not arr:
        return 0
    
    # Use a prefix sum approach with dynamic programming
    prefix_sums = {0: -1}  # Initialize with 0 sum at index -1
    current_sum = 0
    max_length = 0
    
    for end, num in enumerate(arr):
        current_sum += num
        
        # Check if we have a prefix sum that makes the current subsequence match target
        if current_sum - target in prefix_sums:
            # Update max length, ensuring local max
            candidate_length = end - prefix_sums[current_sum - target]
            max_length = max(max_length, candidate_length)
        
        # Store the leftmost occurrence of each prefix sum
        prefix_sums.setdefault(current_sum, end)
    
    return max_length