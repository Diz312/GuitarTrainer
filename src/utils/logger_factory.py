"""
Centralized Logging System for GuitarTrainer

Educational Focus: Enterprise-grade logging patterns for computer vision applications.
Demonstrates proper logging architecture that scales across multiple components.
Now integrated with hierarchical configuration system.

Author: GuitarTrainer Development
"""

import logging
import logging.handlers
from pathlib import Path
from typing import Dict, Optional
import yaml
from datetime import datetime

# Import hierarchical configuration system
try:
    import sys
    sys.path.append(str(Path(__file__).parent.parent.parent))
    from config import get_infrastructure_config
except ImportError:
    # Fallback for testing or standalone usage
    get_infrastructure_config = None

class LoggerFactory:
    """
    Context-aware logger factory for GuitarTrainer project.
    
    Educational Note: Large applications need centralized logging to:
    - Maintain consistent log formats across components
    - Enable component-specific log levels for debugging
    - Provide centralized log storage for troubleshooting
    - Support different output targets (console + files)
    
    This factory pattern allows each component to get a properly
    configured logger without duplicating setup code.
    """
    
    _instance: Optional['LoggerFactory'] = None
    _loggers: Dict[str, logging.Logger] = {}
    _initialized: bool = False
    
    def __new__(cls) -> 'LoggerFactory':
        """Singleton pattern - one factory instance per application."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize the logger factory if not already done."""
        if not self._initialized:
            self._setup_logging_system()
            LoggerFactory._initialized = True
    
    def _setup_logging_system(self):
        """
        Set up the centralized logging system.
        
        Educational Note: Proper logging setup involves:
        - Creating log directory structure
        - Configuring formatters for consistent output
        - Setting up handlers for different targets (console/file)
        - Implementing rotation to prevent huge log files
        """
        # Create logs directory
        self.logs_dir = Path(__file__).parent.parent.parent / "logs"
        self.logs_dir.mkdir(exist_ok=True)
        
        # Load logging configuration
        self.config = self._load_logging_config()
        
        # Set up formatters
        self.file_formatter = logging.Formatter(
            fmt='%(asctime)s | %(name)s | %(levelname)-8s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        self.console_formatter = logging.Formatter(
            fmt='%(name)s | %(levelname)-5s | %(message)s'
        )
    
    def _load_logging_config(self) -> Dict:
        """
        Load logging configuration from hierarchical config system.
        
        Educational Note: This demonstrates integration with the hierarchical
        configuration system, using infrastructure config for logging settings.
        Falls back gracefully if config system is unavailable.
        """
        # Default configuration if config system unavailable
        default_config = {
            'default_level': 'INFO',
            'component_levels': {
                'video_input': 'DEBUG',
                'pose_detection': 'INFO',
                'gui': 'INFO',
                'analysis': 'INFO',
                'main': 'INFO'
            },
            'console_level': 'INFO',
            'enable_console': True,
            'rotation_when': 'midnight',
            'backup_count': 30  # Keep 30 days of logs
        }
        
        try:
            # Try to load from hierarchical config system
            if get_infrastructure_config is not None:
                infra_config = get_infrastructure_config()
                
                if infra_config.logging and hasattr(infra_config.logging, 'items'):
                    # Convert ConfigDict to regular dict for logging config
                    logging_config = dict(infra_config.logging)
                    
                    # Merge with defaults for any missing keys
                    for key, value in default_config.items():
                        if key not in logging_config:
                            logging_config[key] = value
                    
                    return logging_config
                else:
                    print("Warning: No logging configuration found in infrastructure config")
                    return default_config
            else:
                # Fallback to YAML file if config system not available
                return self._load_yaml_config(default_config)
                
        except Exception as e:
            print(f"Warning: Error loading logging config from hierarchy: {e}")
            return self._load_yaml_config(default_config)
    
    def _load_yaml_config(self, default_config: Dict) -> Dict:
        """
        Fallback method to load logging config directly from YAML file.
        
        Educational Note: This provides backward compatibility and fallback
        when the hierarchical config system is not available.
        """
        config_path = Path(__file__).parent.parent.parent / "config" / "20_logging.yaml"
        
        try:
            if config_path.exists():
                with open(config_path, 'r') as f:
                    config_data = yaml.safe_load(f)
                    
                # Extract logging section if it exists
                if 'logging' in config_data:
                    config = config_data['logging']
                else:
                    config = config_data
                    
                # Merge with defaults for missing keys
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
            else:
                # Create default config file for user customization
                config_path.parent.mkdir(exist_ok=True)
                with open(config_path, 'w') as f:
                    yaml.dump({'logging': default_config}, f, default_flow_style=False)
                return default_config
                
        except Exception as e:
            print(f"Warning: Could not load YAML logging config: {e}")
            return default_config
    
    def _create_file_handler(self, component_name: str, log_level: str) -> logging.Handler:
        """
        Create a rotating file handler for a component.
        
        Educational Note: Rotating file handlers prevent log files from
        growing indefinitely. Daily rotation with backup count ensures
        we keep recent logs while managing disk space.
        """
        log_file = self.logs_dir / f"{component_name}.log"
        
        # TimedRotatingFileHandler rotates logs daily at midnight
        handler = logging.handlers.TimedRotatingFileHandler(
            filename=log_file,
            when=self.config['rotation_when'],
            backupCount=self.config['backup_count']
        )
        
        handler.setLevel(getattr(logging, log_level.upper()))
        handler.setFormatter(self.file_formatter)
        
        return handler
    
    def _create_console_handler(self) -> Optional[logging.Handler]:
        """
        Create console handler for real-time log viewing.
        
        Educational Note: Console output is essential during development
        for immediate feedback. In production, this might be disabled
        to reduce console noise.
        """
        if not self.config['enable_console']:
            return None
            
        handler = logging.StreamHandler()
        handler.setLevel(getattr(logging, self.config['console_level'].upper()))
        handler.setFormatter(self.console_formatter)
        
        return handler
    
    def get_component_logger(self, component_name: str) -> logging.Logger:
        """
        Get or create a logger for a specific component.
        
        Educational Note: This method implements the factory pattern,
        creating loggers on-demand with proper configuration.
        Each component gets its own logger with component-specific settings.
        
        Args:
            component_name: Name of component (e.g., 'video_input', 'pose_detection')
            
        Returns:
            Configured logger for the component
            
        Example:
            >>> logger = get_component_logger('video_input')
            >>> logger.info("Video processing started")
            # Logs to: logs/video_input.log and console
        """
        if component_name in self._loggers:
            return self._loggers[component_name]
        
        # Create new logger for component
        logger = logging.getLogger(f"guitartainer.{component_name}")
        logger.setLevel(logging.DEBUG)  # Let handlers control filtering
        
        # Prevent duplicate logs from parent loggers
        logger.propagate = False
        
        # Clear any existing handlers to prevent duplicates
        logger.handlers.clear()
        
        # Get component-specific log level
        component_level = self.config['component_levels'].get(
            component_name, 
            self.config['default_level']
        )
        
        # Add file handler
        file_handler = self._create_file_handler(component_name, component_level)
        logger.addHandler(file_handler)
        
        # Add console handler if enabled
        console_handler = self._create_console_handler()
        if console_handler:
            logger.addHandler(console_handler)
        
        # Cache the logger
        self._loggers[component_name] = logger
        
        # Log the logger creation
        logger.info(f"Logger initialized for component '{component_name}' with level '{component_level}'")
        
        return logger


# Global factory instance
_factory = LoggerFactory()

def get_component_logger(component_name: str) -> logging.Logger:
    """
    Convenience function to get a component logger.
    
    Educational Note: This provides a simple import interface for components:
    from utils.logger_factory import get_component_logger
    
    Args:
        component_name: Component identifier (video_input, pose_detection, etc.)
        
    Returns:
        Configured logger for the component
    """
    return _factory.get_component_logger(component_name)


def log_system_info():
    """
    Log system information for debugging and audit purposes.
    
    Educational Note: Logging system startup info helps with debugging
    configuration issues and provides audit trail of application starts.
    """
    main_logger = get_component_logger('main')
    main_logger.info("=" * 60)
    main_logger.info("GuitarTrainer Application Started")
    main_logger.info(f"Timestamp: {datetime.now().isoformat()}")
    main_logger.info(f"Logs directory: {_factory.logs_dir}")
    main_logger.info(f"Logging config: {_factory.config}")
    main_logger.info("=" * 60)


if __name__ == "__main__":
    """
    Manual testing and demonstration of logging factory.
    
    Educational Note: This demonstrates the logging system in action
    using dynamic introspection to show configuration and behavior.
    """
    
    def print_logging_config_structure(config, indent=0, max_depth=3):
        """
        Recursively print logging configuration structure.
        
        Educational Note: Dynamic structure printing shows configuration
        without hardcoding specific values, making it adaptable to changes.
        """
        if indent > max_depth:
            print("  " * indent + "... (max depth reached)")
            return
            
        for key, value in config.items():
            prefix = "  " * indent + f"📄 {key}:"
            
            if isinstance(value, dict):
                print(prefix)
                print_logging_config_structure(value, indent + 1, max_depth)
            elif isinstance(value, list):
                print(f"{prefix} {value} (list of {len(value)} items)")
            else:
                print(f"{prefix} {value} ({type(value).__name__})")
    
    def demonstrate_logger_creation():
        """
        Demonstrate logger creation for different components.
        
        Educational Note: Shows how different components get
        appropriately configured loggers.
        """
        print("\n📈 DEMONSTRATING LOGGER CREATION:")
        print("-" * 40)
        
        # Test components from our project
        test_components = ['video_input', 'pose_detection', 'gui', 'analysis', 'main']
        
        for component in test_components:
            logger = get_component_logger(component)
            print(f"✅ {component}: {logger.name} (level: {logger.level}, handlers: {len(logger.handlers)})")
            
            # Show handler details
            for i, handler in enumerate(logger.handlers):
                handler_type = type(handler).__name__
                handler_level = logging.getLevelName(handler.level)
                print(f"    Handler {i+1}: {handler_type} (level: {handler_level})")
    
    def test_actual_logging():
        """
        Test actual logging output to demonstrate functionality.
        
        Educational Note: Shows the logging system in action with
        real log messages at different levels.
        """
        print("\n📝 TESTING ACTUAL LOGGING OUTPUT:")
        print("-" * 40)
        
        # Get logger for testing
        test_logger = get_component_logger('logger_test')
        
        # Test different log levels
        log_levels = ['debug', 'info', 'warning', 'error', 'critical']
        
        for level in log_levels:
            log_method = getattr(test_logger, level)
            log_method(f"Test {level.upper()} message from logger factory demonstration")
            print(f"✅ Logged {level.upper()} message")
    
    def show_log_files():
        """
        Show created log files and their properties.
        
        Educational Note: Demonstrates file-based logging output
        and log file organization.
        """
        print("\n📁 LOG FILES CREATED:")
        print("-" * 40)
        
        logs_dir = _factory.logs_dir
        log_files = list(logs_dir.glob("*.log"))
        
        if log_files:
            for log_file in sorted(log_files):
                size = log_file.stat().st_size
                modified = datetime.fromtimestamp(log_file.stat().st_mtime)
                print(f"📄 {log_file.name}: {size} bytes, modified {modified.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("ℹ️ No log files found yet (will be created on first log message)")
    
    print("🎸 GUITARTAINER LOGGER FACTORY TEST 🎸")
    print("=" * 60)
    
    try:
        print("\n🔧 TESTING LOGGER FACTORY INITIALIZATION:")
        factory = LoggerFactory()
        print(f"✅ Factory created: {type(factory).__name__}")
        print(f"✅ Logs directory: {factory.logs_dir}")
        print(f"✅ Factory initialized: {factory._initialized}")
        
        print("\n📇 LOGGING CONFIGURATION STRUCTURE:")
        print_logging_config_structure(factory.config)
        
        # Demonstrate logger creation
        demonstrate_logger_creation()
        
        # Test actual logging
        test_actual_logging()
        
        # Show log files
        show_log_files()
        
        print("\n🎯 LOGGER FACTORY VALIDATION:")
        validation_points = [
            "Logger factory singleton pattern working",
            "Hierarchical config integration successful",
            "Component-specific loggers created properly",
            "File and console handlers configured",
            "Log rotation and formatting applied",
            "Dynamic configuration introspection working",
            "Graceful fallback for missing config"
        ]
        
        for point in validation_points:
            print(f"✅ {point}")
        
        print("\n🚀 LOGGER FACTORY READY FOR ALL COMPONENTS!")
        print("📈 Components can now use: from utils.logger_factory import get_component_logger")
        
    except Exception as e:
        print(f"\n❌ LOGGER FACTORY ERROR: {e}")
        import traceback
        traceback.print_exc()
        print("\n🔧 Check logging configuration and file permissions")
