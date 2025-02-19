def solve_knights_tour(start_x, start_y):
    """
    Solve the Knight's Tour problem on an 8x8 chessboard.
    
    Args:
        start_x (int): Starting x-coordinate (0-7)
        start_y (int): Starting y-coordinate (0-7)
    
    Returns:
        list: A list of (x, y) tuples representing the knight's moves 
              that visit every square exactly once, or None if no solution exists
    """
    # All possible knight moves
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    # 8x8 board
    board_size = 8
    
    # Validate start position
    if not (0 <= start_x < board_size and 0 <= start_y < board_size):
        raise ValueError("Start position must be within 8x8 board")
    
    def is_valid_move(x, y, board):
        """Check if move is within board and not visited"""
        return (0 <= x < board_size and 
                0 <= y < board_size and 
                board[y][x] == -1)
    
    def solve_tour(x, y, move_count, board, tour):
        """Recursive backtracking solution"""
        # If we've made 64 moves, we've visited every square
        if move_count == board_size * board_size:
            return tour
        
        # Try all possible knight moves
        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            
            # Check if next move is valid
            if is_valid_move(next_x, next_y, board):
                # Mark the square
                board[next_y][next_x] = move_count
                tour.append((next_x, next_y))
                
                # Recursively try to complete the tour
                result = solve_tour(next_x, next_y, move_count + 1, board, tour)
                
                # If a solution is found, return it
                if result:
                    return result
                
                # Backtrack
                board[next_y][next_x] = -1
                tour.pop()
        
        return None
    
    # Initialize board and tour
    board = [[-1] * board_size for _ in range(board_size)]
    board[start_y][start_x] = 0
    tour = [(start_x, start_y)]
    
    # Solve the tour
    solution = solve_tour(start_x, start_y, 1, board, tour)
    
    return solution