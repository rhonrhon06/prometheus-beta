from typing import Dict, List, Optional
import heapq

class MallGraph:
    """
    A class representing the mall map as a weighted graph for navigation.
    
    Attributes:
        graph (Dict[str, Dict[str, float]]): Adjacency list representation of the mall map
    """
    
    def __init__(self):
        """
        Initialize an empty mall graph.
        """
        self.graph: Dict[str, Dict[str, float]] = {}
    
    def add_store(self, store: str) -> None:
        """
        Add a store to the mall graph.
        
        Args:
            store (str): Name of the store to add
        
        Raises:
            ValueError: If store already exists in the graph
        """
        if store in self.graph:
            raise ValueError(f"Store {store} already exists in the mall map")
        self.graph[store] = {}
    
    def add_connection(self, store1: str, store2: str, distance: float) -> None:
        """
        Add a connection between two stores with a given distance.
        
        Args:
            store1 (str): First store name
            store2 (str): Second store name
            distance (float): Distance between the stores
        
        Raises:
            ValueError: If either store does not exist in the graph
        """
        if store1 not in self.graph or store2 not in self.graph:
            raise ValueError("Both stores must exist in the mall map before adding a connection")
        
        if distance < 0:
            raise ValueError("Distance must be non-negative")
        
        self.graph[store1][store2] = distance
        self.graph[store2][store1] = distance  # Assume undirected graph
    
    def find_shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        """
        Find the shortest path between two stores using Dijkstra's algorithm.
        
        Args:
            start (str): Starting store name
            end (str): Destination store name
        
        Returns:
            Optional[List[str]]: List of stores in the shortest path, or None if no path exists
        
        Raises:
            ValueError: If start or end store does not exist
        """
        # Validate input stores exist
        if start not in self.graph:
            raise ValueError(f"Start store {start} does not exist in the mall map")
        if end not in self.graph:
            raise ValueError(f"End store {end} does not exist in the mall map")
        
        # If start and end are the same, return a list with just that store
        if start == end:
            return [start]
        
        # Initialize distances and predecessors
        distances = {store: float('inf') for store in self.graph}
        distances[start] = 0
        predecessors = {store: None for store in self.graph}
        
        # Priority queue to track minimum distances
        pq = [(0, start)]
        
        while pq:
            current_distance, current_store = heapq.heappop(pq)
            
            # If we've reached the destination, reconstruct and return the path
            if current_store == end:
                path = []
                while current_store:
                    path.append(current_store)
                    current_store = predecessors[current_store]
                return list(reversed(path))
            
            # If we've found a longer path, skip
            if current_distance > distances[current_store]:
                continue
            
            # Check neighbors
            for neighbor, weight in self.graph[current_store].items():
                distance = current_distance + weight
                
                # If we've found a shorter path, update
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_store
                    heapq.heappush(pq, (distance, neighbor))
        
        # No path found
        return None