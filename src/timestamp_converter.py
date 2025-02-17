from datetime import datetime

def timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp to a human-readable date string.
    
    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch)
    
    Returns:
        str: Human-readable date string in format 'Month Day, Year'
    
    Raises:
        ValueError: If timestamp is not a valid number
        TypeError: If timestamp is not an int or float
    """
    # Type checking
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be an integer or float")
    
    try:
        # Convert timestamp to datetime object
        date_obj = datetime.fromtimestamp(timestamp)
        
        # Format date in a human-readable way
        return date_obj.strftime("%B %d, %Y")
    
    except (ValueError, OverflowError):
        raise ValueError("Invalid timestamp: Unable to convert to date")