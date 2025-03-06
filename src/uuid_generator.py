import os
import time
import random

def generate_uuid():
    """
    Generate a version 4 UUID (Universally Unique Identifier) without using libraries.
    
    Returns:
        str: A randomly generated UUID in standard 8-4-4-4-12 format.
    """
    # Get current timestamp and process ID for additional randomness
    timestamp = int(time.time() * 1000)
    pid = os.getpid()
    
    # Use a combination of random bytes and timestamp for entropy
    random.seed(timestamp + pid)
    
    # Generate 16 random bytes (128 bits)
    uuid_bytes = [random.randint(0, 255) for _ in range(16)]
    
    # Set version (4) and variant bits as per UUID v4 spec
    # Version is set in 7th byte (index 6)
    uuid_bytes[6] = (uuid_bytes[6] & 0x0F) | 0x40
    # Variant is set in 9th byte (index 8)
    uuid_bytes[8] = (uuid_bytes[8] & 0x3F) | 0x80
    
    # Convert to hexadecimal string with standard UUID formatting
    hex_chars = [f'{byte:02x}' for byte in uuid_bytes]
    return (
        f"{''.join(hex_chars[0:4])}-"
        f"{''.join(hex_chars[4:6])}-"
        f"{''.join(hex_chars[6:8])}-"
        f"{''.join(hex_chars[8:10])}-"
        f"{''.join(hex_chars[10:16])}"
    )