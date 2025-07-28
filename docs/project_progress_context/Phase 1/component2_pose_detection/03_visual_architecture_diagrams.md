# Component 2 Visual Architecture Diagrams - MediaPipe Pose Detection

## 🎨 **UML/MERMAID ARCHITECTURE VISUALIZATIONS**

**Component:** MediaPipe Pose Detection Engine  
**Purpose:** Visual understanding of pose detection architecture, data flow, and integration patterns  
**Format:** Professional UML/Mermaid diagrams for educational clarity  

---

## 🏗️ **COMPONENT ARCHITECTURE OVERVIEW**

### **System Integration Diagram**
```mermaid
graph TD
    A[VideoLoader] -->|np.ndarray frames| B[MediaPipeDetector]
    B -->|pose landmarks| C[LandmarkExtractor]
    C -->|guitar landmarks| D[PoseDetectionResult]
    D -->|structured output| E[Component 3<br/>Analysis Engine]
    
    F[Config System] -->|pose settings| B
    G[Logger Factory] -->|component logger| B
    H[Test Fixtures] -->|test_video.mp4| A
    
    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#f3e5f5
    style D fill:#e8f5e8
    style E fill:#fff8e1
```

### **Data Flow Architecture**
```mermaid
sequenceDiagram
    participant VL as VideoLoader
    participant MD as MediaPipeDetector
    participant LE as LandmarkExtractor
    participant PR as PoseDetectionResult
    
    VL->>MD: get_next_frame()
    Note over VL,MD: np.ndarray (BGR format)
    
    MD->>MD: convert BGR→RGB
    MD->>MD: MediaPipe.process()
    
    MD->>LE: extract_pose_landmarks()
    Note over MD,LE: Raw MediaPipe results
    
    LE->>LE: filter_by_confidence()
    LE->>LE: extract_guitar_landmarks()
    LE->>LE: normalize_coordinates()
    
    LE->>PR: create_result_structure()
    Note over LE,PR: Structured guitar landmarks
    
    PR-->>MD: PoseDetectionResult
    MD-->>VL: detection complete
```

---

## 🔬 **MICRO-INCREMENTAL DEVELOPMENT FLOW**

### **Development Sequence Diagram**
```mermaid
graph LR
    A[1. MediaPipe<br/>Init] --> B[2. Frame<br/>Processing]
    B --> C[3. Landmark<br/>Extraction]
    C --> D[4. Confidence<br/>Filtering]
    D --> E[5. Guitar<br/>Selection]
    E --> F[6. Coordinate<br/>Conversion]
    F --> G[7. Result<br/>Structure]
    G --> H[8. Pipeline<br/>Integration]
    H --> I[9. Class<br/>Wrapper]
    
    style A fill:#ffebee
    style B fill:#f3e5f5
    style C fill:#e8eaf6
    style D fill:#e0f2f1
    style E fill:#fff3e0
    style F fill:#fce4ec
    style G fill:#e1f5fe
    style H fill:#f1f8e9
    style I fill:#fff8e1
```

### **Validation Gates Flow**
```mermaid
stateDiagram-v2
    [*] --> Build
    Build --> Test
    Test --> Validate
    Validate --> UserApproval
    UserApproval --> NextIncrement: Approved
    UserApproval --> Build: Rejected
    NextIncrement --> Build: More increments
    NextIncrement --> Complete: All done
    Complete --> [*]
    
    Test : Unit Test + Manual Test
    Validate : Educational Comments + Integration Check
    UserApproval : Request progression permission
```

---

## 🧠 **MEDIAPIPE INTEGRATION ARCHITECTURE**

### **MediaPipe Processing Pipeline**
```mermaid
graph TD
    A[Input Frame<br/>BGR Format] --> B[Color Conversion<br/>BGR → RGB]
    B --> C[MediaPipe Pose<br/>Model Processing]
    C --> D{Pose Detected?}
    
    D -->|Yes| E[33 Landmarks<br/>Normalized Coords]
    D -->|No| F[No Detection<br/>Return None]
    
    E --> G[Confidence Filtering<br/>Threshold: 0.7]
    G --> H[Guitar Landmark<br/>Selection]
    H --> I[Coordinate<br/>Transformation]
    I --> J[Structured Result<br/>Output]
    
    F --> K[Graceful Error<br/>Handling]
    K --> J
    
    style A fill:#ffebee
    style C fill:#e3f2fd
    style E fill:#e8f5e8
    style J fill:#fff3e0
```

### **Landmark Mapping Visualization**
```mermaid
graph TB
    subgraph "MediaPipe 33 Landmarks"
        A[0-10: Face/Head]
        B[11-12: Shoulders]
        C[13-16: Arms/Wrists]
        D[17-22: Hands]
        E[23-32: Torso/Legs]
    end
    
    subgraph "Guitar-Relevant Selection"
        F[Shoulders: 11,12]
        G[Elbows: 13,14]
        H[Wrists: 15,16]
        I[Hands: 17-22]
    end
    
    B --> F
    C --> G
    C --> H
    D --> I
    
    style B fill:#e8f5e8
    style C fill:#fff3e0
    style D fill:#f3e5f5
    style F fill:#c8e6c9
    style G fill:#ffecb3
    style H fill:#f8bbd9
    style I fill:#e1bee7
```

---

## 🏛️ **CLASS ARCHITECTURE DESIGN**

### **Component Class Relationships**
```mermaid
classDiagram
    class MediaPipeDetector {
        -config: PoseDetectionConfig
        -logger: Logger
        -pose_model: MediaPipePose
        +__init__()
        +detect_pose(frame) PoseDetectionResult
        +is_initialized() bool
        +get_detection_stats() Dict
        +cleanup() None
    }
    
    class LandmarkExtractor {
        -confidence_threshold: float
        +extract_guitar_landmarks(results) Dict
        +filter_by_confidence(landmarks) Dict
        +normalize_coordinates(landmarks) Dict
        +validate_pose_completeness(landmarks) bool
    }
    
    class PoseDetectionResult {
        +success: bool
        +landmarks: Dict
        +confidence: float
        +metadata: Dict
        +is_valid_detection() bool
        +get_landmark_count() int
        +to_dict() Dict
    }
    
    class VideoLoader {
        +get_next_frame() np.ndarray
        +is_video_loaded() bool
        +get_video_info() Dict
    }
    
    VideoLoader --> MediaPipeDetector : provides frames
    MediaPipeDetector --> LandmarkExtractor : uses
    MediaPipeDetector --> PoseDetectionResult : creates
    LandmarkExtractor --> PoseDetectionResult : populates
```

### **Configuration Integration Pattern**
```mermaid
graph LR
    A[config/10_project_config.yaml] --> B[ConfigManager]
    B --> C[get_project_config()]
    C --> D[pose_detection section]
    D --> E[MediaPipeDetector]
    
    subgraph "Config Hierarchy"
        F[pose_detection.core]
        G[pose_detection.guitar_analysis]
        H[pose_detection.performance]
        I[pose_detection.output]
    end
    
    D --> F
    D --> G
    D --> H
    D --> I
    
    style A fill:#e3f2fd
    style E fill:#fff3e0
```

---

## 🧪 **TESTING ARCHITECTURE**

### **Test Integration Flow**
```mermaid
graph TD
    A[test_video.mp4<br/>Fixture] --> B[VideoLoader<br/>Integration Test]
    B --> C[MediaPipeDetector<br/>Unit Tests]
    C --> D[LandmarkExtractor<br/>Unit Tests]
    D --> E[PoseDetectionResult<br/>Validation Tests]
    
    F[Manual Testing<br/>__main__ sections] --> G[Dynamic Result<br/>Display]
    
    H[pytest Framework] --> C
    H --> D
    H --> E
    H --> I[Integration Tests<br/>Full Pipeline]
    
    style A fill:#e8f5e8
    style F fill:#fff3e0
    style H fill:#f3e5f5
```

### **Validation Strategy Diagram**
```mermaid
sequenceDiagram
    participant Dev as Developer
    participant UT as Unit Tests
    participant MT as Manual Test
    participant User as User Review
    
    Dev->>UT: Run automated tests
    UT-->>Dev: Pass/Fail results
    
    Dev->>MT: Execute __main__ demo
    MT-->>Dev: Visual validation
    
    Dev->>User: Request approval
    User-->>Dev: Approve/Reject
    
    Note over Dev,User: Repeat for each micro-increment
```

---

## 🔗 **INTEGRATION PREPARATION**

### **Component 3 Interface Design**
```mermaid
graph LR
    A[Component 2<br/>PoseDetectionResult] --> B[Component 3<br/>Analysis Engine]
    
    subgraph "Data Structure"
        C[detection_success: bool]
        D[landmarks: Dict]
        E[average_confidence: float]
        F[metadata: Dict]
    end
    
    A --> C
    A --> D
    A --> E
    A --> F
    
    subgraph "Analysis Engine Input"
        G[Biomechanical Calculator]
        H[Technique Evaluator]
        I[Posture Analyzer]
    end
    
    B --> G
    B --> H
    B --> I
    
    style A fill:#fff3e0
    style B fill:#e8f5e8
```

### **Future Pipeline Extension**
```mermaid
graph TD
    A[VideoLoader] --> B[MediaPipeDetector]
    B --> C[Component 3<br/>Analysis Engine]
    C --> D[Component 4<br/>Feedback Engine]
    D --> E[Component 5<br/>GUI Display]
    
    F[Training Data] --> G[Component 6<br/>Learning Pipeline]
    G --> C
    
    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#e8f5e8
    style D fill:#f3e5f5
    style E fill:#ffecb3
    style F fill:#fce4ec
    style G fill:#f1f8e9
```

---

## 📊 **PERFORMANCE CONSIDERATIONS**

### **Processing Timeline**
```mermaid
gantt
    title Component 2 Processing Timeline
    dateFormat X
    axisFormat %s ms
    
    section Frame Processing
    BGR→RGB Conversion    :0, 2
    MediaPipe Detection   :2, 15
    Landmark Extraction   :15, 18
    
    section Analysis Prep
    Confidence Filtering  :18, 20
    Guitar Selection      :20, 22
    Coordinate Transform  :22, 25
    
    section Result Creation
    Structure Assembly    :25, 27
    Metadata Generation   :27, 30
```

### **Memory Usage Pattern**
```mermaid
graph LR
    A[Input Frame<br/>~2MB] --> B[RGB Conversion<br/>~2MB]
    B --> C[MediaPipe Process<br/>~4MB peak]
    C --> D[Landmarks Dict<br/>~1KB]
    D --> E[Filtered Results<br/>~500B]
    E --> F[Final Structure<br/>~1KB]
    
    style A fill:#ffebee
    style C fill:#fff3e0
    style F fill:#e8f5e8
```

**These diagrams provide complete visual understanding of Component 2 architecture, enabling clear implementation and integration with existing infrastructure.**