import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_graph_with_cycle():
    """Test a graph that contains a cycle"""
    graph = {
        0: [1],
        1: [2],
        2: [0]  # Cycle: 0 -> 1 -> 2 -> 0
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_graph_without_cycle():
    """Test a graph without a cycle"""
    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_empty_graph():
    """Test an empty graph"""
    graph = {}
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_self_loop():
    """Test a graph with a single node pointing to itself"""
    graph = {0: [0]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_complex_graph_with_cycle():
    """Test a more complex graph with a cycle"""
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: [1]  # Cycle: 1 -> 2 -> 3 -> 1
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_complex_graph_without_cycle():
    """Test a more complex graph without a cycle"""
    graph = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [4],
        4: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_none_graph():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError, match="Graph cannot be None"):
        detect_cycle_in_directed_graph(None)

def test_invalid_graph_input():
    """Test that invalid input raises a ValueError"""
    with pytest.raises(ValueError, match="Graph must be a dictionary"):
        detect_cycle_in_directed_graph([1, 2, 3])

def test_disconnected_graph_with_cycle():
    """Test a disconnected graph that contains a cycle"""
    graph = {
        0: [1],
        1: [0],  # Cycle in first component
        2: [3],
        3: [4],
        4: [2]   # Cycle in second component
    }
    assert detect_cycle_in_directed_graph(graph) == True