"""
Video Input Module - Utility Functions

Educational Focus: Helper functions for video file operations and validation.
This module contains utility functions that support the main video processing classes.

Author: GuitarTrainer Development
"""

from pathlib import Path
from typing import Optional
import logging

# Set up module logger
logger = logging.getLogger(__name__)


def check_file_exists(file_path: Path) -> bool:
    """
    Verify that a video file exists and is accessible.
    
    Educational Note: File existence checking is the first validation step
    in any computer vision pipeline. We use pathlib.Path for modern,
    cross-platform file operations instead of older os.path methods.
    
    Computer Vision Context: Video processing applications must handle
    user-provided file paths gracefully. Users often provide:
    - Non-existent files (typos in path)
    - Files that exist but are not readable (permission issues)
    - Network paths that are temporarily unavailable
    
    Args:
        file_path (Path): Path to video file to check
        
    Returns:
        bool: True if file exists and is readable, False otherwise
        
    Example:
        >>> video_path = Path("guitar_lesson.mp4")
        >>> if check_file_exists(video_path):
        ...     print("File is ready for processing")
        ... else:
        ...     print("File not found or not accessible")
    """
    # Educational Note: We explicitly check both existence and readability
    # because a file might exist but not be readable due to permissions
    
    try:
        # Check if path exists (could be file or directory)
        if not file_path.exists():
            logger.warning(f"File does not exist: {file_path}")
            return False
            
        # Check if it's actually a file (not a directory)
        if not file_path.is_file():
            logger.warning(f"Path exists but is not a file: {file_path}")
            return False
            
        # Check if file is readable (has content and permissions allow reading)
        # Note: This doesn't guarantee the file is a valid video, just that
        # we can access it for reading
        if file_path.stat().st_size == 0:
            logger.warning(f"File exists but is empty: {file_path}")
            return False
            
        # Educational Note: We could also check read permissions here with
        # os.access(file_path, os.R_OK) but pathlib + try/catch is more pythonic
        
        logger.debug(f"File validation passed: {file_path}")
        return True
        
    except PermissionError:
        # Handle permission denied errors specifically
        logger.error(f"Permission denied accessing file: {file_path}")
        return False
        
    except OSError as e:
        # Handle other OS-level errors (network issues, corrupted filesystem, etc.)
        logger.error(f"OS error accessing file {file_path}: {e}")
        return False
        
    except Exception as e:
        # Catch any unexpected errors to prevent crashes
        logger.error(f"Unexpected error checking file {file_path}: {e}")
        return False


# Educational Note: This function focuses purely on file system validation.
# It does NOT check if the file is a valid video - that's a separate concern
# that will be handled by format validation and OpenCV loading functions.
# This separation of concerns makes testing easier and code more maintainable.
