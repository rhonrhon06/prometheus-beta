def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending).
    
    Returns:
        list: A list of missing numbers between the minimum and maximum values.
    
    Raises:
        ValueError: If the input is not a valid list of positive integers.
    """
    # Validate input
    if not arr or not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Determine if the array is ascending or descending
    is_ascending = arr[0] <= arr[-1]
    
    # Sort the array in ascending order for consistent processing
    if not is_ascending:
        arr = sorted(arr, reverse=True)
    
    # Find the range of numbers
    min_val = arr[0]
    max_val = arr[-1]
    
    # Create a set of the input array for efficient lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_val, max_val + 1) 
        if num not in num_set
    ]
    
    # If originally descending, return in descending order
    return sorted(missing_numbers, reverse=not is_ascending)