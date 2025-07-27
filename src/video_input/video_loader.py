"""
Video file loading and validation for guitar analysis.

This module demonstrates fundamental video I/O operations using OpenCV,
proper resource management patterns, and error handling for computer vision applications.

Educational Focus:
- OpenCV VideoCapture usage and best practices
- Video property validation for CV analysis suitability
- Resource management (always release video captures)
- Integration with project configuration and logging systems
"""

import cv2
import logging
import sys
from pathlib import Path
from typing import Optional, Dict, Any

# Add project root to Python path for proper imports
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Import project infrastructure
try:
    from config.config_manager import get_project_config
    from src.utils.logger_factory import get_component_logger
    logger = get_component_logger('video_input')
    config = get_project_config()
except ImportError:
    # Graceful fallback for standalone usage
    logger = logging.getLogger(__name__)
    config = None

# Import module utilities (absolute imports)
from src.video_input.video_utils import check_file_exists, validate_video_format


class VideoLoader:
    """
    Handles video file loading and validation for guitar technique analysis.
    
    Educational Note: Video loading for computer vision requires careful validation
    to ensure files are suitable for analysis. This class demonstrates:
    - Proper OpenCV VideoCapture usage
    - Video property validation (fps, frame count, resolution)
    - Resource management patterns (always release captures)
    - Integration with configuration and logging systems
    
    The class is designed to be the first layer in the video processing pipeline,
    providing validated video sources for pose detection and analysis.
    """
    
    def __init__(self):
        """
        Initialize VideoLoader with configuration and logging.
        
        Educational Note: Constructor sets up dependencies but doesn't load any video.
        This separation allows the class to be reused for multiple video files
        without recreating the object.
        """
        self.logger = logger
        self.config = config
        self.current_video: Optional[cv2.VideoCapture] = None
        self.video_info: Dict[str, Any] = {}
        self.current_file_path: Optional[Path] = None
        
        # Log initialization for debugging
        self.logger.debug("VideoLoader initialized")
    
    def load_video(self, file_path: Path) -> bool:
        """
        Load video file and validate it's suitable for analysis.
        
        Educational Note: This method demonstrates the complete video loading workflow:
        1. File system validation (exists, readable, correct format)
        2. OpenCV VideoCapture creation and validation
        3. Video property extraction and validation
        4. Resource cleanup on any failure
        
        The method returns a simple boolean for easy integration with error handling,
        while detailed error information is logged for debugging.
        
        Args:
            file_path: Path to video file to load
            
        Returns:
            bool: True if video loaded successfully and is suitable for analysis
            
        Raises:
            No exceptions raised - all errors handled gracefully with logging
            
        Example:
            >>> loader = VideoLoader()
            >>> success = loader.load_video(Path("guitar_video.mp4"))
            >>> if success:
            ...     print(f"Video loaded: {loader.get_video_info()}")
        """
        # Educational Note: Always start with basic validation before expensive operations
        self.logger.info(f"Attempting to load video: {file_path}")
        
        # Step 1: File system validation using our existing utilities
        if not check_file_exists(file_path):
            self.logger.warning(f"File validation failed: {file_path}")
            return False
            
        if not validate_video_format(file_path):
            self.logger.warning(f"Unsupported video format: {file_path.suffix}")
            return False
        
        # Step 2: Close any existing video before loading new one
        self._close_current_video()
        
        # Step 3: OpenCV VideoCapture creation and validation
        try:
            # Educational Note: Convert Path to string for OpenCV compatibility
            video_cap = cv2.VideoCapture(str(file_path))
            
            # Educational Note: Always check if VideoCapture opened successfully
            # This can fail due to codec issues, corruption, or unsupported formats
            if not video_cap.isOpened():
                self.logger.error(f"OpenCV could not open video file: {file_path}")
                video_cap.release()  # Clean up even failed captures
                return False
            
            # Step 4: Extract and validate video properties
            if not self._validate_video_properties(video_cap, file_path):
                video_cap.release()
                return False
            
            # Step 5: Success - store video capture and file info
            self.current_video = video_cap
            self.current_file_path = file_path
            
            self.logger.info(f"Video loaded successfully: {file_path}")
            self.logger.debug(f"Video properties: {self.video_info}")
            
            return True
            
        except cv2.error as e:
            # Educational Note: OpenCV operations can raise cv2.error exceptions
            self.logger.error(f"OpenCV error loading video {file_path}: {e}")
            return False
            
        except Exception as e:
            # Educational Note: Catch unexpected errors to prevent crashes
            self.logger.error(f"Unexpected error loading video {file_path}: {e}")
            return False
    
    def _validate_video_properties(self, video_cap: cv2.VideoCapture, file_path: Path) -> bool:
        """
        Validate video properties for analysis suitability.
        
        Educational Note: Computer vision applications require videos with:
        - Valid frame rate (fps > 0) for temporal analysis
        - Sufficient frame count (> 0) to have content to analyze
        - Reasonable resolution for pose detection accuracy
        
        This method extracts properties and validates they meet minimum requirements.
        
        Args:
            video_cap: OpenCV VideoCapture object to validate
            file_path: Path to video file (for logging)
            
        Returns:
            bool: True if video properties are suitable for analysis
        """
        try:
            # Educational Note: Extract key video properties using OpenCV constants
            fps = video_cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
            width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            # Calculate duration for user information
            duration = frame_count / fps if fps > 0 else 0
            
            # Store video information for later access
            self.video_info = {
                'file_path': str(file_path),
                'fps': fps,
                'frame_count': frame_count,
                'width': width,
                'height': height,
                'duration_seconds': duration,
                'resolution': f"{width}x{height}"
            }
            
            # Educational Note: Validate critical properties for CV analysis
            if fps <= 0:
                self.logger.error(f"Invalid fps ({fps}) in video: {file_path}")
                return False
                
            if frame_count <= 0:
                self.logger.error(f"Invalid frame count ({frame_count}) in video: {file_path}")
                return False
                
            if width <= 0 or height <= 0:
                self.logger.error(f"Invalid resolution ({width}x{height}) in video: {file_path}")
                return False
            
            # Educational Note: Check against configuration limits if available
            if self.config:
                try:
                    max_width, max_height = self.config.video.core.max_resolution
                    if width > max_width or height > max_height:
                        self.logger.warning(
                            f"Video resolution ({width}x{height}) exceeds maximum "
                            f"({max_width}x{max_height}). May impact performance."
                        )
                        # Note: This is a warning, not a failure - we can still process
                except AttributeError:
                    # Configuration not available or malformed
                    self.logger.debug("No resolution limits configured")
            
            self.logger.debug(f"Video validation passed: {fps:.1f}fps, {frame_count} frames, {width}x{height}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error validating video properties for {file_path}: {e}")
            return False
    
    def _close_current_video(self) -> None:
        """
        Close currently loaded video and clean up resources.
        
        Educational Note: Proper resource management is critical in OpenCV applications.
        VideoCapture objects hold system resources (file handles, memory) that must
        be explicitly released to prevent resource leaks.
        """
        if self.current_video is not None:
            try:
                self.current_video.release()
                self.logger.debug(f"Released video capture for: {self.current_file_path}")
            except Exception as e:
                self.logger.warning(f"Error releasing video capture: {e}")
            finally:
                self.current_video = None
                self.current_file_path = None
                self.video_info = {}
    
    def is_video_loaded(self) -> bool:
        """
        Check if a video is currently loaded and ready for processing.
        
        Returns:
            bool: True if video is loaded and capture is open
        """
        return (self.current_video is not None and 
                self.current_video.isOpened())
    
    def get_video_info(self) -> Dict[str, Any]:
        """
        Get information about the currently loaded video.
        
        Educational Note: This method provides metadata that other components
        can use for processing decisions (frame rate for temporal analysis,
        resolution for pose detection accuracy, etc.)
        
        Returns:
            dict: Video properties including fps, frame count, resolution, duration
                 Empty dict if no video is loaded
        """
        return self.video_info.copy()  # Return copy to prevent external modification
    
    def close_video(self) -> None:
        """
        Close currently loaded video and release resources.
        
        Educational Note: Public method for explicit resource cleanup.
        Should be called when done processing a video to free system resources.
        """
        self._close_current_video()
        self.logger.debug("Video closed by user request")
    
    def __del__(self):
        """
        Destructor to ensure video resources are released.
        
        Educational Note: Python destructor as safety net for resource cleanup.
        While explicit close_video() calls are preferred, this ensures resources
        are released even if the programmer forgets to call cleanup methods.
        """
        self._close_current_video()


if __name__ == "__main__":
    """
    Manual testing and demonstration of VideoLoader functionality.
    
    Educational Note: This section demonstrates proper VideoLoader usage
    and shows how to handle both success and failure cases.
    """
    
    def demonstrate_video_loader():
        """Demonstrate VideoLoader with various scenarios."""
        print("🎯 VIDEOLOADER DEMONSTRATION")
        print("=" * 50)
        
        # Create VideoLoader instance
        loader = VideoLoader()
        print(f"✅ VideoLoader created")
        
        # Test with non-existent file
        print("\n📁 Testing with non-existent file:")
        test_path = Path("nonexistent_video.mp4")
        success = loader.load_video(test_path)
        print(f"   Result: {'✅ Success' if success else '❌ Failed (expected)'}")
        
        # Test with invalid format
        print("\n📁 Testing with invalid format:")
        test_path = Path("test_file.txt")
        # Create a temporary text file for testing
        try:
            test_path.touch()
            success = loader.load_video(test_path)
            print(f"   Result: {'✅ Success' if success else '❌ Failed (expected)'}")
            test_path.unlink()  # Clean up
        except Exception as e:
            print(f"   Setup error: {e}")
        
        # Test with real video file if available
        print("\n🎬 Testing with real test video file:")
        test_video_path = Path(__file__).parent.parent.parent / "tests" / "fixtures" / "test_video.mp4"
        
        if test_video_path.exists():
            print(f"   📹 Found test video: {test_video_path.name}")
            success = loader.load_video(test_video_path)
            
            if success:
                print("   ✅ Real video loaded successfully!")
                
                # Show detailed video information
                info = loader.get_video_info()
                print("\n   📊 Real Video Properties:")
                for key, value in info.items():
                    if key == 'duration_seconds':
                        print(f"      {key}: {value:.2f} seconds")
                    elif isinstance(value, float):
                        print(f"      {key}: {value:.1f}")
                    else:
                        print(f"      {key}: {value}")
                
                print(f"\n   📺 Video loaded status: {loader.is_video_loaded()}")
                
                # Test resource cleanup with real file
                print("   🧹 Testing cleanup with real video...")
                loader.close_video()
                print(f"   📺 Video loaded after cleanup: {loader.is_video_loaded()}")
                
            else:
                print("   ❌ Failed to load real video (check file format/corruption)")
        else:
            print(f"   ⚠️  Test video not found at: {test_video_path}")
            print("   📝 To enable real video testing, place a test video at the above path")
        
        # Final status check
        final_info = loader.get_video_info()
        if final_info:
            print("\n📊 Remaining video information (should be empty):")
            for key, value in final_info.items():
                print(f"   {key}: {value}")
        else:
            print("\n📊 ✅ No video information remaining (cleanup successful)")
    
    
    def show_integration_patterns():
        """Show how VideoLoader integrates with project infrastructure."""
        print("\n🔗 INTEGRATION PATTERNS DEMONSTRATION")
        print("=" * 50)
        
        # Show configuration integration
        loader = VideoLoader()
        if loader.config:
            print("✅ Configuration system integrated")
            try:
                # Dynamically show configuration sections
                config_sections = [attr for attr in dir(loader.config) if not attr.startswith('_')]
                print("📋 Available config sections:")
                for section in config_sections:
                    print(f"   - {section}")
            except Exception as e:
                print(f"   Configuration access error: {e}")
        else:
            print("⚠️  Configuration system not available (fallback mode)")
        
        # Show logging integration
        print(f"\n📝 Logger: {loader.logger.name}")
        print(f"   Logger level: {loader.logger.level}")
        
        # Demonstrate typical workflow
        print(f"\n🔄 Typical workflow:")
        print(f"   1. Create VideoLoader instance")
        print(f"   2. Call load_video() with file path")
        print(f"   3. Check is_video_loaded() for success")
        print(f"   4. Use get_video_info() for metadata")
        print(f"   5. Process video frames (next micro-increment)")
        print(f"   6. Call close_video() when done")
    
    def demonstrate_real_video_workflow():
        """Demonstrate complete workflow with real video file."""
        print("\n🎬 REAL VIDEO WORKFLOW DEMONSTRATION")
        print("=" * 50)
        
        test_video_path = Path(__file__).parent.parent.parent / "tests" / "fixtures" / "test_video.mp4"
        
        if not test_video_path.exists():
            print(f"   ⚠️  Test video not available for workflow demonstration")
            print(f"   📝 Place test_video.mp4 in tests/fixtures/ to see complete workflow")
            return
        
        loader = VideoLoader()
        
        print(f"   📹 Using test video: {test_video_path.name}")
        print(f"   💾 File size: {test_video_path.stat().st_size / 1024:.1f} KB")
        
        # Step-by-step workflow demonstration
        print("\n   🔄 Step-by-step workflow:")
        
        print("   1. 🚀 Initializing VideoLoader...")
        assert not loader.is_video_loaded()
        print("      ✅ Initial state verified (no video loaded)")
        
        print("   2. 📁 Loading video file...")
        success = loader.load_video(test_video_path)
        if success:
            print("      ✅ Video loaded successfully")
        else:
            print("      ❌ Video loading failed")
            return
        
        print("   3. 📊 Extracting video properties...")
        info = loader.get_video_info()
        
        # Display properties in organized way
        print("      📹 Basic Properties:")
        print(f"         Resolution: {info.get('resolution', 'Unknown')}")
        print(f"         Frame Rate: {info.get('fps', 0):.1f} fps")
        print(f"         Duration: {info.get('duration_seconds', 0):.2f} seconds")
        print(f"         Total Frames: {info.get('frame_count', 0)}")
        
        print("      🔍 Analysis Suitability:")
        fps = info.get('fps', 0)
        width = info.get('width', 0)
        height = info.get('height', 0)
        
        if fps >= 24:
            print(f"         ✅ Frame rate ({fps:.1f} fps) suitable for analysis")
        else:
            print(f"         ⚠️  Frame rate ({fps:.1f} fps) may be too low for smooth analysis")
        
        if width >= 640 and height >= 480:
            print(f"         ✅ Resolution ({width}x{height}) suitable for pose detection")
        else:
            print(f"         ⚠️  Resolution ({width}x{height}) may be too low for accurate pose detection")
        
        print("   4. 📋 Verifying video state...")
        assert loader.is_video_loaded()
        assert loader.current_file_path == test_video_path
        print("      ✅ Video state verification passed")
        
        print("   5. 🧹 Cleaning up resources...")
        loader.close_video()
        assert not loader.is_video_loaded()
        assert loader.get_video_info() == {}
        print("      ✅ Resource cleanup completed")
        
        print("\n   🎉 Complete workflow demonstration successful!")
    
    # Run demonstrations
    demonstrate_video_loader() 
    demonstrate_real_video_workflow()
    show_integration_patterns()
    
    print("\n🎉 VideoLoader demonstration completed!")
    print("\n📚 Educational Notes:")
    print("   - Always validate files before OpenCV operations")
    print("   - Check VideoCapture.isOpened() after creation")
    print("   - Validate video properties for CV suitability")
    print("   - Always release VideoCapture resources")
    print("   - Use configuration and logging for production code")
