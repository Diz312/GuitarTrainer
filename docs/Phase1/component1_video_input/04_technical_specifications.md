# Component 1: Video Input Module - Development Instructions

## 🎯 **COMPONENT OVERVIEW**

**Component:** Video Input Module  
**Location:** `src/video_input/`  
**Phase:** 1 (Foundation)  
**Timeline:** Days 1-2  
**Dependencies:** OpenCV, NumPy, pathlib  

**Purpose:** Handle video file loading, validation, and frame extraction for guitar technique analysis.

---

## COMPONENT SPECIFICATIONS

### **Files to Create:**
```
src/video_input/
├── __init__.py              # Module initialization and exports
├── video_loader.py          # File loading and validation
├── video_processor.py       # Frame extraction and preprocessing  
└── video_utils.py           # Helper functions and utilities
```

### **Core Classes and Functions:**

#### **1. VideoLoader Class** (`video_loader.py`)
```python
class VideoLoader:
    """
    Handles video file loading and validation for guitar analysis.
    
    Educational Focus: Video I/O fundamentals and validation patterns
    """
    
    def __init__(self, config: VideoConfig)
    def load_video(self, file_path: Path) -> bool
    def get_video_info(self) -> Dict[str, Any]
    def is_video_loaded(self) -> bool
    def close_video(self) -> None
    def validate_format(self, file_path: Path) -> bool
```

#### **2. VideoProcessor Class** (`video_processor.py`)
```python
class VideoProcessor:
    """
    Processes loaded videos for pose detection analysis.
    
    Educational Focus: Frame extraction and preprocessing techniques
    """
    
    def __init__(self, video_loader: VideoLoader)
    def extract_frame(self, frame_number: int) -> Optional[np.ndarray]
    def extract_frames_batch(self, start_frame: int, count: int) -> List[np.ndarray]
    def preprocess_frame(self, frame: np.ndarray) -> np.ndarray
    def get_frame_count(self) -> int
    def get_fps(self) -> float
```

#### **3. Utility Functions** (`video_utils.py`) - ✅ **IMPLEMENTED**
```python
# COMPLETED IMPLEMENTATIONS:
def check_file_exists(file_path: Path) -> bool
    """Comprehensive file validation with error handling"""
    # ✅ COMPLETE: File existence, type, size, permissions validation
    # ✅ COMPLETE: Educational comments and CV context
    # ✅ COMPLETE: Robust error handling (PermissionError, OSError, etc.)
    
def get_supported_video_formats() -> List[str]
    """Get supported formats from hierarchical configuration system"""
    # ✅ COMPLETE: Integration with hierarchical config system
    # ✅ COMPLETE: Graceful fallback mechanisms
    # ✅ COMPLETE: Educational comments about config integration

# REMAINING TO IMPLEMENT:
def validate_video_properties(video_cap: cv2.VideoCapture) -> Dict[str, bool]
def format_duration(total_seconds: float) -> str
def resize_frame_if_needed(frame: np.ndarray, max_size: Tuple[int, int]) -> np.ndarray
def convert_frame_bgr_to_rgb(frame: np.ndarray) -> np.ndarray
```

---

## DETAILED IMPLEMENTATION REQUIREMENTS

### **1. Module Initialization** (`__init__.py`) - ✅ **IMPLEMENTED**
```python
"""
Video Input Module

Handles video file operations for guitar technique analysis.
Provides video loading, validation, and frame extraction capabilities.

Educational Note: This module demonstrates fundamental video I/O operations
using OpenCV and proper error handling patterns for computer vision applications.
"""

# ✅ COMPLETED IMPLEMENTATION:
from .video_utils import check_file_exists, get_supported_video_formats

__all__ = [
    'check_file_exists',
    'get_supported_video_formats',
]

# REMAINING TO ADD:
# from .video_loader import VideoLoader
# from .video_processor import VideoProcessor
# from .video_utils import validate_video_properties
```

### **2. VideoLoader Implementation** (`video_loader.py`)

#### **Class Structure:**
```python
"""
Video file loading and validation for guitar analysis.

Educational Focus: 
- Video I/O fundamentals with OpenCV
- Proper resource management (always release video captures)
- Error handling patterns for file operations
- Video property validation for analysis suitability
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Optional, Dict, Any, List
import logging

from ..config.settings import VideoConfig
from .video_utils import validate_video_properties

class VideoLoader:
    """
    Handles video file loading and validation.
    
    Educational Note: Video loading requires careful validation of file properties
    to ensure they're suitable for computer vision analysis. Always check:
    - File exists and is readable
    - Video codec is supported 
    - Video has valid fps and frame count
    - Resolution is within acceptable range
    """
```

#### **Key Methods Implementation Requirements:**

**`load_video(self, file_path: Path) -> bool`**
- Validate file exists and has supported extension
- Use OpenCV VideoCapture to load video
- Check video properties (fps > 0, frame count > 0)
- Store video capture object for frame extraction
- Handle errors gracefully with logging
- Return True/False for success/failure

**`get_video_info(self) -> Dict[str, Any]`**
- Return dictionary with video metadata:
  - fps, frame_count, duration, resolution
  - file_size, format, codec information
- Handle case where no video is loaded
- Format duration as human-readable string

**`validate_format(self, file_path: Path) -> bool`**
- Check file extension against supported formats
- Validate file is not empty
- Return clear boolean result

### **3. VideoProcessor Implementation** (`video_processor.py`)

#### **Educational Focus:**
```python
"""
Video frame processing for pose detection analysis.

Educational Focus:
- Frame extraction techniques and memory management
- Video preprocessing for computer vision (resize, color space)
- Batch processing vs single frame processing trade-offs
- Error handling for corrupted or invalid frames
"""
```

#### **Key Methods Implementation Requirements:**

**`extract_frame(self, frame_number: int) -> Optional[np.ndarray]`**
- Set video position to specific frame
- Read frame using VideoCapture.read()
- Validate frame was read successfully
- Return numpy array in BGR format (OpenCV default)
- Handle edge cases (frame beyond video end)

**`extract_frames_batch(self, start_frame: int, count: int) -> List[np.ndarray]`**
- Extract multiple consecutive frames efficiently
- Implement memory management (don't hold all frames in memory)
- Skip corrupted frames but log warnings
- Return list of valid frames only

**`preprocess_frame(self, frame: np.ndarray) -> np.ndarray`**
- Resize frame if larger than max resolution (maintain aspect ratio)
- Ensure frame is in correct color space for pose detection
- Handle invalid input frames gracefully
- Add educational comments about preprocessing importance

### **4. Utility Functions** (`video_utils.py`)

#### **Implementation Requirements:**

**`get_supported_formats() -> List[str]`**
```python
def get_supported_formats() -> List[str]:
    """
    Return list of video formats supported by the application.
    
    Educational Note: We limit to commonly supported formats that work
    well with OpenCV and are typical for user-generated content.
    """
    return ['.mp4', '.avi', '.mov', '.mkv']
```

**`validate_video_properties(video_cap: cv2.VideoCapture) -> Dict[str, bool]`**
```python
def validate_video_properties(video_cap: cv2.VideoCapture) -> Dict[str, bool]:
    """
    Validate video properties for analysis suitability.
    
    Educational Note: Computer vision applications require videos with:
    - Valid frame rate (fps > 0)
    - Sufficient frame count for analysis
    - Reasonable resolution (not too small/large)
    """
    # Check fps, frame count, resolution
    # Return dict with validation results
    # Include detailed reasoning for failures
```

**`resize_frame_if_needed(frame: np.ndarray, max_size: Tuple[int, int]) -> np.ndarray`**
- Maintain aspect ratio during resize
- Only resize if frame exceeds maximum dimensions
- Use appropriate interpolation (cv2.INTER_AREA for downscaling)
- Add educational comments about interpolation choices

---

## ERROR HANDLING REQUIREMENTS

### **Exception Handling Pattern:**
```python
try:
    video_cap = cv2.VideoCapture(str(file_path))
    if not video_cap.isOpened():
        raise ValueError(f"Could not open video: {file_path}")
        
    # Always validate video properties
    fps = video_cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        raise ValueError("Invalid video: fps <= 0")
        
except cv2.error as e:
    self.logger.error(f"OpenCV error: {e}")
    return False
except ValueError as e:
    self.logger.warning(f"Validation error: {e}")
    return False
except Exception as e:
    self.logger.error(f"Unexpected error: {e}")
    return False
finally:
    # Always clean up resources
    if 'video_cap' in locals() and video_cap.isOpened():
        video_cap.release()
```

### **Logging Requirements:**
- Use module-level logger: `logging.getLogger(__name__)`
- Log validation failures as warnings (user input issues)
- Log technical errors as errors (file corruption, codec issues)
- Log successful operations as debug level
- Include relevant context (file path, error details)

---

## TESTING REQUIREMENTS - ✅ **ENHANCED IMPLEMENTATION**

### **Testing Methodology:** - ✅ **DUAL APPROACH IMPLEMENTED**

#### **1. Automated Testing (pytest):**
```python
# ✅ COMPLETED: tests/10_project_components/test_video_utils.py
class TestVideoUtils:
    def test_check_file_exists_valid_file(test_files):
        """Test file existence checking with valid files"""
        
    def test_check_file_exists_nonexistent_file(test_files):
        """Test handling of non-existent files"""
        
    @pytest.mark.parametrize("invalid_path", [...])
    def test_edge_cases(invalid_path):
        """Parametrized testing of edge cases"""
        
    # ✅ COMPLETE: pytest fixtures with tmp_path
    # ✅ COMPLETE: Comprehensive edge case testing
    # ✅ COMPLETE: Educational comments explaining test patterns
```

#### **2. Manual Demonstration (`__main__` sections):**
```python
# ✅ COMPLETED: Dynamic demonstration in video_utils.py
if __name__ == "__main__":
    def demonstrate_file_existence_checking():
        """Dynamic testing without hardcoded values"""
        
    def demonstrate_config_integration():
        """Show hierarchical config system usage"""
        
    def show_function_integration():
        """Demonstrate typical video processing workflow"""
        
    # ✅ COMPLETE: No hardcoded values, dynamic test cases
    # ✅ COMPLETE: Educational demonstrations
    # ✅ COMPLETE: Real-world workflow examples
```

### **Test Organization:** - ✅ **IMPLEMENTED**
```
tests/
├── 10_project_components/
│   └── test_video_utils.py     # ✅ COMPLETE
├── 20_infrastructure/
│   └── test_logger_factory.py  # ✅ COMPLETE
└── 30_integration/              # Ready for integration tests
```

---

## PERFORMANCE REQUIREMENTS

### **Memory Management:**
- Release OpenCV VideoCapture objects in `finally` blocks
- Don't hold large frame arrays longer than necessary
- Implement frame batching to limit memory usage
- Clear processed frames from memory promptly

### **Processing Efficiency:**
- Cache video properties after first read
- Minimize video seeking operations
- Use efficient frame preprocessing (only resize when needed)
- Target: Process 30-second video in <10 seconds on typical hardware

---

## EDUCATIONAL DOCUMENTATION REQUIREMENTS

### **Inline Comments:**
- Explain OpenCV concepts (VideoCapture, frame formats)
- Describe video property validation importance
- Comment on memory management patterns
- Explain error handling strategies

### **Module README:**
Create `src/video_input/README.md`:
```markdown
# Video Input Module

Handles video file operations for guitar technique analysis.

## Key Concepts Demonstrated
- Video I/O with OpenCV
- Resource management patterns
- Error handling for file operations
- Frame preprocessing for computer vision

## Usage Examples
[Include practical examples]

## Common Issues
[Document typical problems and solutions]
```

---

## INTEGRATION POINTS

### **With Pose Detection Module:**
```python
# VideoProcessor provides frames to pose detection
processor = VideoProcessor(video_loader)
frame = processor.extract_frame(frame_number)

# Frame format: numpy.ndarray, BGR color space, uint8 dtype
# Expected by MediaPipe pose detection
pose_results = pose_detector.detect_pose(frame)
```

### **With GUI Module:**
```python
# GUI uses VideoLoader for file operations
video_loader = VideoLoader(config)
success = video_loader.load_video(selected_file_path)

# GUI displays video info from VideoLoader
video_info = video_loader.get_video_info()
gui.update_video_info_display(video_info)

# GUI requests specific frames for display
frame = video_processor.extract_frame(current_frame_number)
gui.display_frame(frame)
```

### **Configuration Integration:** - ✅ **ENHANCED IMPLEMENTATION**
```python
# ✅ COMPLETED: Hierarchical Configuration Integration
from config import get_project_config

# Video module now uses hierarchical config system:
config = get_project_config()
supported_formats = config.video.core.supported_formats
max_resolution = config.video.core.max_resolution
resize_dimensions = config.video.processing.resize_dimensions

# Enhanced fallback mechanisms:
# - Graceful handling when config system unavailable
# - Robust error handling with detailed logging
# - Educational comments explaining integration patterns
```

### **Logging Integration:** - ✅ **IMPLEMENTED**
```python
# ✅ COMPLETED: Component-specific logging
from utils.logger_factory import get_component_logger

logger = get_component_logger('video_input')
# Automatic log file creation: logs/video_input.log
# Integrated with hierarchical infrastructure configuration
```

---

## SUCCESS CRITERIA

### **Functional Requirements:**
- [✅] File existence validation with comprehensive error handling
- [✅] Configuration-driven supported format management
- [✅] Integration with hierarchical configuration system
- [✅] Component-specific logging with automatic file creation
- [ ] Successfully load MP4, AVI, MOV video files (VideoLoader)
- [ ] Extract individual frames as numpy arrays (VideoProcessor)
- [ ] Validate video properties (fps, resolution, duration)
- [ ] Handle file errors gracefully without crashing
- [ ] Provide accurate video metadata

### **Code Quality Requirements:**
- [✅] Extensive educational comments explaining CV concepts
- [✅] Proper error handling with meaningful messages
- [✅] Resource cleanup patterns (pathlib.Path usage)
- [✅] Clear function documentation with examples
- [✅] Comprehensive testing (pytest + `__main__` demonstrations)
- [ ] Resource cleanup (always release video captures) - for VideoLoader
- [ ] Clear class documentation - for VideoLoader/VideoProcessor
- [ ] Unit tests with >90% coverage - for complete module

### **Integration Requirements:**
- [✅] Integration with hierarchical configuration system
- [✅] Component-specific logging integration
- [✅] Graceful fallback mechanisms for missing config
- [✅] Educational integration patterns demonstrated
- [ ] Provides frames in format expected by pose detection
- [ ] Integrates with GUI file selection dialogs
- [ ] Uses project configuration system (VideoLoader/VideoProcessor)
- [ ] Follows project logging standards (VideoLoader/VideoProcessor)

---

## COMPLETION CHECKLIST

### **Implementation Phase:**
- [✅] Create module structure with all required files
- [✅] Implement video_utils.py with file validation functions
- [✅] Integrate with hierarchical configuration system
- [✅] Add comprehensive error handling and logging
- [✅] Write extensive educational comments and documentation
- [ ] Implement VideoLoader class with all methods
- [ ] Implement VideoProcessor class with all methods
- [ ] Complete remaining utility functions

### **Testing Phase:**
- [✅] Write and run pytest tests for video_utils functions
- [✅] Create comprehensive `__main__` demonstration sections
- [✅] Test error scenarios and edge cases
- [✅] Implement dual testing methodology (pytest + manual demos)
- [✅] Organize tests in numbered directory structure
- [ ] Test with various video formats and sizes (VideoLoader/VideoProcessor)
- [ ] Validate memory usage and performance (VideoLoader/VideoProcessor)
- [ ] Test integration points with other modules

### **Documentation Phase:**
- [✅] Add inline code comments explaining CV concepts
- [✅] Document configuration integration patterns
- [✅] Create educational demonstration workflows
- [✅] Update technical specifications with progress
- [ ] Create module README with usage examples
- [ ] Document common issues and solutions
- [ ] Update project documentation

### **Current Status:** 🚀 **Micro-Increment 1 COMPLETE - Foundation Established**
- ✅ **Video utilities foundation** with file validation and config integration
- ✅ **Infrastructure integration** with hierarchical config and logging systems
- ✅ **Testing methodology** established with pytest + `__main__` dual approach
- ✅ **Educational patterns** implemented throughout codebase

### **Next Steps (Micro-Increment 2):**
- **Format validation function** - Validate file extensions against supported formats
- **Enhanced file validation** - MIME type checking and basic file structure validation
- **Error handling expansion** - More detailed error reporting and recovery

**This component serves as the foundation for all video processing in the GuitarTrainer application and must be robust, educational, and well-integrated.**
