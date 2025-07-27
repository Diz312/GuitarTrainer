"""
Video Input Module

Handles video file operations for guitar technique analysis.
Provides video loading, validation, and frame extraction capabilities.

Educational Note: This module demonstrates fundamental video I/O operations
using OpenCV and proper error handling patterns for computer vision applications.
"""

# Import utility functions
from .video_utils import (
    check_file_exists, 
    validate_video_format, 
    get_supported_video_formats
)

# Import main classes
from .video_loader import VideoLoader

__all__ = [
    # Utility functions
    'check_file_exists',
    'validate_video_format', 
    'get_supported_video_formats',
    # Main classes
    'VideoLoader',
]
