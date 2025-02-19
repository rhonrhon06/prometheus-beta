import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from knights_tour import solve_knights_tour

def test_knights_tour_valid_start():
    """Test a valid Knight's Tour from a starting position"""
    # Test starts from different positions
    starts = [(0, 0), (3, 3), (7, 7)]
    
    for start_x, start_y in starts:
        tour = solve_knights_tour(start_x, start_y)
        
        # Verify tour exists
        assert tour is not None, f"No tour found for start ({start_x}, {start_y})"
        
        # Verify tour length is 64 (all squares visited)
        assert len(tour) == 64, f"Tour length incorrect for start ({start_x}, {start_y})"
        
        # Verify no repeated squares
        assert len(set(tour)) == 64, f"Repeated squares in tour for start ({start_x}, {start_y})"
        
        # Verify the tour starts at the given position
        assert tour[0] == (start_x, start_y), f"Tour does not start at ({start_x}, {start_y})"

def test_knights_tour_move_validity():
    """Test the validity of moves in the Knight's Tour"""
    # Choose an arbitrary valid start
    start_x, start_y = 3, 3
    tour = solve_knights_tour(start_x, start_y)
    
    # All possible knight moves
    knight_moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    # Check each move is a valid knight move
    for i in range(len(tour) - 1):
        x1, y1 = tour[i]
        x2, y2 = tour[i+1]
        
        # Calculate move
        dx, dy = x2 - x1, y2 - y1
        
        # Check if the move is a valid knight's move
        assert (dx, dy) in knight_moves, f"Invalid move from {tour[i]} to {tour[i+1]}"

def test_knights_tour_invalid_start():
    """Test invalid start positions"""
    # Test out-of-bounds positions
    invalid_starts = [(-1, 0), (8, 0), (0, -1), (0, 8)]
    
    for start_x, start_y in invalid_starts:
        with pytest.raises(ValueError, match="Start position must be within 8x8 board"):
            solve_knights_tour(start_x, start_y)

def test_knights_tour_board_coverage():
    """Ensure the entire board is covered in order"""
    start_x, start_y = 0, 0
    tour = solve_knights_tour(start_x, start_y)
    
    # Create a board to mark visited squares
    board = [[False] * 8 for _ in range(8)]
    
    # Mark each square as visited in order
    for x, y in tour:
        # Ensure square hasn't been visited before
        assert not board[y][x], f"Square ({x}, {y}) visited twice"
        board[y][x] = True
    
    # Verify all squares are visited
    for row in board:
        assert all(row), "Not all squares were visited"