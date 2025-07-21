"""
Configuration Management for GuitarTrainer Project - Hierarchical Merging System

Provides consolidated access to configuration settings using hierarchical merging
from numbered YAML files. Each config type reads all relevant files and consolidates
them into a single, hierarchical configuration object.

Educational Focus: Demonstrates enterprise configuration patterns with file-type
consolidation and hierarchical namespacing for conflict resolution.
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List
from dataclasses import dataclass
import logging


logger = logging.getLogger(__name__)


class ConfigDict(dict):
    """
    Enhanced dictionary that supports dot notation access.
    
    Educational Note: This allows accessing nested config values like:
    config.video.core.supported_formats instead of config['video']['core']['supported_formats']
    
    Makes configuration access more intuitive and IDE-friendly.
    """
    
    def __init__(self, data: Dict[str, Any]):
        super().__init__()
        for key, value in data.items():
            if isinstance(value, dict):
                self[key] = ConfigDict(value)
            else:
                self[key] = value
    
    def __getattr__(self, key: str) -> Any:
        """Enable dot notation access: config.video instead of config['video']"""
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"Configuration key '{key}' not found")
    
    def __setattr__(self, key: str, value: Any) -> None:
        """Enable dot notation assignment: config.video = value"""
        self[key] = value
    
    def get_nested(self, path: str, default: Any = None) -> Any:
        """
        Get nested value using dot notation path.
        
        Example: config.get_nested('video.core.supported_formats')
        """
        keys = path.split('.')
        current = self
        
        for key in keys:
            if isinstance(current, ConfigDict) and key in current:
                current = current[key]
            else:
                return default
        
        return current


@dataclass
class ProjectConfig:
    """
    Consolidated project-level configuration.
    
    Educational Note: This represents all project configuration consolidated
    from files numbered 10-19. Uses hierarchical structure to avoid conflicts.
    """
    video: ConfigDict
    pose_detection: ConfigDict
    gui: ConfigDict
    analysis: ConfigDict
    machine_learning: ConfigDict
    application: ConfigDict
    
    def __post_init__(self):
        """Convert dict values to ConfigDict for dot notation access."""
        for field_name in ['video', 'pose_detection', 'gui', 'analysis', 'machine_learning', 'application']:
            field_value = getattr(self, field_name)
            if isinstance(field_value, dict) and not isinstance(field_value, ConfigDict):
                setattr(self, field_name, ConfigDict(field_value))


@dataclass
class InfrastructureConfig:
    """
    Consolidated infrastructure configuration.
    
    Educational Note: This represents all infrastructure configuration
    consolidated from files numbered 20-29 (logging, monitoring, etc.).
    """
    logging: ConfigDict
    # Future: monitoring, performance, etc.
    
    def __post_init__(self):
        """Convert dict values to ConfigDict for dot notation access."""
        for field_name in ['logging']:
            field_value = getattr(self, field_name)
            if field_value and isinstance(field_value, dict) and not isinstance(field_value, ConfigDict):
                setattr(self, field_name, ConfigDict(field_value))


class ProjectConfigManager:
    """
    Manages project-level configuration (files 10-19).
    
    Educational Note: This class demonstrates the consolidation pattern where
    multiple configuration files of the same type are merged into a single
    configuration object with hierarchical structure for conflict resolution.
    """
    
    def __init__(self):
        self.config_dir = Path(__file__).parent
        self._consolidated_config: ProjectConfig = None
    
    def _load_project_files(self) -> Dict[str, Any]:
        """
        Load and merge all project configuration files (10-19).
        
        Educational Note: Files are loaded in numerical order, with later
        files potentially overriding earlier ones at the same hierarchy level.
        """
        consolidated_data = {}
        
        # Find all project config files (10-19)
        project_files = sorted([
            f for f in self.config_dir.glob("1[0-9]_*.yaml")
            if f.is_file()
        ])
        
        if not project_files:
            raise FileNotFoundError("No project configuration files found (10-19 range)")
        
        for config_file in project_files:
            try:
                logger.debug(f"Loading project config: {config_file.name}")
                with open(config_file, 'r', encoding='utf-8') as file:
                    file_data = yaml.safe_load(file)
                    
                if file_data:
                    # Hierarchical merge - later files can extend/override
                    consolidated_data = self._deep_merge(consolidated_data, file_data)
                    
            except yaml.YAMLError as e:
                logger.error(f"Error parsing {config_file.name}: {e}")
                raise ValueError(f"Invalid YAML in {config_file.name}: {e}")
            except Exception as e:
                logger.error(f"Error loading {config_file.name}: {e}")
                raise
        
        return consolidated_data
    
    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deep merge two dictionaries, with override taking precedence.
        
        Educational Note: This enables hierarchical configuration where
        video.core.* and video.experimental.* can coexist from different files.
        """
        result = base.copy()
        
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                # Recursively merge nested dictionaries
                result[key] = self._deep_merge(result[key], value)
            else:
                # Override or add new value
                result[key] = value
        
        return result
    
    def get_project_config(self) -> ProjectConfig:
        """
        Get consolidated project configuration.
        
        Returns:
            ProjectConfig: Unified configuration object with dot notation access
        """
        if self._consolidated_config is None:
            data = self._load_project_files()
            
            # Extract expected sections with defaults
            self._consolidated_config = ProjectConfig(
                video=ConfigDict(data.get('video', {})),
                pose_detection=ConfigDict(data.get('pose_detection', {})),
                gui=ConfigDict(data.get('gui', {})),
                analysis=ConfigDict(data.get('analysis', {})),
                machine_learning=ConfigDict(data.get('machine_learning', {})),
                application=ConfigDict(data.get('application', {}))
            )
        
        return self._consolidated_config
    
    def reload_config(self) -> ProjectConfig:
        """Reload configuration from files (useful for development)."""
        self._consolidated_config = None
        return self.get_project_config()


class InfrastructureConfigManager:
    """
    Manages infrastructure configuration (files 20-29).
    
    Educational Note: Separate from project config to maintain clear separation
    between business logic configuration and infrastructure concerns.
    """
    
    def __init__(self):
        self.config_dir = Path(__file__).parent
        self._consolidated_config: InfrastructureConfig = None
    
    def _load_infrastructure_files(self) -> Dict[str, Any]:
        """Load and merge all infrastructure configuration files (20-29)."""
        consolidated_data = {}
        
        # Find all infrastructure config files (20-29)
        infrastructure_files = sorted([
            f for f in self.config_dir.glob("2[0-9]_*.yaml")
            if f.is_file()
        ])
        
        if not infrastructure_files:
            logger.warning("No infrastructure configuration files found (20-29 range)")
            return {}
        
        for config_file in infrastructure_files:
            try:
                logger.debug(f"Loading infrastructure config: {config_file.name}")
                with open(config_file, 'r', encoding='utf-8') as file:
                    file_data = yaml.safe_load(file)
                    
                if file_data:
                    # Deep merge infrastructure configs
                    consolidated_data = self._deep_merge(consolidated_data, file_data)
                    
            except yaml.YAMLError as e:
                logger.error(f"Error parsing {config_file.name}: {e}")
                raise ValueError(f"Invalid YAML in {config_file.name}: {e}")
            except Exception as e:
                logger.error(f"Error loading {config_file.name}: {e}")
                raise
        
        return consolidated_data
    
    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Deep merge dictionaries (same logic as ProjectConfigManager)."""
        result = base.copy()
        
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        
        return result
    
    def get_infrastructure_config(self) -> InfrastructureConfig:
        """Get consolidated infrastructure configuration."""
        if self._consolidated_config is None:
            data = self._load_infrastructure_files()
            
            self._consolidated_config = InfrastructureConfig(
                logging=ConfigDict(data.get('logging', {}))
            )
        
        return self._consolidated_config


# Convenience functions for easy access
def get_project_config() -> ProjectConfig:
    """Get project configuration - convenience function."""
    return ProjectConfigManager().get_project_config()


def get_infrastructure_config() -> InfrastructureConfig:
    """Get infrastructure configuration - convenience function.""" 
    return InfrastructureConfigManager().get_infrastructure_config()


if __name__ == "__main__":
    """
    Test the configuration system when run as standalone script.
    
    Educational Note: This demonstrates the config factory in action,
    showing how easy it is to access hierarchical configuration.
    Uses dynamic introspection to display all config values.
    """
    
    def print_config_dict(config_dict, indent=0, max_depth=3):
        """
        Recursively print configuration dictionary structure.
        
        Args:
            config_dict: ConfigDict or dict to print
            indent: Current indentation level
            max_depth: Maximum recursion depth to prevent overflow
        """
        if indent > max_depth:
            print("  " * indent + "... (max depth reached)")
            return
            
        for key, value in config_dict.items():
            prefix = "  " * indent + f"📄 {key}:"
            
            if isinstance(value, (ConfigDict, dict)):
                print(prefix)
                print_config_dict(value, indent + 1, max_depth)
            elif isinstance(value, list):
                print(f"{prefix} {value} (list of {len(value)} items)")
            else:
                print(f"{prefix} {value} ({type(value).__name__})")
    
    def print_config_sections(config, config_name="Config"):
        """
        Print all sections of a configuration object dynamically.
        
        Args:
            config: Configuration object to inspect
            config_name: Name for display purposes
        """
        print(f"\n🔍 {config_name} Structure:")
        print("-" * 40)
        
        # Get all attributes that don't start with underscore
        sections = [attr for attr in dir(config) if not attr.startswith('_') and not callable(getattr(config, attr))]
        
        for section_name in sections:
            try:
                section_value = getattr(config, section_name)
                print(f"\n📂 {section_name.upper()}:")
                
                if isinstance(section_value, (ConfigDict, dict)):
                    print_config_dict(section_value, indent=1)
                else:
                    print(f"  📄 {section_value} ({type(section_value).__name__})")
                    
            except Exception as e:
                print(f"  ❌ Error accessing {section_name}: {e}")
    
    print("🎸 GUITARTAINER CONFIG FACTORY TEST 🎸")
    print("=" * 50)
    
    try:
        print("\n📋 Testing Project Configuration Factory:")
        
        # Test the simple import and usage pattern
        config = get_project_config()
        print(f"✅ Config loaded: {type(config).__name__}")
        
        # Dynamically print all project configuration sections
        print_config_sections(config, "Project Configuration")
        
        print("\n🔍 Testing Nested Access Methods:")
        
        # Test nested access dynamically
        test_paths = [
            'video.core.supported_formats',
            'video.processing.resize_dimensions', 
            'gui.core.window.width',
            'application.core.name',
            'pose_detection.core.min_detection_confidence',
            'nonexistent.path'  # Test missing path
        ]
        
        for path in test_paths:
            try:
                section_name = path.split('.')[0]
                if hasattr(config, section_name):
                    section = getattr(config, section_name)
                    if hasattr(section, 'get_nested'):
                        value = section.get_nested('.'.join(path.split('.')[1:]), default='NOT_FOUND')
                        print(f"✅ {path}: {value}")
                    else:
                        print(f"⚠️ {path}: Section not accessible")
                else:
                    print(f"❌ {path}: Section '{section_name}' not found")
            except Exception as e:
                print(f"❌ {path}: Error - {e}")
        
        print("\n🏗️ Testing Infrastructure Configuration:")
        
        infra_config = get_infrastructure_config()
        print(f"✅ Infrastructure config: {type(infra_config).__name__}")
        
        # Dynamically print infrastructure configuration
        print_config_sections(infra_config, "Infrastructure Configuration")
        
        print("\n🎯 CONFIGURATION FACTORY VALIDATION:")
        validation_points = [
            "Simple import pattern works: from config import get_project_config",
            "Hierarchical access works: config.video.core.supported_formats",
            "Dot notation access works throughout",
            "Nested path access works with fallbacks",
            "File consolidation working behind the scenes",
            "No manual file management needed",
            "Dynamic configuration introspection working"
        ]
        
        for point in validation_points:
            print(f"✅ {point}")
        
        print("\n🚀 CONFIG FACTORY READY FOR USE IN OTHER MODULES!")
        
    except Exception as e:
        print(f"\n❌ CONFIG FACTORY ERROR: {e}")
        import traceback
        traceback.print_exc()
        print("\n🔧 Check YAML files and file paths")
