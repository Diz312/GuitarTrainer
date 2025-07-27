# GuitarTrainer Project-Specific Context\n\n## 🎯 **CURRENT PROJECT STATE**\n\n### **Project Overview**\n**Name**: GuitarTrainer - Computer Vision Guitar Technique Analysis  \n**Purpose**: Analyze guitar playing technique using pose estimation, providing biomechanical feedback for improvement  \n**Approach**: Educational learning project with professional quality standards  \n**Platform**: Desktop application (Windows/macOS/Linux)  \n\n### **Development Status**\n**Phase**: Component 1 (Video Input Module) - Ready for Development  \n**Architecture**: Complete and documented  \n**Infrastructure**: Project structure, documentation, and environment setup complete  \n**Next Action**: Begin micro-incremental development of video input functionality  \n\n---\n\n## 🏗️ **ARCHITECTURE DECISIONS MADE**\n\n### **Technology Stack Selected**\n- **Core Language**: Python 3.9+ (educational value, rapid development)\n- **Computer Vision**: OpenCV 4.8+ (video processing), MediaPipe 0.10+ (pose detection)\n- **Machine Learning**: scikit-learn 1.3+ (analysis algorithms)\n- **GUI Framework**: PyQt6 6.5+ (professional desktop interface)\n- **Database**: SQLite with SQLAlchemy 2.0+ (training data storage)\n- **Environment**: UV for Python package management\n\n### **System Architecture**\n```\nVideo Input → Pose Detection → Analysis Engine → Feedback Engine → GUI\n     ↓              ↓              ↓              ↓           ↑\nVideoLoader → MediaPipeDetector → BiomechAnalysis → ScoreGen → Display\nVideoProcessor → LandmarkExtractor → TechniqueEval → Recommendations → Controls\n```\n\n### **Component Organization**\n- **Phase 1**: Video Input + Pose Detection + Basic GUI (Foundation)\n- **Phase 2**: Analysis Engine + Feedback System (Core Features)\n- **Phase 3**: Training Data Management + Manual Annotation (Learning Infrastructure)\n- **Phase 4**: Continuous Learning Pipeline + Auto-Retraining (Intelligence)\n- **Phase 5**: Advanced Features + Performance Optimization (Polish)\n\n---\n\n## 📊 **BIOMECHANICAL ANALYSIS SPECIFICATIONS**\n\n### **Target Body Parts for Analysis**\n1. **Shoulder Alignment**\n   - **Landmarks**: Left shoulder (11), Right shoulder (12)\n   - **Metrics**: Angle deviation from horizontal, forward head posture\n   - **Good Range**: ±5 degrees from level\n   - **Analysis**: Posture symmetry and alignment\n\n2. **Right Wrist Position** (Picking Hand)\n   - **Landmarks**: Right wrist (16), related hand landmarks\n   - **Metrics**: Wrist angle relative to neutral, deviation patterns\n   - **Good Range**: 10-20 degrees extension\n   - **Analysis**: Picking motion stability and ergonomics\n\n3. **Right Hand Movement** (Picking Motion)\n   - **Landmarks**: Right hand landmarks (21 points)\n   - **Metrics**: Movement consistency, picking arc smoothness\n   - **Analysis**: Motion patterns, tension indicators, efficiency\n\n4. **Left Hand Fingers** (Fretting Hand)\n   - **Landmarks**: Left hand landmarks (21 points)\n   - **Metrics**: Individual finger curvature, positioning accuracy\n   - **Good Range**: Curved fingers, perpendicular to fretboard\n   - **Analysis**: Finger independence, placement precision\n\n### **Analysis Progression Strategy**\n**Critical**: Implement one body part at a time, never multiple simultaneously\n1. **Start**: Shoulder alignment analysis only\n2. **Test thoroughly**: Ensure shoulder detection works reliably\n3. **Add**: Right wrist analysis only\n4. **Test integration**: Shoulder + wrist together\n5. **Continue**: Right hand movement analysis\n6. **Final**: Left hand finger analysis\n\n---\n\n## 🔧 **DEVELOPMENT METHODOLOGY ESTABLISHED**\n\n### **Micro-Incremental Development Rules**\n1. **Smallest Possible Pieces**: Single function, single capability only\n2. **Build → Test → Validate → Proceed**: Never skip validation steps\n3. **No Combination Building**: One piece at a time, always\n4. **User Approval Gates**: Request validation before major progression\n5. **Educational Focus**: Extensive comments explaining CV concepts\n\n### **Component 1 (Video Input) Micro-Sequence**\n1. **File existence check** - Single function only\n2. **Format validation** - Single function only  \n3. **Basic OpenCV file opening** - VideoCapture creation only\n4. **Property extraction** - fps, frame count only\n5. **Single frame read** - Frame 0 extraction only\n6. **Frame validation** - Check numpy array validity\n7. **Basic resize function** - Simple preprocessing only\n8. **Error handling layer** - Add try-catch patterns\n9. **Class integration** - Combine functions into VideoLoader/VideoProcessor\n\n### **Validation Requirements**\n- **Unit test** for each micro-increment\n- **Manual testing** with real video files\n- **Educational comments** comprehensive and clear\n- **Integration readiness** designed for future connections\n- **Error handling** graceful failures, no crashes\n\n---\n\n## 📁 **PROJECT STRUCTURE IMPLEMENTED**\n\n### **Source Code Organization**\n```\nsrc/\n├── main.py                     # Application entry point\n├── video_input/                # Component 1 (Current Focus)\n│   ├── video_loader.py        # File loading and validation\n│   ├── video_processor.py     # Frame extraction and preprocessing\n│   └── video_utils.py         # Helper functions\n├── pose_detection/             # Component 2 (Next)\n├── gui/                        # Component 3 (Next)\n├── analysis/                   # Phase 2 components\n├── training/                   # Phase 3 components\n├── feedback/                   # Phase 2 components\n├── continuous_learning/        # Phase 4 components\n└── config/\n    └── settings.py            # Configuration management\n```\n\n### **Documentation Structure**\n```\ndocs/\n├── 00_ARCHITECT_SESSION_LOG.md          # Core methodology (lean)\n├── 01_COLLABORATION_PATTERNS.md         # User preferences & communication\n├── 02_METHODOLOGY_EVOLUTION.md          # How approaches evolved\n├── 03_DECISION_RATIONALE_LIBRARY.md     # Why specific choices made\n├── 04_EFFICIENCY_OPTIMIZATIONS.md       # Discovered improvements\n├── 05_PROJECT_SPECIFIC_CONTEXT.md       # This file - current project state\n└── component1_video_input/              # Component-specific documentation\n    ├── bootstrap_instructions.md        # Developer agent foundation\n    ├── context_validation_tests.md      # Comprehension tests\n    ├── technical_specifications.md      # Implementation details\n    └── visual_architecture_diagrams.md  # UML/Mermaid diagrams\n```\n\n---\n\n## 🎓 **EDUCATIONAL OBJECTIVES**\n\n### **Computer Vision Concepts to Learn**\n1. **Video I/O Fundamentals**\n   - OpenCV VideoCapture usage\n   - Frame extraction and preprocessing\n   - Video property validation\n   - Memory management for video processing\n\n2. **Pose Estimation Concepts**\n   - MediaPipe framework integration\n   - Confidence threshold filtering\n   - Coordinate system transformations\n   - Real-time vs batch processing\n\n3. **Biomechanical Analysis**\n   - Anatomical landmark mapping\n   - Angle calculations and metrics\n   - Movement pattern analysis\n   - Statistical validation techniques\n\n4. **Machine Learning Pipeline**\n   - Training data collection and annotation\n   - Feature extraction from pose data\n   - Model training and validation\n   - Continuous learning implementation\n\n### **Software Engineering Skills**\n1. **Modular Architecture Design**\n   - Component separation and interfaces\n   - Dependency injection patterns\n   - Configuration management\n   - Error handling strategies\n\n2. **Testing and Validation**\n   - Unit testing for CV applications\n   - Integration testing strategies\n   - Manual testing procedures\n   - Performance validation\n\n3. **Documentation and Communication**\n   - Technical specification writing\n   - UML/Mermaid diagram creation\n   - Educational code commenting\n   - Architecture decision documentation\n\n---\n\n## 🚀 **IMMEDIATE NEXT ACTIONS**\n\n### **Ready for Development**\n**Status**: All architecture, documentation, and infrastructure complete  \n**Next Step**: Begin Component 1 micro-incremental development  \n**Starting Point**: File existence check function implementation  \n\n### **Developer Agent Bootstrap Requirements**\n1. **Load**: `component1_video_input/bootstrap_instructions.md` for complete context\n2. **Validate**: Understanding through context validation tests if needed\n3. **Begin**: Micro-increment 1 - file existence check function only\n4. **Test**: Unit test and manual validation before proceeding\n5. **Request**: User approval before moving to next micro-increment\n\n### **Success Criteria for Component 1**\n- [ ] All 9 micro-increments completed and validated\n- [ ] VideoLoader and VideoProcessor classes fully functional\n- [ ] Comprehensive unit test coverage\n- [ ] Integration with Configuration system\n- [ ] Error handling for all edge cases\n- [ ] Educational code comments throughout\n- [ ] Ready for Component 2 (Pose Detection) integration\n\n---\n\n## 📈 **PROJECT SUCCESS METRICS**\n\n### **Technical Metrics**\n- **Performance**: Process 30-second video in <60 seconds\n- **Accuracy**: >85% pose detection confidence on guitar videos\n- **Reliability**: Handle error scenarios without crashes\n- **Scalability**: Support videos up to 1080p resolution\n\n### **Educational Metrics**\n- **Code Quality**: Extensive educational comments and examples\n- **Concept Coverage**: All major CV concepts demonstrated\n- **Professional Practices**: Industry-standard patterns and documentation\n- **Learning Progression**: Logical skill building from basic to advanced\n\n### **User Experience Metrics**\n- **Usability**: Intuitive interface for video upload and analysis\n- **Feedback Quality**: Actionable technique improvement suggestions\n- **Learning Value**: Clear explanations of analysis results\n- **Progress Tracking**: Visible improvement over multiple sessions\n\n**This project context provides complete current state information for efficient continuation of development work.**

---

## 🔄 **LATEST SESSION UPDATES**

### **Context Optimization Implementation**
**Date**: Current Session  
**Action**: Implemented hierarchical documentation strategy to manage context window limits

**Changes Made**:
- **Created**: Specialized knowledge files in `architect_agent_context/` directory
- **Separated**: Architect context from project documentation
- **Optimized**: Master session log to be lean with cross-references
- **Established**: "update sesh" protocol for maintaining architect context

### **Directory Organization Refinement**
**User Instruction**: "Place the optimized context files into a separate subdirectory called 'architect_agent_context'"

**Implementation**:
- **Moved**: All architect session logs to dedicated subdirectory
- **Clarified**: Separation between MY context and other agent contexts
- **Established**: Clear distinction between architect logs and technical documentation

### **Setup Documentation Simplification**
**User Instruction**: "Clean up the SETUP_COMMANDS.md file. It is full of specific paths for this machine."

**Optimization**:
- **Removed**: Machine-specific paths (E:\Python\GitHub\GuitarTrainer)
- **Replaced**: With generic `/path/to/GuitarTrainer` placeholder
- **Simplified**: Content from ~500 lines to ~100 essential commands
- **Made Platform Agnostic**: Works for Windows, macOS, Linux
- **Focused**: On essential setup and daily workflow commands only

### **Context Management Protocol Established**
**Understanding Confirmed**:
- **`architect_agent_context/`** = MY session logs, learning, and context evolution ONLY
- **`component1_video_input/`** = Component specifications and technical documentation
- **Other agents** = Would have separate context directories if created
- **"update sesh"** = Update MY context files in architect_agent_context/ only

### **Documentation Folder Structure Evolution**
**User Instruction**: "Use number prefixes in the component instruction files for the developer agent. Rename the files in the order they should be viewed and used with the developer agent. Also notice that I updated the folder structure so that its organized by phase matching the phases articulated in the development timeline."

**Implementation**:
- **Phase-Based Organization**: Restructured docs into phase-specific folders
  - `docs/Phase1/` - Foundation phase (basic video + pose detection)
  - `docs/Phase2/` - Core features (analysis + feedback) 
  - `docs/Phase3/` - Learning infrastructure (training tools)
  - `docs/Phase4/` - Intelligence (smart learning)
  - `docs/Phase5/` - Polish (advanced features)
- **Component File Numbering**: Added sequential prefixes for developer agent workflow
  - `01_bootstrap_instructions.md` - Complete foundation knowledge (start here)
  - `02_context_validation_tests.md` - Verify understanding before coding
  - `03_visual_architecture_diagrams.md` - Visual structure understanding
  - `04_technical_specifications.md` - Detailed implementation requirements

**Benefits Achieved**:
- **Clear Developer Workflow**: Numbered sequence eliminates confusion
- **Phase Alignment**: Documentation structure matches development timeline
- **Scalable Pattern**: Template for future components and phases
- **Logical Progression**: Sequential flow from context to implementation

### **Documentation Structure Standards (Latest Evolution)**
**Date**: Current Session  
**Optimization**: Phase-based organization with numbered developer agent files

**Implementation**:
- **Phase Folders**: Restructured to match development timeline phases
  - `docs/Phase1/` - Foundation (basic video + pose detection)
  - `docs/Phase2/` - Core features (analysis + feedback)
  - `docs/Phase3/` - Learning infrastructure (training tools)
  - `docs/Phase4/` - Intelligence (smart learning)
  - `docs/Phase5/` - Polish (advanced features)
- **Numbered Component Files**: Sequential workflow for developer agents
  - `01_bootstrap_instructions.md` - Complete foundation (start here)
  - `02_context_validation_tests.md` - Verify understanding
  - `03_visual_architecture_diagrams.md` - Visual structure
  - `04_technical_specifications.md` - Implementation details

**Key Benefits**:
- **Clear Workflow**: Eliminates confusion about file sequence
- **Phase Alignment**: Documentation matches development timeline
- **Template Pattern**: Reusable structure for all future components
- **Developer Efficiency**: Logical progression from context to code

### **Standard Template for Future Components**:
```
docs/PhaseN/componentX_name/
├── 01_bootstrap_instructions.md      # Foundation knowledge
├── 02_context_validation_tests.md    # Understanding tests
├── 03_visual_architecture_diagrams.md # UML/Mermaid diagrams
└── 04_technical_specifications.md    # Implementation details
```

### **Testing and Coverage Methodology Implementation (Latest Session)**
**Date**: Current Session  
**Action**: Established comprehensive testing infrastructure with portable coverage configuration

**Key Infrastructure Components Added**:
- **`.coveragerc`**: Portable coverage configuration excluding demonstration code
- **`PYTEST_COMMANDS.md`**: Complete pytest reference documentation
- **`.gitignore` updates**: Proper coverage file exclusions
- **Test organization**: Numbered directory structure (10_project_components/, 20_infrastructure/, 30_integration/)

**Coverage Configuration Optimization**:
```ini
# .coveragerc - Excludes __main__ sections for realistic coverage targets
[run]
source = src
omit = */tests/*, */.venv/*

[report]  
exclude_lines = if __name__ == .__main__.:
show_missing = True

[html]
directory = htmlcov
```

**Testing Workflow Established**:
- **Quick Check**: `pytest tests/10_project_components/test_module.py -v`
- **Coverage Analysis**: `pytest --cov=src/module --cov-report=term-missing`
- **Deep Investigation**: `pytest --cov=src/module --cov-report=html`

**Coverage Standards**:
- **Functional Code**: 60-80% coverage targets
- **Demonstration Code**: Excluded from coverage (realistic for educational projects)
- **HTML Reports**: Line-by-line analysis in `htmlcov/index.html`

**Benefits Achieved**:
- **Portable Configuration**: Works across all machines and CI/CD systems
- **Team Consistency**: Same coverage rules for all developers
- **Development Feedback**: Instant coverage feedback during development
- **Documentation**: Complete pytest reference eliminates command lookup
- **Realistic Targets**: Focuses coverage on business logic, not demonstrations

**Template for Future Projects**:
1. Create `.coveragerc` with standard exclusions
2. Create `PYTEST_COMMANDS.md` with complete workflow reference
3. Update `.gitignore` for coverage files
4. Organize tests in numbered category directories
5. Establish development workflow (quick → coverage → deep analysis)

**This testing methodology represents proven efficiency gains and is now standard for all future projects.**

### **Ready for Component 1 Development**
**Status**: All optimizations complete, context management system operational
**Next Action**: Begin micro-incremental development with optimized context tracking
**Documentation**: Phase-based organization with numbered developer agent files"