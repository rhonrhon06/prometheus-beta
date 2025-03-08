import pytest
from src.mall_navigation import MallGraph

def test_create_mall_graph():
    """Test creating a mall graph"""
    mall = MallGraph()
    assert isinstance(mall, MallGraph)
    assert mall.graph == {}

def test_add_store():
    """Test adding a store to the mall graph"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    assert "Apple Store" in mall.graph
    assert mall.graph["Apple Store"] == {}

def test_add_duplicate_store():
    """Test adding a duplicate store raises an error"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    with pytest.raises(ValueError, match="Store Apple Store already exists in the mall map"):
        mall.add_store("Apple Store")

def test_add_connection():
    """Test adding a connection between stores"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    mall.add_store("Nike Store")
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    
    assert "Nike Store" in mall.graph["Apple Store"]
    assert "Apple Store" in mall.graph["Nike Store"]
    assert mall.graph["Apple Store"]["Nike Store"] == 10.5
    assert mall.graph["Nike Store"]["Apple Store"] == 10.5

def test_add_connection_nonexistent_store():
    """Test adding a connection with a nonexistent store raises an error"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    
    with pytest.raises(ValueError, match="Both stores must exist in the mall map before adding a connection"):
        mall.add_connection("Apple Store", "Nike Store", 10.5)

def test_add_negative_distance():
    """Test adding a connection with negative distance raises an error"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    mall.add_store("Nike Store")
    
    with pytest.raises(ValueError, match="Distance must be non-negative"):
        mall.add_connection("Apple Store", "Nike Store", -5)

def test_find_shortest_path_same_store():
    """Test finding path to the same store"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    
    path = mall.find_shortest_path("Apple Store", "Apple Store")
    assert path == ["Apple Store"]

def test_find_shortest_path_direct_connection():
    """Test finding path with a direct connection"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    mall.add_store("Nike Store")
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    
    path = mall.find_shortest_path("Apple Store", "Nike Store")
    assert path == ["Apple Store", "Nike Store"]

def test_find_shortest_path_multiple_stores():
    """Test finding path through multiple stores"""
    mall = MallGraph()
    # Setup a more complex graph
    stores = ["Apple Store", "Nike Store", "Zara", "Food Court", "Restroom"]
    for store in stores:
        mall.add_store(store)
    
    # Add connections
    mall.add_connection("Apple Store", "Nike Store", 10)
    mall.add_connection("Nike Store", "Zara", 15)
    mall.add_connection("Apple Store", "Food Court", 20)
    mall.add_connection("Food Court", "Zara", 5)
    mall.add_connection("Food Court", "Restroom", 7)
    
    # Path from Apple Store to Zara via Food Court
    path = mall.find_shortest_path("Apple Store", "Zara")
    assert path == ["Apple Store", "Food Court", "Zara"]

def test_find_shortest_path_nonexistent_start():
    """Test finding path with a nonexistent start store"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    
    with pytest.raises(ValueError, match="Start store Nordstrom does not exist in the mall map"):
        mall.find_shortest_path("Nordstrom", "Apple Store")

def test_find_shortest_path_nonexistent_end():
    """Test finding path with a nonexistent end store"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    
    with pytest.raises(ValueError, match="End store Nordstrom does not exist in the mall map"):
        mall.find_shortest_path("Apple Store", "Nordstrom")

def test_find_shortest_path_no_path():
    """Test finding path with no possible connection"""
    mall = MallGraph()
    mall.add_store("Apple Store")
    mall.add_store("Nike Store")
    
    path = mall.find_shortest_path("Apple Store", "Nike Store")
    assert path is None