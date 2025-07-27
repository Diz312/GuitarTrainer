# Component 1: Video Input Module - Visual Architecture

## 🏗️ Component Class Diagram

```mermaid
classDiagram
    class VideoLoader {
        -config: VideoConfig
        -current_video: VideoCapture
        -logger: Logger
        -supported_formats: List[str]
        +__init__(config: VideoConfig)
        +load_video(file_path: Path) bool
        +get_video_info() Dict[str, Any]
        +is_video_loaded() bool
        +close_video() None
        +validate_format(file_path: Path) bool
    }
    
    class VideoProcessor {
        -video_loader: VideoLoader
        -logger: Logger
        +__init__(video_loader: VideoLoader)
        +extract_frame(frame_number: int) Optional[ndarray]
        +extract_frames_batch(start_frame: int, count: int) List[ndarray]
        +preprocess_frame(frame: ndarray) ndarray
        +get_frame_count() int
        +get_fps() float
    }
    
    class VideoUtils {
        <<utility>>
        +get_supported_formats() List[str]
        +validate_video_properties(video_cap: VideoCapture) Dict[str, bool]
        +format_duration(total_seconds: float) str
        +resize_frame_if_needed(frame: ndarray, max_size: Tuple) ndarray
        +convert_frame_bgr_to_rgb(frame: ndarray) ndarray
    }
    
    class VideoConfig {
        +supported_formats: List[str]
        +max_resolution: Tuple[int, int]
        +target_fps: int
    }
    
    VideoProcessor --> VideoLoader : depends on
    VideoLoader --> VideoConfig : uses
    VideoLoader --> VideoUtils : calls
    VideoProcessor --> VideoUtils : calls
    
    note for VideoLoader "Handles file I/O and validation.\nManages OpenCV VideoCapture lifecycle."
    note for VideoProcessor "Extracts and preprocesses frames.\nProvides clean numpy arrays for CV."
    note for VideoUtils "Utility functions for common\nvideo operations and validation."
```

## 🔄 Data Flow Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant GUI
    participant VideoLoader
    participant VideoProcessor
    participant OpenCV
    participant PoseDetection
    
    User->>GUI: Select video file
    GUI->>VideoLoader: load_video(file_path)
    VideoLoader->>VideoLoader: validate_format(file_path)
    
    alt Valid format
        VideoLoader->>OpenCV: VideoCapture(file_path)
        OpenCV-->>VideoLoader: video_capture_object
        VideoLoader->>VideoLoader: validate_video_properties()
        
        alt Valid properties
            VideoLoader-->>GUI: True (success)
            GUI->>VideoLoader: get_video_info()
            VideoLoader-->>GUI: video_metadata
            
            loop For each frame needed
                GUI->>VideoProcessor: extract_frame(frame_number)
                VideoProcessor->>VideoLoader: get current_video
                VideoProcessor->>OpenCV: read_frame(frame_number)
                OpenCV-->>VideoProcessor: raw_frame
                VideoProcessor->>VideoProcessor: preprocess_frame(raw_frame)
                VideoProcessor-->>GUI: processed_frame
                GUI->>PoseDetection: detect_pose(processed_frame)
            end
            
        else Invalid properties
            VideoLoader-->>GUI: False (invalid video)
            GUI->>User: Show error message
        end
        
    else Invalid format
        VideoLoader-->>GUI: False (unsupported format)
        GUI->>User: Show format error
    end
```

## 🔗 Component Integration Diagram

```mermaid
graph TD
    A[🖥️ GUI Module] -->|file_path| B[📁 VideoLoader]
    B -->|video_metadata| A
    B -->|VideoCapture| C[🎞️ VideoProcessor]
    C -->|numpy.ndarray frames| D[🤖 Pose Detection]
    C -->|display frames| A
    
    E[⚙️ VideoConfig] --> B
    F[🛠️ VideoUtils] --> B
    F --> C
    
    B -->|BGR frames| G[📊 OpenCV VideoCapture]
    D -->|pose_landmarks| A
    
    classDef gui fill:#e1f5fe
    classDef video fill:#f3e5f5
    classDef cv fill:#e8f5e8
    classDef config fill:#fff3e0
    
    class A gui
    class B,C video
    class D,G cv
    class E,F config
```

## ⚠️ Error Handling State Diagram

```mermaid
stateDiagram-v2
    [*] --> FileSelection
    FileSelection --> FormatValidation: user selects file
    
    FormatValidation --> LoadVideo: format supported
    FormatValidation --> FormatError: unsupported format
    
    LoadVideo --> PropertyValidation: file opened successfully
    LoadVideo --> FileError: cannot open file
    
    PropertyValidation --> Ready: valid video properties
    PropertyValidation --> PropertyError: invalid fps/frames
    
    Ready --> FrameExtraction: extract_frame() called
    FrameExtraction --> Ready: frame extracted successfully
    FrameExtraction --> FrameError: corrupted frame
    
    Ready --> Closed: close_video() called
    
    FormatError --> [*]: show error message
    FileError --> [*]: show error message  
    PropertyError --> [*]: show error message
    FrameError --> Ready: skip corrupted frame
    Closed --> [*]: cleanup complete
    
    note right of Ready
        Video loaded and ready
        for frame processing
    end note
    
    note right of FrameError
        Handle corrupted frames
        gracefully - skip and continue
    end note
```

## 🏛️ Module Architecture Overview

```mermaid
graph LR
    subgraph "Video Input Module"
        A[video_loader.py<br/>📁 VideoLoader Class]
        B[video_processor.py<br/>🎞️ VideoProcessor Class] 
        C[video_utils.py<br/>🛠️ Utility Functions]
        D[__init__.py<br/>📋 Module Exports]
    end
    
    subgraph "External Dependencies"
        E[OpenCV<br/>cv2.VideoCapture]
        F[NumPy<br/>ndarray operations]
        G[Pathlib<br/>file path handling]
    end
    
    subgraph "Project Integration"
        H[Config Module<br/>⚙️ Settings]
        I[GUI Module<br/>🖥️ Interface]
        J[Pose Detection<br/>🤖 Analysis]
    end
    
    A --> E
    A --> G
    B --> A
    B --> F
    C --> E
    C --> F
    D --> A
    D --> B
    D --> C
    
    H --> A
    I --> A
    I --> B
    B --> J
    
    classDef module fill:#bbdefb
    classDef external fill:#c8e6c9
    classDef integration fill:#ffcdd2
    
    class A,B,C,D module
    class E,F,G external
    class H,I,J integration
```

## 📊 Method Call Flow

```mermaid
flowchart TD
    Start([User Loads Video]) --> A{File Exists?}
    
    A -->|No| Error1[FileNotFoundError]
    A -->|Yes| B[validate_format()]
    
    B --> C{Supported Format?}
    C -->|No| Error2[UnsupportedFormatError]
    C -->|Yes| D[cv2.VideoCapture()]
    
    D --> E{Video Opens?}
    E -->|No| Error3[VideoLoadError]
    E -->|Yes| F[validate_video_properties()]
    
    F --> G{Valid Properties?}
    G -->|No| Error4[InvalidVideoError]
    G -->|Yes| H[Store VideoCapture]
    
    H --> I[Return Success]
    I --> J[Ready for Frame Extraction]
    
    J --> K[extract_frame(n)]
    K --> L[set_frame_position(n)]
    L --> M[read_frame()]
    M --> N{Frame Read OK?}
    
    N -->|No| O[Skip/Log Warning]
    N -->|Yes| P[preprocess_frame()]
    P --> Q[resize_if_needed()]
    Q --> R[Return numpy.ndarray]
    
    O --> J
    R --> S[Frame Ready for Pose Detection]
    
    Error1 --> End([Log Error & Exit])
    Error2 --> End
    Error3 --> End
    Error4 --> End
    
    classDef success fill:#c8e6c9
    classDef error fill:#ffcdd2
    classDef process fill:#e1f5fe
    classDef decision fill:#fff3e0
    
    class I,H,R,S success
    class Error1,Error2,Error3,Error4,End error
    class B,D,F,K,L,M,P,Q process
    class A,C,E,G,N decision
```

## 🎓 Educational Concepts Map

```mermaid
mindmap
  root((Video Input Module))
    Computer Vision Fundamentals
      Video as Image Sequences
        Frame Rate (FPS)
        Color Spaces (BGR/RGB)
        Resolution & Aspect Ratio
      OpenCV Integration
        VideoCapture Class
        Frame Reading Methods
        Format Support
    Software Engineering Patterns
      Resource Management
        RAII Pattern
        Try-Finally Blocks
        Memory Cleanup
      Error Handling
        Exception Hierarchies
        Graceful Degradation
        User Feedback
      Design Patterns
        Facade Pattern
        Strategy Pattern
        Observer Pattern
    Data Processing
      Frame Preprocessing
        Resizing Algorithms
        Color Space Conversion
        Normalization
      Batch Processing
        Memory Management
        Performance Optimization
        Progress Tracking
    Integration Architecture
      Module Boundaries
        Clear Interfaces
        Dependency Injection
        Loose Coupling
      Data Flow Design
        Input Validation
        Transformation Pipeline
        Output Standardization
```

## 📋 Component Responsibilities Matrix

| Component | Primary Responsibility | Key Methods | Integration Points |
|-----------|----------------------|-------------|-------------------|
| **VideoLoader** | File I/O & Validation | `load_video()`, `validate_format()` | → GUI (file dialogs)<br/>→ Config (settings) |
| **VideoProcessor** | Frame Operations | `extract_frame()`, `preprocess_frame()` | → VideoLoader (source)<br/>→ Pose Detection (output) |
| **VideoUtils** | Common Operations | `resize_frame_if_needed()`, `validate_properties()` | ← VideoLoader<br/>← VideoProcessor |
| **Module Interface** | API Boundary | `__init__.py` exports | → All external modules |

## 🔧 Technical Implementation Notes

### Key Design Decisions:
1. **Composition over Inheritance**: VideoProcessor depends on VideoLoader rather than extending it
2. **Error Isolation**: Each component handles its own errors without propagating failures
3. **Resource Management**: Explicit cleanup methods for OpenCV VideoCapture objects
4. **Stateless Utilities**: VideoUtils functions are pure functions for maximum reusability
5. **Configuration Injection**: Dependencies passed via constructor for testability

### Performance Considerations:
- Frame extraction optimized for sequential access patterns
- Memory usage minimized through immediate frame processing
- Batch operations available for bulk frame extraction
- Preprocessing only applied when necessary (size/format checks)

### Educational Value:
- Clear separation of concerns demonstrates modular design
- Error handling patterns show robust software development
- OpenCV integration teaches computer vision fundamentals
- Resource management illustrates systems programming concepts