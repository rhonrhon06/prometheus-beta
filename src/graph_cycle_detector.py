from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a directed graph contains a cycle.

    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are nodes, values are lists of adjacent nodes.

    Returns:
        bool: True if the graph contains a cycle, False otherwise.

    Raises:
        ValueError: If the input graph is None or not a valid dictionary.
    """
    # Validate input
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    if not isinstance(graph, dict):
        raise ValueError("Graph must be a dictionary")

    def dfs_cycle_check(node: int, visited: Set[int], rec_stack: Set[int]) -> bool:
        """
        Depth-first search to detect cycles in the graph.

        Args:
            node (int): Current node being explored
            visited (Set[int]): Set of nodes already visited
            rec_stack (Set[int]): Set of nodes in the current recursion stack

        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Mark the current node as visited and add to recursion stack
        visited.add(node)
        rec_stack.add(node)

        # Explore all adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor not visited, recursively check
            if neighbor not in visited:
                if dfs_cycle_check(neighbor, visited, rec_stack):
                    return True
            
            # If neighbor is in recursion stack, cycle detected
            elif neighbor in rec_stack:
                return True

        # Remove node from recursion stack
        rec_stack.remove(node)
        return False

    # Check for cycles starting from each unvisited node
    visited = set()
    for node in graph:
        if node not in visited:
            rec_stack = set()
            if dfs_cycle_check(node, visited, rec_stack):
                return True

    return False