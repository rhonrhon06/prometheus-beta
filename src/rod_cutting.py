def rod_cutting(prices, n):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
        prices (list): A list of prices for rod lengths from 1 to len(prices)
        n (int): The length of the rod to be cut
    
    Returns:
        int: The maximum obtainable value by cutting the rod
    
    Raises:
        ValueError: If prices list is empty or n is negative
    """
    # Validate input
    if not prices:
        raise ValueError("Prices list cannot be empty")
    if n < 0:
        raise ValueError("Rod length must be non-negative")
    
    # Extend prices list to handle different rod lengths
    prices = [0] + prices
    
    # Initialize dynamic programming table
    max_value = [0] * (n + 1)
    
    # Compute maximum value for each rod length
    for i in range(1, n + 1):
        max_curr = float('-inf')
        for j in range(1, min(i, len(prices)) + 1):
            max_curr = max(max_curr, prices[j] + max_value[i - j])
        max_value[i] = max_curr
    
    return max_value[n]