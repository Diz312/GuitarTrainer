"""
Video Input Module

Handles video file operations for guitar technique analysis.
Provides video loading, validation, and frame extraction capabilities.

Educational Note: This module demonstrates fundamental video I/O operations
using OpenCV and proper error handling patterns for computer vision applications.
"""

# Import functions as they're implemented
from .video_utils import check_file_exists, get_supported_video_formats

__all__ = [
    'check_file_exists',
    'get_supported_video_formats',
]
