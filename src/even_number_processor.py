def remove_even_numbers_and_sum(numbers):
    """
    Remove even numbers from the input array and return their sum.
    
    Args:
        numbers (list): A list of integers to process
    
    Returns:
        int: The sum of even numbers removed from the input list
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Separate even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # Return the sum of even numbers
    return sum(even_numbers)