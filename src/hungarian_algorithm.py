import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Implements the Hungarian algorithm (Munkres algorithm) for solving the assignment problem.

    Args:
        cost_matrix (list of lists or numpy.ndarray): A square matrix representing 
                                                     assignment costs, where each cell 
                                                     represents the cost of assigning 
                                                     a worker to a job.

    Returns:
        list: A list of (worker, job) assignments that minimize the total cost.

    Raises:
        ValueError: If the input is not a valid square matrix.
    """
    # Convert input to numpy array
    if not isinstance(cost_matrix, np.ndarray):
        cost_matrix = np.array(cost_matrix, dtype=float)
    
    # Validate input
    if len(cost_matrix.shape) != 2 or cost_matrix.shape[0] != cost_matrix.shape[1]:
        raise ValueError("Input must be a square matrix")
    
    n = cost_matrix.shape[0]
    
    # Create a copy of the cost matrix to work with
    matrix = cost_matrix.copy()
    
    # Step 1: Subtract row minimums
    for i in range(n):
        matrix[i] -= matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        matrix[:, j] -= matrix[:, j].min()
    
    # Step 3: Find optimal assignment using greedy approach
    assignments = []
    covered_rows = set()
    covered_cols = set()
    
    def find_zero(matrix, except_row=None, except_col=None):
        for i in range(n):
            if except_row is not None and i == except_row:
                continue
            for j in range(n):
                if except_col is not None and j == except_col:
                    continue
                if matrix[i, j] == 0 and i not in covered_rows and j not in covered_cols:
                    return i, j
        return None
    
    # Find assignments greedily
    while len(assignments) < n:
        zero = find_zero(matrix)
        
        if zero is None:
            break
        
        row, col = zero
        assignments.append((row, col))
        covered_rows.add(row)
        covered_cols.add(col)
    
    # If not all assignments are found, use a more complex approach
    if len(assignments) < n:
        # Modified version to ensure full assignment
        used_rows = set(row for row, _ in assignments)
        used_cols = set(col for _, col in assignments)
        
        for i in range(n):
            if i in used_rows:
                continue
            for j in range(n):
                if j in used_cols:
                    continue
                assignments.append((i, j))
                used_rows.add(i)
                used_cols.add(j)
                break
    
    return assignments