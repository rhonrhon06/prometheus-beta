class FontLogger:
    """
    A logging utility that supports output with different font sizes.
    
    Font sizes are represented by integers, with larger numbers 
    indicating larger font sizes.
    """
    
    @staticmethod
    def log(message, font_size=12):
        """
        Log a message with a specified font size.
        
        Args:
            message (str): The message to log
            font_size (int, optional): Size of the font. Defaults to 12.
                                       Must be between 1 and 72.
        
        Raises:
            ValueError: If font size is not between 1 and 72
            TypeError: If message is not a string or font_size is not an integer
        """
        # Validate inputs
        if not isinstance(message, str):
            raise TypeError("Message must be a string")
        
        if not isinstance(font_size, int):
            raise TypeError("Font size must be an integer")
        
        # Check font size range
        if font_size < 1 or font_size > 72:
            raise ValueError("Font size must be between 1 and 72")
        
        # Simulate logging with font size
        # In a real-world scenario, this might use a logging framework 
        # or UI-specific font rendering
        print(f"[Font Size {font_size}] {message}")
        
        return f"[Font Size {font_size}] {message}"