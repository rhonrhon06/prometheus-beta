from cryptography.fernet import Fernet
import os

def decrypt_file(encrypted_file_path, key_path, output_file_path=None):
    """
    Decrypt an encrypted file using a Fernet symmetric encryption key.
    
    Args:
        encrypted_file_path (str): Path to the encrypted file
        key_path (str): Path to the encryption key file
        output_file_path (str, optional): Path to save the decrypted file. 
                                          If not provided, uses the input filename without .encrypted extension
    
    Returns:
        str: Path to the decrypted file
    
    Raises:
        FileNotFoundError: If encrypted file or key file does not exist
        ValueError: If key is invalid or decryption fails
    """
    # Check file existence
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_path}")
    
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key file not found: {key_path}")
    
    # Read encryption key
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    
    # Initialize Fernet encryptor
    try:
        fernet = Fernet(key)
    except Exception as e:
        raise ValueError(f"Invalid encryption key: {e}")
    
    # Read encrypted file
    try:
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
    except IOError as e:
        raise IOError(f"Could not read encrypted file: {e}")
    
    # Decrypt file
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")
    
    # Determine output file path
    if output_file_path is None:
        # Remove .encrypted extension if present
        output_file_path = encrypted_file_path.removesuffix('.encrypted')
        if output_file_path == encrypted_file_path:
            output_file_path += '.decrypted'
    
    # Write decrypted data
    try:
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decrypted_data)
    except IOError as e:
        raise IOError(f"Could not write decrypted file: {e}")
    
    return output_file_path