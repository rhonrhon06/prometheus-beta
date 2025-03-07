def search_rotated_array(arr, target):
    """
    Search for a target element in a rotated sorted array using binary search.
    
    A rotated sorted array is an array that was originally sorted in ascending order,
    but has been rotated around a pivot point. This function finds the target element
    in O(log n) time complexity.
    
    Args:
        arr (list): A rotated sorted array of distinct integers
        target (int): The element to search for
    
    Returns:
        int: Index of the target element if found, else -1
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Raises:
        TypeError: If input is not a list or target is not an integer
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Handle empty array
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If mid element is the target, return its index
        if arr[mid] == target:
            return mid
        
        # Check which half is sorted
        # Left half is sorted
        if arr[left] <= arr[mid]:
            # Check if target is in the sorted left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Check if target is in the sorted right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    # Target not found
    return -1