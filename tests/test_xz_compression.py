import pytest
import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from xz_compression import compress_xz, decompress_xz

def test_compress_decompress_text():
    """Test compression and decompression of text data"""
    original_text = "Hello, world! This is a test of XZ compression."
    compressed = compress_xz(original_text)
    decompressed = decompress_xz(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data"""
    original_bytes = b'\x00\x01\x02\x03\x04\x05'
    compressed = compress_xz(original_bytes)
    decompressed = decompress_xz(compressed)
    assert decompressed == original_bytes

def test_different_compression_levels():
    """Test compression with different levels"""
    text = "Test compression at different levels"
    for level in range(10):
        compressed = compress_xz(text, compression_level=level)
        decompressed = decompress_xz(compressed)
        assert decompressed.decode('utf-8') == text

def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        compress_xz("Test", compression_level=10)
    with pytest.raises(ValueError):
        compress_xz("Test", compression_level=-1)

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_xz(123)
    with pytest.raises(TypeError):
        compress_xz(None)
    with pytest.raises(TypeError):
        decompress_xz("not bytes")
    with pytest.raises(TypeError):
        decompress_xz(123)

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_text = ""
    compressed = compress_xz(empty_text)
    decompressed = decompress_xz(compressed)
    assert decompressed.decode('utf-8') == empty_text

def test_large_input():
    """Test compression and decompression of large input"""
    large_text = "x" * 100000  # 100KB of repeated characters
    compressed = compress_xz(large_text)
    decompressed = decompress_xz(compressed)
    assert decompressed.decode('utf-8') == large_text