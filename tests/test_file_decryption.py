import os
import pytest
from cryptography.fernet import Fernet
from src.file_decryption import decrypt_file

@pytest.fixture
def sample_key():
    """Generate a test encryption key"""
    return Fernet.generate_key()

@pytest.fixture
def encrypted_file(sample_key, tmp_path):
    """Create an encrypted file for testing"""
    # Create sample content
    content = b"Secret message for decryption testing!"
    
    # Create key file
    key_file_path = tmp_path / "test_key.key"
    with open(key_file_path, 'wb') as f:
        f.write(sample_key)
    
    # Create encrypted file
    fernet = Fernet(sample_key)
    encrypted_content = fernet.encrypt(content)
    encrypted_file_path = tmp_path / "test_file.txt.encrypted"
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_content)
    
    return {
        'content': content,
        'key_path': str(key_file_path),
        'encrypted_path': str(encrypted_file_path)
    }

def test_decrypt_file_success(encrypted_file, tmp_path):
    """Test successful file decryption"""
    output_path = str(tmp_path / "decrypted_file.txt")
    result_path = decrypt_file(
        encrypted_file['encrypted_path'], 
        encrypted_file['key_path'], 
        output_path
    )
    
    # Check result path
    assert result_path == output_path
    
    # Verify decrypted content
    with open(result_path, 'rb') as f:
        decrypted_content = f.read()
    
    assert decrypted_content == encrypted_file['content']

def test_decrypt_file_default_output(encrypted_file, tmp_path):
    """Test decryption with default output filename"""
    result_path = decrypt_file(
        encrypted_file['encrypted_path'], 
        encrypted_file['key_path']
    )
    
    # Check default name
    assert result_path.endswith('.txt')
    
    # Verify decrypted content
    with open(result_path, 'rb') as f:
        decrypted_content = f.read()
    
    assert decrypted_content == encrypted_file['content']

def test_decrypt_nonexistent_file():
    """Test decryption with non-existent encrypted file"""
    with pytest.raises(FileNotFoundError):
        decrypt_file('/path/to/nonexistent/file.encrypted', '/path/to/key')

def test_decrypt_nonexistent_key(encrypted_file):
    """Test decryption with non-existent key file"""
    with pytest.raises(FileNotFoundError):
        decrypt_file(encrypted_file['encrypted_path'], '/path/to/nonexistent/key')

def test_decrypt_invalid_key(encrypted_file, tmp_path):
    """Test decryption with invalid key"""
    invalid_key_path = tmp_path / "invalid_key.key"
    with open(invalid_key_path, 'wb') as f:
        f.write(b'invalid_key')
    
    with pytest.raises(ValueError):
        decrypt_file(encrypted_file['encrypted_path'], str(invalid_key_path))