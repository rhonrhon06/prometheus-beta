from typing import Dict, List, Optional, Tuple, Union
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
            TypeError: If store is not a string
            ValueError: If store already exists in the graph
        """
        if not isinstance(store, str):
            raise TypeError("Store name must be a string")
        
        if not store.strip():
            raise ValueError("Store name cannot be empty")
        
        if store in self.graph:
            raise ValueError(f"Store {store} already exists in the mall map")
        
        self.graph[store] = {}
    
    def add_connection(self, store1: str, store2: str, distance: Union[int, float]) -> None:
        """
        Add a connection between two stores with a given distance.
        
        Args:
            store1 (str): First store name
            store2 (str): Second store name
            distance (Union[int, float]): Distance between the stores
        
        Raises:
            TypeError: If inputs are of incorrect type
            ValueError: If stores do not exist or distance is invalid
        """
        if not isinstance(store1, str) or not isinstance(store2, str):
            raise TypeError("Store names must be strings")
        
        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be a number")
        
        if store1 not in self.graph or store2 not in self.graph:
            raise ValueError("Both stores must exist in the mall map before adding a connection")
        
        if distance < 0:
            raise ValueError("Distance must be non-negative")
        
        self.graph[store1][store2] = float(distance)
        self.graph[store2][store1] = float(distance)  # Assume undirected graph
    
    def find_shortest_path(self, start: str, end: str) -> Optional[Tuple[List[str], float]]:
        """
        Find the shortest path between two stores using Dijkstra's algorithm.
        
        Args:
            start (str): Starting store name
            end (str): Destination store name
        
        Returns:
            Optional[Tuple[List[str], float]]: Tuple of (path, total_distance), or None if no path exists
        
        Raises:
            ValueError: If start or end store does not exist
        """
        # Validate input stores exist
        if start not in self.graph:
            raise ValueError(f"Start store {start} does not exist in the mall map")
        if end not in self.graph:
            raise ValueError(f"End store {end} does not exist in the mall map")
        
        # If start and end are the same, return a list with just that store and 0 distance
        if start == end:
            return [start], 0.0
        
        # Initialize distances and predecessors
        distances = {store: float('inf') for store in self.graph}
        distances[start] = 0
        predecessors = {store: None for store in self.graph}
        
        # Priority queue to track minimum distances
        pq = [(0, start)]
        
        while pq:
            current_distance, current_store = heapq.heappop(pq)
            
            # Skip if we've found a longer path
            if current_distance > distances[current_store]:
                continue
            
            # If we've reached the destination, reconstruct and return the path
            if current_store == end:
                path = []
                total_distance = 0
                while current_store is not None:
                    path.append(current_store)
                    if len(path) > 1:
                        # Add distance between current store and previous store
                        total_distance += self.graph[path[-1]][path[-2]]
                    current_store = predecessors[current_store]
                return list(reversed(path)), total_distance
            
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