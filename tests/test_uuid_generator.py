import re
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from uuid_generator import generate_uuid

def test_uuid_format():
    """Test that the generated UUID matches the standard format."""
    uuid = generate_uuid()
    
    # Check overall UUID format
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid, re.IGNORECASE), f"Invalid UUID format: {uuid}"

def test_uuid_uniqueness():
    """Test that multiple UUID generations produce unique results."""
    uuids = set()
    num_generations = 1000
    
    for _ in range(num_generations):
        uuids.add(generate_uuid())
    
    assert len(uuids) == num_generations, "UUIDs are not unique"

def test_uuid_version():
    """Test that the UUID version is correctly set to 4."""
    uuid = generate_uuid()
    version_char = uuid.split('-')[2][0]
    assert version_char == '4', f"Incorrect UUID version: {version_char}"

def test_uuid_variant():
    """Test that the UUID variant is correctly set."""
    uuid = generate_uuid()
    variant_char = uuid.split('-')[3][0]
    assert variant_char in ['8', '9', 'a', 'b'], f"Incorrect UUID variant: {variant_char}"