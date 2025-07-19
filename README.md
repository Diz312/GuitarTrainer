# GuitarTrainer - Computer Vision Guitar Technique Analysis

A desktop application that uses computer vision and machine learning to analyze guitar playing technique and provide biomechanical feedback for improvement.

## Overview

GuitarTrainer analyzes video clips of guitar playing to track body positioning and movement patterns, identifying technique issues in real-time. The application learns from examples of good and poor technique to provide personalized feedback.

## Key Features

### Core Analysis
- **Shoulder Alignment**: Detects slouching or asymmetric positioning
- **Right Wrist Position**: Monitors wrist angle and stability during picking
- **Right Hand Movement**: Tracks picking motion and hand positioning
- **Left Hand Fingers**: Individual finger placement and positioning analysis

### Learning Capabilities
- **Manual Training**: Upload and label video examples of good/bad technique
- **Continuous Learning**: Automatically improves analysis through user feedback
- **Model Versioning**: Track performance improvements over time
- **Progress Tracking**: Monitor technique improvement across sessions

### User Interface
- **Video Upload**: Drag-and-drop video clip analysis
- **Visual Feedback**: Pose overlay visualization on video frames
- **Scoring System**: Numerical scores (0-100) for each body part
- **Recommendations**: Actionable text feedback for improvement

## Technical Architecture

### System Components

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
                                │                       │
                                ▼                       ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │Model Retraining &│    │Training Data    │
                       │   Versioning     │◄───│  Repository     │
                       └──────────────────┘    └─────────────────┘
```

### Technology Stack

- **Core**: Python 3.9+
- **Computer Vision**: OpenCV 4.8+, MediaPipe 0.10+
- **Machine Learning**: scikit-learn, TensorFlow Lite
- **GUI**: PyQt6 (primary choice)
- **Database**: SQLite for training data
- **Visualization**: Matplotlib for analysis charts

## Project Structure

```
GuitarTrainer/
├── src/
│   ├── video_input/          # Video file handling and preprocessing
│   ├── pose_detection/       # MediaPipe pose estimation pipeline
│   ├── analysis/            # Biomechanical analysis algorithms
│   ├── training/            # Model training and data management
│   ├── feedback/            # Scoring and recommendation generation
│   ├── gui/                 # User interface components
│   └── continuous_learning/ # Automated learning pipeline
├── data/
│   ├── models/              # Trained models and versions
│   ├── training_videos/     # Labeled training examples
│   └── configs/             # Application configuration files
├── tests/                   # Unit and integration tests
├── docs/                    # Documentation and guides
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Webcam or video files for analysis
- 4GB+ RAM recommended
- Windows/macOS/Linux desktop environment

### Dependencies
```bash
pip install -r requirements.txt
```

Key packages:
- opencv-python>=4.8.0
- mediapipe>=0.10.0
- scikit-learn>=1.3.0
- PyQt6>=6.5.0
- numpy>=1.24.0
- matplotlib>=3.7.0

## Usage

### Basic Analysis
1. **Launch Application**: Run `python src/main.py`
2. **Upload Video**: Drag-drop or browse for guitar playing video (MP4, AVI, MOV)
3. **View Results**: See pose overlay, scores, and recommendations
4. **Save Session**: Export results for progress tracking

### Training Mode
1. **Upload Examples**: Add videos of good/poor technique
2. **Label Data**: Mark clips as "good" or "needs improvement"
3. **Train Model**: Automatic retraining triggers after sufficient data
4. **Validate**: Review model performance improvements

### Continuous Learning
- **Auto-Learning**: App learns from your corrections over time
- **Progress Tracking**: Monitor improvement across sessions
- **Model Updates**: Automatic model improvements with user feedback

## Biomechanical Metrics

### Shoulder Alignment
- **Metric**: Angle deviation from horizontal line
- **Good Range**: ±5 degrees from level
- **Common Issues**: Forward head posture, uneven shoulders

### Right Wrist Position
- **Metric**: Wrist angle relative to neutral position
- **Good Range**: 10-20 degrees extension
- **Common Issues**: Over-extension, ulnar deviation

### Right Hand Movement
- **Metric**: Movement stability and picking arc consistency
- **Good Range**: Smooth, consistent motion patterns
- **Common Issues**: Excessive tension, irregular picking motion

### Left Hand Fingers
- **Metric**: Individual finger curvature and positioning
- **Good Range**: Curved fingers, perpendicular to fretboard
- **Common Issues**: Flat fingers, thumb placement

## Development Phases

### Phase 1: Foundation (Weeks 1-2)
- ✅ Project structure setup
- ⏳ Basic video input and pose detection
- ⏳ Simple GUI framework

### Phase 2: Basic Analysis (Weeks 3-4)
- ⏳ Rule-based analysis engine
- ⏳ Basic feedback generation
- ⏳ Initial training data collection

### Phase 3: Training Infrastructure (Weeks 5-6)
- ⏳ Training data repository
- ⏳ Manual annotation interface
- ⏳ Model training pipeline

### Phase 4: Continuous Learning (Weeks 7-8)
- ⏳ Upload & label interface
- ⏳ Automated retraining
- ⏳ Model versioning system

### Phase 5: Advanced Features (Weeks 9-10)
- ⏳ Performance tracking dashboard
- ⏳ Smart retraining triggers
- ⏳ Model comparison tools

## Performance Requirements

- **Processing Speed**: 30-second clips in <60 seconds
- **Memory Usage**: <2GB for typical videos
- **Video Support**: Up to 1080p resolution
- **Accuracy Target**: >85% pose detection confidence

## Contributing

This is a personal learning project focused on computer vision education. The codebase prioritizes readability and educational value over optimization.

### Code Style
- Clear variable names and extensive comments
- Modular design for easy understanding
- Educational documentation in key algorithms

## License

Personal use project - not intended for commercial distribution.

## Roadmap

- [ ] Real-time webcam analysis
- [ ] Multiple camera angle support
- [ ] Advanced biomechanical models
- [ ] Integration with guitar learning apps
- [ ] Community sharing of technique improvements

## Contact & Support

This is a learning project. For questions or collaboration on computer vision techniques, please refer to the documentation in the `docs/` folder.

---

**Note**: This application is designed for educational purposes to learn computer vision programming. It is not a substitute for professional guitar instruction.