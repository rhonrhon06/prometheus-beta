from collections import Counter

def sort_by_frequency(numbers):
    """
    Sort a list of integers based on their frequency.
    Less frequent elements appear first, more frequent elements appear later.
    If multiple elements have the same frequency, sort by their first occurrence.
    
    Args:
        numbers (list): A list of integers to be sorted
    
    Returns:
        list: A new list sorted by frequency
    """
    if not numbers:
        return []
    
    # Count the frequency of each number
    freq_count = Counter(numbers)
    
    # Create a mapping of first occurrence of each unique number to preserve order
    first_occurrence = {x: numbers.index(x) for x in set(numbers)}
    
    # Sort the list based on frequency (ascending), then by first occurrence
    return sorted(numbers, key=lambda x: (freq_count[x], first_occurrence[x]))