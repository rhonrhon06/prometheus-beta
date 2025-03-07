import pytest
import logging
import time
import json
import os
from src.browser_performance import BrowserPerformanceLogger

class TestBrowserPerformanceLogger:
    def setup_method(self):
        # Create a temporary log file for testing
        self.log_file = 'test_performance_log.txt'
        self.logger = BrowserPerformanceLogger(log_file=self.log_file)
    
    def teardown_method(self):
        # Remove the temporary log file after each test
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
    
    def test_create_performance_metrics_basic(self):
        # Test creating basic performance metrics
        metrics = self.logger.create_performance_metrics(
            dom_load_time=0.5, 
            render_time=0.3, 
            total_load_time=0.8
        )
        
        assert 'dom_load_time' in metrics
        assert 'render_time' in metrics
        assert 'total_load_time' in metrics
        assert 'timestamp' in metrics
        assert metrics['dom_load_time'] == 0.5
        assert metrics['render_time'] == 0.3
        assert metrics['total_load_time'] == 0.8
    
    def test_create_performance_metrics_with_additional(self):
        # Test creating metrics with additional data
        additional = {'memory_usage': 100, 'cpu_load': 50}
        metrics = self.logger.create_performance_metrics(
            dom_load_time=0.5, 
            render_time=0.3, 
            total_load_time=0.8,
            additional_metrics=additional
        )
        
        assert metrics['memory_usage'] == 100
        assert metrics['cpu_load'] == 50
    
    def test_create_performance_metrics_negative_times(self):
        # Test that negative times raise a ValueError
        with pytest.raises(ValueError, match="Performance time metrics cannot be negative"):
            self.logger.create_performance_metrics(
                dom_load_time=-0.5, 
                render_time=0.3, 
                total_load_time=0.8
            )
    
    def test_log_rendering_metrics(self):
        # Test logging rendering metrics
        metrics = {
            'dom_load_time': 0.5,
            'render_time': 0.3,
            'total_load_time': 0.8,
            'additional_data': 'test'
        }
        
        # Capture logging output
        with self.capture_logs() as captured:
            self.logger.log_rendering_metrics(metrics)
        
        # Check that the metrics were logged
        assert len(captured) > 0
        logged_message = captured[0]
        assert 'Browser Rendering Metrics' in logged_message
        
        # Verify the logged metrics can be parsed as JSON
        json_part = logged_message.split(': ', 1)[1]
        parsed_metrics = json.loads(json_part)
        assert parsed_metrics == metrics
    
    def test_log_rendering_metrics_empty(self):
        # Test logging empty metrics raises an error
        with pytest.raises(ValueError, match="Performance metrics cannot be empty"):
            self.logger.log_rendering_metrics({})
    
    def test_log_rendering_metrics_missing_keys(self):
        # Test logging metrics with missing required keys
        with pytest.raises(ValueError, match="Missing required metric"):
            self.logger.log_rendering_metrics({
                'some_random_metric': 1.0
            })
    
    def capture_logs(self):
        """
        Context manager to capture log messages for testing.
        """
        class LogCapture:
            def __init__(self):
                self.captured = []
            
            def write(self, message):
                self.captured.append(message)
            
            def __iter__(self):
                return iter(self.captured)
        
        class CaptureHandler(logging.Handler):
            def __init__(self, capture):
                super().__init__()
                self.capture = capture
            
            def emit(self, record):
                msg = self.format(record)
                self.capture.write(msg)
        
        capture = LogCapture()
        handler = CaptureHandler(capture)
        handler.setFormatter(logging.Formatter('%(message)s'))
        
        # Temporarily add capture handler
        self.logger.logger.addHandler(handler)
        
        class LogCaptureContext:
            def __init__(self, logger, handler, capture):
                self.logger = logger
                self.handler = handler
                self.capture = capture
            
            def __enter__(self):
                return self.capture.captured
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                self.logger.logger.removeHandler(self.handler)
        
        return LogCaptureContext(self.logger, handler, capture)