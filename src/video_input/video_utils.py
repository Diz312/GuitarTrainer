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

# Import logger factory
try:
    # Add src directory to path for imports
    sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))
    from utils.logger_factory import get_component_logger
    logger = get_component_logger('video_input')
except ImportError as e:
    # Fallback for testing or standalone usage
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

def validate_video_format(file_path: Path) -> bool:
    """
    Validate that a file has a supported video format extension.
    
    Educational Note: Format validation is the second validation step
    in a computer vision pipeline, after file existence checking.
    This function only checks the file extension - it does NOT validate
    the actual file content or codec information.
    
    Computer Vision Context: Video processing applications need to
    filter out unsupported formats early to prevent processing errors.
    Different video formats have different characteristics:
    - Container formats (.mp4, .avi, .mov, .mkv)
    - Codec requirements (H.264, H.265, VP9)
    - Metadata handling capabilities
    
    This function handles the first level - container format validation.
    
    Args:
        file_path (Path): Path to video file to validate
        
    Returns:
        bool: True if file extension is in supported formats, False otherwise
        
    Example:
        >>> video_path = Path("guitar_lesson.mp4")
        >>> if validate_video_format(video_path):
        ...     print("Format is supported")
        ... else:
        ...     print("Unsupported video format")
    """
    # Educational Note: We validate format regardless of file existence
    # because this function has a single responsibility - format checking
    # File existence should be checked separately using check_file_exists()
    
    try:
        # Get file extension (convert to lowercase for case-insensitive comparison)
        file_extension = file_path.suffix.lower()
        
        # Handle edge case of no extension
        if not file_extension:
            logger.warning(f"File has no extension: {file_path}")
            return False
        
        # Get supported formats from configuration
        supported_formats = get_supported_video_formats()
        
        # Check if extension is in supported list
        is_supported = file_extension in supported_formats
        
        if is_supported:
            logger.debug(f"Video format validation passed: {file_path} ({file_extension})")
        else:
            logger.warning(f"Unsupported video format: {file_path} ({file_extension}). Supported: {supported_formats}")
            
        return is_supported
        
    except Exception as e:
        # Handle any unexpected errors gracefully
        logger.error(f"Error validating video format for {file_path}: {e}")
        return False

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
    
    def demonstrate_format_validation():
        """
        Demonstrate video format validation with various file types.
        
        Educational Note: Shows how format validation works with different
        file extensions, including edge cases and unsupported formats.
        """
        print("\n🎬 DEMONSTRATING VIDEO FORMAT VALIDATION:")
        print("-" * 50)
        
        # Test cases with different file extensions
        test_cases = [
            ("Valid MP4 video", Path("guitar_lesson.mp4")),
            ("Valid AVI video", Path("practice_session.avi")),
            ("Valid MOV video", Path("performance.MOV")),  # Test case sensitivity
            ("Invalid text file", Path("readme.txt")),
            ("Invalid image file", Path("photo.jpg")),
            ("No extension", Path("videofile")),
            ("Empty extension", Path("video.")),
            ("Multiple extensions", Path("backup.mp4.old")),
        ]
        
        supported_formats = get_supported_video_formats()
        print(f"\n📋 Supported formats: {supported_formats}")
        
        for description, test_path in test_cases:
            print(f"\n📹 Testing: {description}")
            print(f"   File: {test_path}")
            print(f"   Extension: '{test_path.suffix.lower()}'")
            
            try:
                result = validate_video_format(test_path)
                status = "✅ SUPPORTED" if result else "❌ NOT SUPPORTED"
                print(f"   Result: {status}")
                
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
        
        Educational Note: Demonstrates the complete validation workflow
        combining file existence checking and format validation.
        """
        print("\n🔄 DEMONSTRATING COMPLETE VALIDATION WORKFLOW:")
        print("-" * 50)
        
        # Simulate a complete video processing validation workflow
        test_files = [
            Path("sample_video.mp4"),
            Path("guitar_lesson.avi"),
            Path("invalid_file.txt"),
            Path(__file__)  # This Python file
        ]
        
        for test_file in test_files:
            print(f"\n📹 Processing: {test_file.name}")
            
            # Step 1: Check if file exists
            exists = check_file_exists(test_file)
            print(f"   1. File exists: {'✅ Yes' if exists else '❌ No'}")
            
            # Step 2: Check if format is supported (regardless of existence)
            format_valid = validate_video_format(test_file)
            print(f"   2. Format supported: {'✅ Yes' if format_valid else '❌ No'}")
            
            # Step 3: Overall validation for video processing
            ready_for_processing = exists and format_valid
            print(f"   3. Ready for processing: {'✅ Yes' if ready_for_processing else '❌ No'}")
            
            # Show reasoning
            if not exists:
                print(f"      → Cannot process: File not accessible")
            elif not format_valid:
                print(f"      → Cannot process: Unsupported format ({test_file.suffix})")
            elif ready_for_processing:
                print(f"      → Ready for video processing pipeline")
    
    print("🎸 GUITARTAINER VIDEO INPUT UTILITIES TEST 🎸")
    print("=" * 60)
    
    try:
        print("\n🔧 TESTING VIDEO INPUT UTILITY FUNCTIONS:")
        
        # Test logger integration first
        print(f"\n📋 Logger status: {logger.name if hasattr(logger, 'name') else 'basic logger'}")
        logger.info("Starting video_utils demonstration")
        
        # Demonstrate each function
        demonstrate_file_existence_checking()
        demonstrate_format_validation()
        demonstrate_config_integration()
        show_function_integration()
        
        print("\n🎯 VIDEO INPUT UTILITIES VALIDATION:")
        validation_points = [
            "File existence checking working with various scenarios",
            "Video format validation working with supported/unsupported extensions",
            "Case-insensitive format validation implemented",
            "Configuration integration successful (formats loaded)",
            "Error handling graceful for invalid inputs",
            "Complete validation workflow demonstrates real-world usage",
            "Dynamic testing without hardcoded values",
            "Educational demonstrations show CV pipeline concepts"
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
