# GuitarTrainer Developer Agent Bootstrap - Complete Foundation

## 🎯 **DEVELOPER AGENT CONTEXT INITIALIZATION**

**Project:** GuitarTrainer - Computer Vision Guitar Technique Analysis  
**Role:** Primary Development Agent  
**Approach:** Educational code with professional architecture  
**Development Method:** Component-by-component with validation  

---

## PROJECT ARCHITECTURE OVERVIEW

### **Core Mission**
Build a desktop application that analyzes guitar playing technique using computer vision, providing biomechanical feedback for improvement, with continuous learning capabilities.

### **System Architecture**
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Video Input   │───▶│  Pose Detection  │───▶│ Feature Extract │
│    Module       │    │     Engine       │    │     Module      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  GUI Interface  │◄───│ Feedback Engine  │◄───│ Analysis Engine │
└─────────────────┘    └──────────────────┘    └─────────────────┘
        │                                               │
        ▼                                               ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│Upload & Label   │───▶│Continuous Learn  │◄───│ Data Management │
│   Interface     │    │    Pipeline      │    │     Module      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### **Technology Stack**
- **Core Language:** Python 3.9+
- **Computer Vision:** OpenCV 4.8+, MediaPipe 0.10+
- **Machine Learning:** scikit-learn 1.3+
- **GUI Framework:** PyQt6 6.5+
- **Data Processing:** NumPy 1.24+, pandas 2.0+
- **Database:** SQLite with SQLAlchemy 2.0+
- **Configuration:** python-dotenv, PyYAML

---

## DEVELOPMENT STANDARDS & PATTERNS

### **Educational Code Philosophy**
- **Readability over optimization** - Code should teach computer vision concepts
- **Extensive comments** - Explain CV algorithms and design decisions
- **Clear naming** - Variables and functions that explain their purpose
- **Modular design** - Easy to understand and extend individual components
- **Professional patterns** - Industry-standard architecture with educational clarity

### **Code Quality Standards**

#### **File Organization Pattern**
```python
"""
Module: video_input/video_loader.py
Purpose: Handle video file loading and validation for guitar analysis
Author: GuitarTrainer Development
Educational Focus: Video processing fundamentals
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Optional, Tuple, List
import logging

# Import project-specific modules
from ..config.settings import VideoConfig
from .video_utils import validate_video_format
```

#### **Class Structure Pattern**
```python
class VideoLoader:
    """
    Handles video file loading and basic validation.
    
    Educational Note: This class demonstrates video I/O fundamentals
    and proper error handling for computer vision applications.
    
    Attributes:
        supported_formats (List[str]): Video formats we can process
        current_video (Optional[cv2.VideoCapture]): Currently loaded video
    """
    
    def __init__(self, config: VideoConfig):
        """Initialize video loader with configuration."""
        self.config = config
        self.supported_formats = ['.mp4', '.avi', '.mov']
        self.current_video: Optional[cv2.VideoCapture] = None
        self.logger = logging.getLogger(__name__)
    
    def load_video(self, file_path: Path) -> bool:
        """
        Load video file and validate it's suitable for analysis.
        
        Educational Note: Always validate video properties before processing
        to avoid crashes and provide meaningful user feedback.
        
        Args:
            file_path: Path to video file
            
        Returns:
            bool: True if video loaded successfully
            
        Raises:
            ValueError: If video format not supported
            FileNotFoundError: If video file doesn't exist
        """
        # Implementation with extensive educational comments
        pass
```

#### **Function Documentation Pattern**
```python
def extract_pose_landmarks(frame: np.ndarray, 
                         confidence_threshold: float = 0.7) -> Optional[dict]:
    """
    Extract human pose landmarks from a single video frame.
    
    Educational Note: This function demonstrates MediaPipe pose detection
    and shows how confidence thresholds filter unreliable detections.
    
    Computer Vision Concept: Pose estimation uses deep learning models
    trained on large datasets to predict body joint locations in 2D space.
    
    Args:
        frame: Single video frame as numpy array (BGR format)
        confidence_threshold: Minimum confidence for reliable detection (0.0-1.0)
        
    Returns:
        Dictionary containing landmark coordinates and confidence scores,
        or None if no reliable pose detected
        
    Example:
        >>> frame = cv2.imread('guitar_player.jpg')
        >>> landmarks = extract_pose_landmarks(frame, confidence_threshold=0.8)
        >>> if landmarks:
        ...     shoulder_left = landmarks['pose']['left_shoulder']
        ...     print(f"Left shoulder at: {shoulder_left['x']}, {shoulder_left['y']}")
    """
    # Implementation with CV educational explanations
    pass
```

#### **Error Handling Pattern**
```python
try:
    video_cap = cv2.VideoCapture(str(file_path))
    if not video_cap.isOpened():
        raise ValueError(f"Could not open video file: {file_path}")
        
    # Educational note: Always check video properties
    fps = video_cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if fps <= 0 or frame_count <= 0:
        raise ValueError("Invalid video properties detected")
        
except cv2.error as e:
    self.logger.error(f"OpenCV error loading video: {e}")
    return False
except Exception as e:
    self.logger.error(f"Unexpected error loading video: {e}")
    return False
finally:
    if 'video_cap' in locals():
        video_cap.release()
```

---

## PROJECT FILE STRUCTURE

### **Complete Directory Organization**
```
E:\Python\GitHub\GuitarTrainer\
├── src/
│   ├── main.py                     # Application entry point
│   ├── video_input/                # Phase 1 Component
│   │   ├── __init__.py
│   │   ├── video_loader.py        # File loading and validation
│   │   ├── video_processor.py     # Frame extraction and preprocessing
│   │   └── video_utils.py         # Helper functions
│   ├── pose_detection/             # Phase 1 Component
│   │   ├── __init__.py
│   │   ├── mediapipe_detector.py  # MediaPipe pose detection
│   │   ├── landmark_extractor.py  # Process pose landmarks
│   │   └── detection_utils.py     # Utility functions
│   ├── gui/                        # Phase 1 Component
│   │   ├── __init__.py
│   │   ├── main_window.py         # Primary application window
│   │   ├── video_player.py        # Video display widget
│   │   ├── controls.py            # UI controls and dialogs
│   │   └── gui_utils.py           # UI helper functions
│   ├── analysis/                   # Phase 2 Components
│   ├── training/                   # Phase 3 Components
│   ├── feedback/                   # Phase 2 Components
│   ├── continuous_learning/        # Phase 4 Components
│   └── config/
│       ├── __init__.py
│       └── settings.py            # Configuration management
├── data/
│   ├── models/                     # Trained models and versions
│   ├── training_videos/            # Labeled training examples
│   └── configs/                    # Configuration files
├── tests/
├── docs/
├── logs/
├── temp/                           # Video processing temporary files
├── cache/                          # Performance cache
├── requirements.txt
├── .env
└── README.md
```

### **Import Strategy**
```python
# Standard library imports first
import os
import sys
from pathlib import Path
from typing import Optional, Dict, List, Tuple
import logging

# Third-party imports
import cv2
import numpy as np
import mediapipe as mp
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QThread, pyqtSignal

# Project imports (relative)
from .config.settings import load_settings
from .video_input.video_loader import VideoLoader
from .pose_detection.mediapipe_detector import MediaPipeDetector
```

---

## PHASE 1 TECHNICAL SPECIFICATIONS

### **Component Responsibilities**

#### **1. Video Input Module**
**Purpose:** Handle video file operations and preprocessing
**Files:** `src/video_input/`
**Key Classes:**
- `VideoLoader` - File loading and validation
- `VideoProcessor` - Frame extraction and preprocessing  
- `VideoUtils` - Helper functions and format utilities

**Core Functionality:**
- Load MP4, AVI, MOV video files
- Validate video properties (fps, resolution, duration)
- Extract frames for processing
- Handle video format conversions if needed
- Provide video metadata (duration, frame count, fps)

#### **2. Pose Detection Engine**
**Purpose:** Extract human pose landmarks from video frames
**Files:** `src/pose_detection/`
**Key Classes:**
- `MediaPipeDetector` - Main pose detection interface
- `LandmarkExtractor` - Process and filter pose landmarks
- `DetectionUtils` - Coordinate transformations and utilities

**Core Functionality:**
- Initialize MediaPipe pose detection models
- Process single frames to extract pose landmarks
- Filter landmarks by confidence threshold (>0.7)
- Extract specific guitar-relevant body parts:
  - Shoulders (landmarks 11, 12)
  - Right wrist (landmark 16) 
  - Right hand landmarks (21 points)
  - Left hand landmarks (21 points)
- Handle detection failures gracefully

#### **3. GUI Framework**
**Purpose:** Desktop interface for video loading and visualization
**Files:** `src/gui/`
**Key Classes:**
- `MainWindow` - Primary application window
- `VideoPlayer` - Video display and playback controls
- `Controls` - UI controls and file dialogs

**Core Functionality:**
- Main application window with menu bar
- Video player widget with play/pause/seek
- File browser for video selection
- Pose landmark visualization overlay
- Status bar for processing feedback
- Basic settings dialog

### **Integration Points**
```python
# Data flow between components
video_file → VideoLoader → VideoProcessor → frames
frames → MediaPipeDetector → pose_landmarks 
pose_landmarks → GUI → visual_overlay
```

### **Configuration Management**
```python
# settings.py structure
@dataclass
class VideoConfig:
    supported_formats: List[str] = field(default_factory=lambda: ['.mp4', '.avi', '.mov'])
    max_resolution: Tuple[int, int] = (1920, 1080)
    target_fps: int = 30
    
@dataclass 
class PoseConfig:
    model_complexity: int = 1
    min_detection_confidence: float = 0.7
    min_tracking_confidence: float = 0.5
    
@dataclass
class GUIConfig:
    window_width: int = 1200
    window_height: int = 800
    theme: str = "dark"
```

---

## TESTING REQUIREMENTS

### **Unit Testing Standards**
```python
# tests/test_video_input.py example
import unittest
from pathlib import Path
import cv2

from src.video_input.video_loader import VideoLoader
from src.config.settings import VideoConfig

class TestVideoLoader(unittest.TestCase):
    def setUp(self):
        self.config = VideoConfig()
        self.loader = VideoLoader(self.config)
        
    def test_load_valid_video(self):
        """Test loading a valid MP4 file."""
        # Implementation with educational comments
        pass
        
    def test_invalid_format_handling(self):
        """Test proper error handling for unsupported formats."""
        # Implementation 
        pass
```

### **Integration Testing**
- Test video → pose detection pipeline
- Test GUI component integration  
- Test error handling across modules

### **Manual Testing Checklist**
- [ ] Load various video formats
- [ ] Test pose detection on guitar playing videos
- [ ] Verify GUI responsiveness
- [ ] Test error scenarios (corrupt files, etc.)

## CURRENT DEVELOPMENT STATUS - ✅ **FOUNDATION COMPLETE**

### **Micro-Increment 1 Completed Successfully**
**Date**: 2025-07-20 15:45:00  
**Achievement**: Comprehensive project infrastructure established with video utility foundations

### **🏗️ Infrastructure Successfully Implemented**

#### **Configuration System** ✅
- **Hierarchical YAML Architecture**: File-type consolidation (10-19 project, 20-29 infrastructure)
- **Dot Notation Access**: `config.video.core.supported_formats` pattern
- **Deep Merging**: Multiple config files with conflict resolution
- **Dynamic Introspection**: Recursive data structure traversal
- **Graceful Fallbacks**: Handles missing config gracefully

#### **Logging Infrastructure** ✅  
- **Component-Aware Factory**: `get_component_logger('component_name')`
- **Automatic File Creation**: `logs/video_input.log`, `logs/pose_detection.log`
- **Hierarchical Config Integration**: Logging setup from `config/20_logging.yaml`
- **Professional Patterns**: File rotation, console output, structured logging

#### **Testing Framework** ✅
- **Dual Methodology**: Separate pytest files + `__main__` demonstrations
- **Organized Structure**: Numbered test directories (10_, 20_, 30_)
- **Coverage Configuration**: Portable `.coveragerc` excluding demonstration code
- **Complete Workflow**: Quick check → coverage analysis → deep investigation
- **Documentation**: `PYTEST_COMMANDS.md` with copy-paste commands

### **💻 Video Input Module Progress**

#### **Completed Components** ✅
```python
# src/video_input/video_utils.py - COMPLETE
def check_file_exists(file_path: Path) -> bool:
    """Comprehensive file validation with CV context"""
    # ✅ File existence, type, size, permissions validation
    # ✅ Educational comments explaining CV applications
    # ✅ Robust error handling (PermissionError, OSError)
    # ✅ pathlib.Path for cross-platform compatibility
    
def validate_video_format(file_path: Path) -> bool:
    """Case-insensitive video format validation"""
    # ✅ Extension validation against supported formats
    # ✅ Config integration with fallback mechanisms
    # ✅ Single responsibility (extension only, not content)
    # ✅ Educational notes about container vs codec
    
def get_supported_video_formats() -> List[str]:
    """Hierarchical config integration pattern"""
    # ✅ Dynamic format retrieval from config system
    # ✅ Graceful fallback to default formats
    # ✅ Educational config integration demonstration
```

#### **Module Integration** ✅
```python
# src/video_input/__init__.py - COMPLETE
from .video_utils import (
    check_file_exists, 
    validate_video_format, 
    get_supported_video_formats
)
# All utilities exported and ready for VideoLoader integration
```

### **🧪 Quality Gates Achieved**
- ✅ **Educational Value**: Extensive CV concept explanations
- ✅ **Error Handling**: All edge cases covered (permissions, OS errors, etc.)
- ✅ **Professional Standards**: Modern Python patterns, industry practices
- ✅ **Testing Coverage**: Comprehensive pytest + manual demonstrations
- ✅ **Infrastructure Integration**: Config/logging patterns established
- ✅ **Dynamic Patterns**: Recursive printing, no hardcoded values
- ✅ **Single Responsibility**: Clear function scope validation

### **🚀 Ready for Next Development Phase**

#### **Next Target: Micro-Increment 2 - VideoLoader Class**
**Goal**: Basic OpenCV VideoCapture with property validation
**Scope**: Single `load_video()` method with comprehensive validation
**Foundation**: All infrastructure ready - focus purely on component logic

**Developer Agent can now proceed with confidence:**
- Configuration system operational
- Logging infrastructure ready  
- Testing framework established
- Educational patterns demonstrated
- Integration points designed

**This foundation enables efficient, professional development of remaining video input functionality.**

### **CRITICAL: Micro-Incremental Execution Instructions**

**You have complete component context and specifications. However, you MUST build in micro-increments:**

#### **Execution Rules:**
1. **Start with the smallest possible piece** - Single function, single capability
2. **Build → Test → Validate → Proceed** - Never skip validation
3. **No combination building** - One piece at a time only
4. **User approval required** before major progression

#### **CRITICAL BEHAVIORAL PATTERNS:**

**Test Design and Validation:**
- ✅ **Always verify test cases match actual function responsibility**
- ✅ **Question test assumptions before writing** - what should this function actually do?
- ✅ **Don't assume edge cases are failures** - validate against single responsibility principle
- ✅ **When tests fail, first ask: "Should this actually fail?"**
- ✅ **Distinguish between code bugs vs incorrect test expectations**

**Content Review Before Updates:**
- ✅ **Read existing file content first** to identify redundancies/conflicts
- ✅ **Remove conflicting/outdated content** when adding new features
- ✅ **Clean up while adding** - don't just append
- ✅ **Avoid redundant information** in the same file

**Function Scope Validation:**
- ✅ **Single responsibility principle** - test what the function claims to do
- ✅ **Function name should match function scope** (e.g., validate_video_format = extension validation only)
- ✅ **When making design choices, explicitly state what function will/won't do**
- ✅ **Align all related components** (tests, docs, implementation) with design decisions

**Authorization Requirement:**
- ✅ **NEVER make file edits without explicit user approval**
- ✅ **Always ask "Should I make this change?" before editing**
- ✅ **Show proposed changes and request approval first**

#### **Video Input Module - Recommended Micro-Sequence:**
1. **File existence check** - Single function only
2. **Format validation** - Single function only  
3. **Basic OpenCV file opening** - VideoCapture creation only
4. **Property extraction** - fps, frame count only
5. **Single frame read** - Frame 0 extraction only
6. **Frame validation** - Check numpy array validity
7. **Basic resize function** - Simple preprocessing only
8. **Error handling layer** - Add try-catch patterns
9. **Class integration** - Combine functions into VideoLoader/VideoProcessor

#### **After Each Micro-Piece:**
- **Write unit test** for that specific piece
- **Test manually** with real video file
- **Validate educational comments** are comprehensive
- **Confirm integration points** with existing pieces
- **Request user approval** before proceeding

#### **Validation Gates:**
- **No exceptions** - All error scenarios handled gracefully
- **Educational value** - Extensive comments explaining concepts
- **Professional quality** - Clean, readable code
- **Test coverage** - Unit tests for each piece
- **Integration ready** - Designed for future component connections

---

## DEVELOPMENT EXECUTION APPROACH
1. **Build Video Input Module** → Test independently
2. **Build Pose Detection Engine** → Test independently  
3. **Build GUI Framework** → Test independently
4. **Integration Testing** → Test all components together

### **Quality Gates**
- **Each micro-increment** must pass validation before proceeding
- **No combination building** - one piece at a time only
- **Immediate testing** required after each addition
- **User approval** gates between major increments
- **Regression validation** before adding new functionality

### **Educational Documentation Requirements**
- Inline comments explaining computer vision concepts
- README files in each module explaining purpose and design
- Examples demonstrating key functionality
- Architecture decision documentation

---

## DEVELOPER AGENT SUCCESS CRITERIA

### **Micro-Incremental Execution (CRITICAL):**
- [ ] **Start small** - Build single functions before classes
- [ ] **Test immediately** - Unit test each piece before proceeding  
- [ ] **Educational comments** - Explain CV concepts in every function
- [ ] **Request approval** - Ask for validation before major progression
- [ ] **No combination building** - One capability at a time only

### **Technical Competence**
- [ ] Understand video processing fundamentals (OpenCV)
- [ ] Grasp pose detection concepts (MediaPipe)
- [ ] Apply GUI development patterns (PyQt6)
- [ ] Implement proper error handling and logging
- [ ] Follow project file structure and naming conventions

### **Educational Code Quality**
- [ ] Write extensive explanatory comments
- [ ] Use clear, descriptive variable names  
- [ ] Structure code for maximum readability
- [ ] Include educational notes about CV concepts
- [ ] Provide usage examples and documentation

### **Integration Understanding**
- [ ] Design components for loose coupling
- [ ] Implement proper data flow between modules
- [ ] Handle configuration management consistently
- [ ] Plan for future phase requirements

**This bootstrap document provides complete foundation knowledge for developing Phase 1 components with professional quality and educational clarity.**

---

## SESSION TRACKING REQUIREMENTS

### **Developer Agent Context Evolution**
**Create/Update**: `developer_session_log.md` in this component folder
**Purpose**: Capture development insights for architect context evolution

### **Document Everything**
**Capture After Each Micro-Increment**:
- Every micro-increment attempted and result
- Design decisions made during implementation
- Issues encountered and solutions found
- Testing approaches and results
- Integration insights discovered
- Performance observations
- Educational insights gained

### **Session Log Format Pattern**:
```markdown
## Micro-Increment [N]: [Description]
**Date**: [timestamp]
**Goal**: [specific objective]
**Implementation**: [what was built]
**Testing**: [validation performed]
**Issues**: [problems encountered]
**Solutions**: [how resolved]
**Integration Notes**: [connection points for future components]
**Educational Value**: [concepts demonstrated]
**Next**: [what comes next]
```

### **Critical Notes**
- **Never skip** session logging - architect needs this for methodology evolution
- **Start immediately** with file existence check documentation
- **Update after every micro-increment** - no matter how small
- **Include code snippets** and testing results in the log
