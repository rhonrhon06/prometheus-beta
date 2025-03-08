def filter_primes(numbers):
    """
    Filter a list of integers to return only prime numbers.

    A prime number is a number greater than 1 that has no divisors 
    other than 1 and itself.

    Args:
        numbers (list): A list of integers to filter.

    Returns:
        list: A new list containing only the prime numbers from the input.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Helper function to check if a number is prime
    def is_prime(n):
        # Check input type
        if not isinstance(n, int):
            raise TypeError("All elements must be integers")
        
        # Prime numbers are greater than 1
        if n <= 1:
            return False
        
        # Check for divisibility 
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    # Filter and return prime numbers
    return [num for num in numbers if is_prime(num)]