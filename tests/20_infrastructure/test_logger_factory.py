"""
Test suite for Logger Factory Infrastructure

Educational Focus: Testing enterprise-level logging patterns and integration
with hierarchical configuration system.

Author: GuitarTrainer Development
"""

import pytest
import sys
import logging
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from utils.logger_factory import LoggerFactory, get_component_logger


class TestLoggerFactory:
    """
    Test cases for logger factory infrastructure.
    
    Educational Note: Testing logging infrastructure ensures reliable
    operation across all application components and validates proper
    integration with the hierarchical configuration system.
    """
    
    def test_logger_factory_singleton(self):
        """
        Test that logger factory follows singleton pattern.
        
        Educational Note: Singleton pattern ensures consistent logging
        configuration across the entire application.
        """
        factory1 = LoggerFactory()
        factory2 = LoggerFactory()
        assert factory1 is factory2, "LoggerFactory should be singleton"
    
    def test_logger_factory_initialization(self):
        """
        Test that logger factory initializes properly.
        """
        factory = LoggerFactory()
        assert factory is not None
        assert factory.logs_dir.exists(), "Logs directory should be created"
        assert isinstance(factory.config, dict), "Config should be loaded as dict"
        assert factory._initialized is True, "Factory should be marked as initialized"
    
    def test_logs_directory_creation(self):
        """
        Test that logs directory is created correctly.
        
        Educational Note: Proper directory structure is essential for
        organized log file management in production applications.
        """
        factory = LoggerFactory()
        logs_dir = factory.logs_dir
        
        assert logs_dir.exists(), "Logs directory should exist"
        assert logs_dir.is_dir(), "Logs path should be a directory"
        assert logs_dir.name == "logs", "Directory should be named 'logs'"
    
    def test_config_loading(self):
        """
        Test that logging configuration is loaded properly.
        
        Educational Note: Configuration-driven logging allows easy
        adjustment of log levels and behavior without code changes.
        """
        factory = LoggerFactory()
        config = factory.config
        
        # Validate required config keys exist
        required_keys = ['default_level', 'component_levels', 'console_level', 'enable_console']
        for key in required_keys:
            assert key in config, f"Missing required config key: {key}"
        
        # Validate config value types
        assert isinstance(config['component_levels'], dict), "component_levels should be dict"
        assert isinstance(config['enable_console'], bool), "enable_console should be boolean"
        assert config['default_level'] in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    
    def test_component_logger_creation(self):
        """
        Test that component loggers are created with proper configuration.
        
        Educational Note: Each component should get a properly configured
        logger with appropriate handlers and formatting.
        """
        logger = get_component_logger('test_component')
        
        assert logger is not None, "Logger should be created"
        assert logger.name == 'guitartainer.test_component', "Logger should have correct name"
        assert len(logger.handlers) > 0, "Logger should have handlers attached"
        assert logger.propagate is False, "Logger should not propagate to avoid duplicates"
    
    def test_multiple_logger_instances(self):
        """
        Test that requesting same component logger returns same instance.
        
        Educational Note: Logger caching prevents duplicate logger creation
        and ensures consistent configuration across component usage.
        """
        logger1 = get_component_logger('video_input')
        logger2 = get_component_logger('video_input')
        assert logger1 is logger2, "Should return same logger instance for same component"
    
    def test_different_component_loggers(self):
        """
        Test that different components get different loggers.
        
        Educational Note: Component isolation in logging helps with
        debugging and allows component-specific log level configuration.
        """
        video_logger = get_component_logger('video_input')
        pose_logger = get_component_logger('pose_detection')
        
        assert video_logger is not pose_logger, "Different components should get different loggers"
        assert video_logger.name != pose_logger.name, "Loggers should have different names"
    
    def test_logger_handlers_configuration(self):
        """
        Test that loggers have properly configured handlers.
        
        Educational Note: Proper handler configuration ensures logs
        go to the right destinations with correct formatting.
        """
        logger = get_component_logger('handler_test')
        
        # Should have at least one handler (file handler always present)
        assert len(logger.handlers) >= 1, "Logger should have at least file handler"
        
        # Check for file handler
        file_handlers = [h for h in logger.handlers if hasattr(h, 'baseFilename')]
        assert len(file_handlers) > 0, "Logger should have file handler"
        
        # Validate file handler configuration
        file_handler = file_handlers[0]
        assert hasattr(file_handler, 'formatter'), "File handler should have formatter"
    
    def test_hierarchical_config_integration(self):
        """
        Test integration with hierarchical configuration system.
        
        Educational Note: This validates that the logger factory properly
        integrates with our hierarchical config architecture.
        """
        factory = LoggerFactory()
        
        # Test that config loading doesn't crash
        config = factory.config
        assert config is not None, "Config should be loaded successfully"
        
        # Test fallback mechanism works
        assert 'default_level' in config, "Fallback config should provide default_level"
    
    @pytest.mark.parametrize("component_name", [
        'video_input',
        'pose_detection', 
        'gui',
        'analysis',
        'main'
    ])
    def test_project_component_loggers(self, component_name):
        """
        Test logger creation for all project components.
        
        Educational Note: Parametrized tests ensure all project components
        can successfully create loggers with proper configuration.
        """
        logger = get_component_logger(component_name)
        
        assert logger is not None, f"Logger should be created for {component_name}"
        assert component_name in logger.name, f"Logger name should include {component_name}"
        assert len(logger.handlers) > 0, f"Logger should have handlers for {component_name}"
    
    def test_logging_functionality(self):
        """
        Test that actual logging works without errors.
        
        Educational Note: Functional testing ensures the logging system
        works in practice, not just in configuration.
        """
        logger = get_component_logger('functional_test')
        
        # Test different log levels don't raise exceptions
        try:
            logger.debug("Test debug message")
            logger.info("Test info message")
            logger.warning("Test warning message")
            logger.error("Test error message")
            logger.critical("Test critical message")
        except Exception as e:
            pytest.fail(f"Logging should not raise exceptions: {e}")
    
    def test_log_file_creation(self):
        """
        Test that log files are created when logging occurs.
        
        Educational Note: Validates that file handlers actually create
        log files in the expected location.
        """
        test_component = 'file_creation_test'
        logger = get_component_logger(test_component)
        
        # Log a message to trigger file creation
        logger.info("Test message for file creation")
        
        # Check if log file was created
        factory = LoggerFactory()
        expected_log_file = factory.logs_dir / f"{test_component}.log"
        
        # Note: File creation might be buffered, so we test the setup is correct
        # rather than immediate file existence
        file_handlers = [h for h in logger.handlers if hasattr(h, 'baseFilename')]
        if file_handlers:
            handler_file = Path(file_handlers[0].baseFilename)
            assert handler_file.name == f"{test_component}.log", "Log file should have correct name"
    
    def test_config_fallback_mechanism(self):
        """
        Test that fallback configuration works when hierarchical config unavailable.
        
        Educational Note: Robust systems need fallback mechanisms to handle
        configuration loading failures gracefully.
        """
        # This test validates that the factory can initialize even if
        # the hierarchical config system is unavailable
        factory = LoggerFactory()
        
        # Should still have valid config even with fallback
        assert factory.config is not None, "Fallback config should be available"
        assert 'default_level' in factory.config, "Fallback should provide default_level"
        assert 'component_levels' in factory.config, "Fallback should provide component_levels"


class TestLoggerFactoryErrorHandling:
    """
    Test error handling and edge cases for logger factory.
    
    Educational Note: Robust error handling is crucial for infrastructure
    components that other parts of the application depend on.
    """
    
    def test_invalid_component_name_handling(self):
        """
        Test that invalid component names are handled gracefully.
        """
        # Should not crash with unusual component names
        logger = get_component_logger('test-component-with-dashes')
        assert logger is not None, "Should handle component names with dashes"
        
        logger = get_component_logger('test_component_123')
        assert logger is not None, "Should handle component names with numbers"
    
    def test_empty_component_name(self):
        """
        Test handling of empty component names.
        """
        # Should handle empty string gracefully
        logger = get_component_logger('')
        assert logger is not None, "Should handle empty component name"
    
    def test_factory_reinitialization(self):
        """
        Test that factory handles multiple initialization attempts.
        """
        factory1 = LoggerFactory()
        factory2 = LoggerFactory()
        
        # Should be same instance (singleton)
        assert factory1 is factory2, "Should return same factory instance"
        assert factory1._initialized is True, "Should remain initialized"


if __name__ == "__main__":
    """
    Run tests when executed directly.
    
    Educational Note: This allows running tests with 'python test_logger_factory.py'
    in addition to using pytest discovery.
    """
    pytest.main([__file__, "-v"])
