from collections import Counter

def sort_by_frequency(numbers):
    """
    Sort a list of integers based on their frequency.
    Less frequent elements appear first, more frequent elements appear later.
    If multiple elements have the same frequency, order by their first occurrence.
    
    Args:
        numbers (list): A list of integers to be sorted
    
    Returns:
        list: A new list sorted by frequency
    """
    if not numbers:
        return []
    
    # Count the frequency of each number
    freq_count = Counter(numbers)
    
    # Sort the unique numbers by their frequency
    sorted_unique = sorted(set(numbers), key=lambda x: freq_count[x])
    
    # Create the final sorted list maintaining the order of sorted_unique
    result = []
    for num in sorted_unique:
        result.extend([num] * freq_count[num])
    
    return result