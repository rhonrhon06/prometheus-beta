import time
import json
import logging
from typing import Dict, Any, Optional

class BrowserPerformanceLogger:
    """
    A class to log browser rendering performance metrics.
    
    This logger captures key performance indicators related to browser rendering,
    including timing information and potential performance bottlenecks.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the performance logger.
        
        Args:
            log_file (Optional[str]): Path to the log file. If None, logs to console.
        """
        # Configure logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Create file handler if log_file is provided
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        else:
            # If no log file, use console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
    
    def log_rendering_metrics(self, metrics: Dict[str, Any]) -> None:
        """
        Log browser rendering performance metrics.
        
        Args:
            metrics (Dict[str, Any]): A dictionary of performance metrics to log.
        
        Raises:
            ValueError: If metrics dictionary is empty or None.
        """
        # Validate input
        if not metrics:
            raise ValueError("Performance metrics cannot be empty")
        
        # Validate required keys
        required_keys = ['dom_load_time', 'render_time', 'total_load_time']
        for key in required_keys:
            if key not in metrics:
                raise ValueError(f"Missing required metric: {key}")
        
        try:
            # Convert metrics to JSON for structured logging
            metrics_json = json.dumps(metrics)
            
            # Log the performance metrics
            self.logger.info(f"Browser Rendering Metrics: {metrics_json}")
        except Exception as e:
            self.logger.error(f"Error logging performance metrics: {str(e)}")
    
    def create_performance_metrics(
        self, 
        dom_load_time: float, 
        render_time: float, 
        total_load_time: float, 
        additional_metrics: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a standardized performance metrics dictionary.
        
        Args:
            dom_load_time (float): Time taken to load the DOM (in seconds)
            render_time (float): Time taken to render the page (in seconds)
            total_load_time (float): Total page load time (in seconds)
            additional_metrics (Optional[Dict[str, Any]]): Additional performance metrics
        
        Returns:
            Dict[str, Any]: Standardized performance metrics dictionary
        
        Raises:
            ValueError: If any time metrics are negative
        """
        # Validate time metrics
        if dom_load_time < 0 or render_time < 0 or total_load_time < 0:
            raise ValueError("Performance time metrics cannot be negative")
        
        # Create base metrics dictionary
        metrics = {
            'dom_load_time': dom_load_time,
            'render_time': render_time,
            'total_load_time': total_load_time,
            'timestamp': time.time()
        }
        
        # Add additional metrics if provided
        if additional_metrics:
            metrics.update(additional_metrics)
        
        return metrics