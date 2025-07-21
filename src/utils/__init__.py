"""
Utilities Package for GuitarTrainer

Provides common utilities used across all components including
centralized logging, configuration management, and helper functions.

Educational Note: Utility packages provide shared functionality to avoid
code duplication and ensure consistent behavior across components.
"""

from .logger_factory import get_component_logger, log_system_info

__all__ = [
    'get_component_logger',
    'log_system_info'
]
