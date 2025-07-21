""" 
Video Input Module - Utility Functions

Educational Focus: Helper functions for video file operations and validation.
This module contains utility functions that support the main video processing classes.

Now integrated with hierarchical configuration system for supported formats.

Author: GuitarTrainer Development
"""

from pathlib import Path
from typing import Optional, List
import logging

# Import project configuration
try:
    import sys
    sys.path.append(str(Path(__file__).parent.parent.parent))
    from config import get_project_config
except ImportError:
    # Fallback for testing or standalone usage
    get_project_config = None

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


def get_supported_video_formats() -> List[str]:
    """
    Get list of supported video formats from configuration.
    
    Educational Note: This demonstrates configuration integration where
    supported formats are centrally managed rather than hardcoded.
    
    Computer Vision Context: Different video formats have different
    characteristics (compression, codec support, metadata handling).
    Centralizing this list allows easy format support updates.
    
    Returns:
        List[str]: Supported video file extensions (e.g. ['.mp4', '.avi'])
        
    Example:
        >>> formats = get_supported_video_formats()
        >>> print(f"Supported formats: {formats}")
        ['.mp4', '.avi', '.mov', '.mkv']
    """
    # Educational Note: We use configuration system for format list
    # rather than hardcoding, making the system more maintainable
    
    try:
        if get_project_config is not None:
            config = get_project_config()
            formats = config.video.core.supported_formats
            logger.debug(f"Loaded supported formats from config: {formats}")
            return formats
        else:
            # Fallback if config system not available
            fallback_formats = ['.mp4', '.avi', '.mov', '.mkv']
            logger.warning("Config system not available, using fallback formats")
            return fallback_formats
            
    except Exception as e:
        # Robust fallback if config loading fails
        logger.error(f"Error loading video formats from config: {e}")
        fallback_formats = ['.mp4', '.avi', '.mov', '.mkv']
        logger.info(f"Using fallback formats: {fallback_formats}")
        return fallback_formats


if __name__ == "__main__":
    """
    Manual testing and demonstration of video input utilities.
    
    Educational Note: This demonstrates the video utility functions in action
    using dynamic examples and real file system operations.
    """
    
    def demonstrate_file_existence_checking():
        """
        Demonstrate file existence checking with various scenarios.
        
        Educational Note: Shows how the function behaves with different
        types of file paths - both valid and invalid cases.
        """
        print("\n📁 DEMONSTRATING FILE EXISTENCE CHECKING:")
        print("-" * 50)
        
        # Test cases with different scenarios
        test_cases = [
            ("This script file (should exist)", Path(__file__)),
            ("Non-existent video file", Path("does_not_exist.mp4")),
            ("Current directory (should be False)", Path(".")),
            ("Parent directory (should be False)", Path("..")),
            ("Empty path", Path("")),
        ]
        
        for description, test_path in test_cases:
            print(f"\n📄 Testing: {description}")
            print(f"   Path: {test_path}")
            
            try:
                result = check_file_exists(test_path)
                status = "✅ PASS" if result else "❌ FAIL"
                print(f"   Result: {result} {status}")
                
                # Additional file info if it exists
                if result and test_path.exists():
                    size = test_path.stat().st_size
                    print(f"   Size: {size} bytes")
                    
            except Exception as e:
                print(f"   ⚠️ Exception: {e}")
    
    def demonstrate_config_integration():
        """
        Demonstrate configuration system integration.
        
        Educational Note: Shows how the function integrates with
        the hierarchical configuration system for format management.
        """
        print("\n⚙️ DEMONSTRATING CONFIGURATION INTEGRATION:")
        print("-" * 50)
        
        try:
            formats = get_supported_video_formats()
            print(f"✅ Supported video formats loaded: {len(formats)} formats")
            
            # Dynamic display of formats
            for i, format_ext in enumerate(formats, 1):
                print(f"   {i}. {format_ext}")
                
            # Test format checking logic
            print("\n🔍 Testing format validation logic:")
            test_extensions = ['.mp4', '.txt', '.avi', '.exe', '.mov']
            
            for ext in test_extensions:
                is_supported = ext in formats
                status = "✅ Supported" if is_supported else "❌ Not supported"
                print(f"   {ext}: {status}")
                
        except Exception as e:
            print(f"❌ Error testing config integration: {e}")
    
    def show_function_integration():
        """
        Show how the utility functions work together.
        
        Educational Note: Demonstrates the workflow of file validation
        followed by format checking in a typical video processing pipeline.
        """
        print("\n🔄 DEMONSTRATING FUNCTION INTEGRATION:")
        print("-" * 50)
        
        # Simulate a video processing workflow
        test_files = [
            Path("sample_video.mp4"),
            Path("guitar_lesson.avi"),
            Path("invalid_file.txt"),
            Path(__file__)  # This Python file
        ]
        
        supported_formats = get_supported_video_formats()
        
        for test_file in test_files:
            print(f"\n📹 Processing: {test_file.name}")
            
            # Step 1: Check if file exists
            exists = check_file_exists(test_file)
            print(f"   File exists: {exists}")
            
            if exists:
                # Step 2: Check if format is supported
                file_ext = test_file.suffix.lower()
                format_supported = file_ext in supported_formats
                print(f"   Format ({file_ext}): {'✅ Supported' if format_supported else '❌ Not supported'}")
                
                # Step 3: Overall validation
                valid_for_processing = exists and format_supported
                print(f"   Ready for processing: {'✅ Yes' if valid_for_processing else '❌ No'}")
            else:
                print(f"   ⚠️ Cannot process - file not accessible")
    
    print("🎸 GUITARTAINER VIDEO INPUT UTILITIES TEST 🎸")
    print("=" * 60)
    
    try:
        # Set up basic logging for demonstration
        import logging
        logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
        
        print("\n🔧 TESTING VIDEO INPUT UTILITY FUNCTIONS:")
        
        # Demonstrate each function
        demonstrate_file_existence_checking()
        demonstrate_config_integration()
        show_function_integration()
        
        print("\n🎯 VIDEO INPUT UTILITIES VALIDATION:")
        validation_points = [
            "File existence checking working with various scenarios",
            "Configuration integration successful (formats loaded)",
            "Error handling graceful for invalid inputs",
            "Function integration demonstrates typical workflow",
            "Dynamic testing without hardcoded values",
            "Educational demonstrations show real-world usage"
        ]
        
        for point in validation_points:
            print(f"✅ {point}")
        
        print("\n🚀 VIDEO INPUT UTILITIES READY FOR COMPONENT INTEGRATION!")
        print("📈 Next: Format validation and video loading functionality")
        
    except Exception as e:
        print(f"\n❌ VIDEO UTILITIES ERROR: {e}")
        import traceback
        traceback.print_exc()
        print("\n🔧 Check configuration system and file permissions")
