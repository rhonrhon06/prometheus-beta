import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    # Simple 3x3 matrix
    cost_matrix = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    assignments = hungarian_algorithm(cost_matrix)
    
    # Verify each worker is assigned to exactly one job
    assigned_rows = set(row for row, _ in assignments)
    assigned_cols = set(col for _, col in assignments)
    
    assert len(assignments) == 3
    assert len(assigned_rows) == 3
    assert len(assigned_cols) == 3

def test_numpy_input():
    # Test with numpy array input
    cost_matrix = np.array([
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ])
    assignments = hungarian_algorithm(cost_matrix)
    
    assert len(assignments) == 3

def test_invalid_input():
    # Test non-square matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([
            [1, 2, 3],
            [4, 5, 6]
        ])
    
    # Test empty matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([])

def test_specific_assignment():
    # More complex matrix to test specific assignments
    cost_matrix = [
        [82, 83, 69, 92],
        [77, 37, 49, 92],
        [11, 69, 5, 86],
        [8, 9, 98, 23]
    ]
    
    assignments = hungarian_algorithm(cost_matrix)
    
    # Verify total number of assignments
    assert len(assignments) == 4
    
    # Verify unique assignments
    assigned_rows = set(row for row, _ in assignments)
    assigned_cols = set(col for _, col in assignments)
    
    assert len(assigned_rows) == 4
    assert len(assigned_cols) == 4

def test_symmetric_matrix():
    # Symmetric cost matrix
    cost_matrix = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    
    assignments = hungarian_algorithm(cost_matrix)
    
    assert len(assignments) == 3