def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within the given array.
    
    This implementation uses Kadane's algorithm to solve the problem 
    with O(n) time complexity and O(1) space complexity.
    
    Args:
        arr (list): A list of integers containing both positive and negative numbers.
    
    Returns:
        int: The maximum sum of any contiguous subarray.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
    """
    # Check for input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_sum = current_sum = arr[0]
    
    # Iterate through the array using Kadane's algorithm
    for num in arr[1:]:
        # Choose between starting a new subarray or extending the current one
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum