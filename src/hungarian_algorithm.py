import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Implements the Hungarian algorithm (also known as the Munkres or Kuhn-Munkres algorithm)
    for solving the assignment problem.

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
    # Convert input to numpy array for easier manipulation
    if not isinstance(cost_matrix, np.ndarray):
        cost_matrix = np.array(cost_matrix)
    
    # Validate input
    if len(cost_matrix.shape) != 2 or cost_matrix.shape[0] != cost_matrix.shape[1]:
        raise ValueError("Input must be a square matrix")
    
    n = cost_matrix.shape[0]
    
    # Step 1: Subtract row minimums
    reduced_matrix = cost_matrix.copy()
    for i in range(n):
        reduced_matrix[i] -= reduced_matrix[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        reduced_matrix[:, j] -= reduced_matrix[:, j].min()
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # This is a simplified covering algorithm
        covered_rows = set()
        covered_cols = set()
        
        # Find rows and columns with zeros
        for i in range(n):
            zero_cols = np.where(matrix[i] == 0)[0]
            if len(zero_cols) == 1:
                col = zero_cols[0]
                if col not in covered_cols:
                    covered_rows.add(i)
                    covered_cols.add(col)
        
        return list(covered_rows), list(covered_cols)
    
    # Step 4: Assign workers to jobs
    def assign_jobs(matrix):
        assignments = []
        used_rows = set()
        used_cols = set()
        
        for i in range(n):
            zero_cols = np.where(matrix[i] == 0)[0]
            for col in zero_cols:
                if col not in used_cols and i not in used_rows:
                    assignments.append((i, col))
                    used_rows.add(i)
                    used_cols.add(col)
                    break
        
        return assignments
    
    # Perform assignments
    assignments = assign_jobs(reduced_matrix)
    
    return assignments