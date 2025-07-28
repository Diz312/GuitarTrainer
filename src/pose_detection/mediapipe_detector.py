"""
MediaPipe Pose Detection Integration Module

This module provides the main interface for MediaPipe pose detection,
focusing on guitar technique analysis applications.

Educational Focus: This module demonstrates MediaPipe pose detection
integration patterns and confidence-based filtering strategies.
"""

import sys
from pathlib import Path
import time
from typing import Dict, Any, Optional
# Add OpenCV import for frame processing
import cv2
import numpy as np

# Add project root to Python path for proper imports
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

try:
    from config import get_project_config
    from src.utils.logger_factory import get_component_logger
    logger = get_component_logger('pose_detection')
    config = get_project_config()
except ImportError:
    # Graceful fallback for standalone usage
    import logging
    logger = logging.getLogger(__name__)
    config = None


def initialize_mediapipe_pose():
    """
    Initialize MediaPipe pose detection model.
    
    Educational Note: MediaPipe uses pre-trained models that require
    specific initialization parameters for optimal performance. The model
    complexity parameter balances accuracy vs speed:
    - 0: Lite model (fastest, lowest accuracy)
    - 1: Full model (balanced performance) 
    - 2: Heavy model (slowest, highest accuracy)
    
    Computer Vision Context: Pose estimation models use deep learning
    architectures trained on large datasets of human poses. MediaPipe's
    models are optimized for real-time inference on various hardware.
    
    Guitar Analysis Application: We use model complexity 1 for balanced
    performance suitable for analyzing guitar playing technique without
    requiring high-end hardware.
    
    Returns:
        MediaPipe pose detection model instance
        
    Raises:
        ImportError: If MediaPipe not available
        RuntimeError: If model initialization fails
    """

    logger.debug("Starting MediaPipe pose model initialization")
    
    try:
        logger.debug("Importing MediaPipe library")
        import mediapipe as mp
        
        # Get MediaPipe pose solution
        mp_pose = mp.solutions.pose
        logger.debug("MediaPipe pose solution loaded successfully")
        
        # Get configuration for MediaPipe parameters
        if config:
            pose_config = config.pose_detection.core
            logger.debug(f"Using config: complexity={pose_config.model_complexity}, detection_conf={pose_config.min_detection_confidence}")
        else:
            logger.warning("Config not available, using fallback values")
            # Fallback configuration
            pose_config = type('obj', (object,), {
                'static_image_mode': False,
                'model_complexity': 1,
                'min_detection_confidence': 0.6,
                'min_tracking_confidence': 0.5
            })()
        
        # Initialize pose model with configuration
        # Educational Note: These parameters control detection behavior
        pose_model = mp_pose.Pose(
            static_image_mode=pose_config.static_image_mode,
            model_complexity=pose_config.model_complexity,
            min_detection_confidence=pose_config.min_detection_confidence,
            min_tracking_confidence=pose_config.min_tracking_confidence
        )
        
        logger.info("MediaPipe pose model initialized successfully with complexity=1")
        return pose_model
        
    except ImportError as e:
        error_msg = f"MediaPipe not available: {e}"
        logger.error(error_msg)
        raise ImportError(error_msg)
    except Exception as e:
        error_msg = f"Failed to initialize MediaPipe pose model: {e}"
        logger.error(error_msg)
        raise RuntimeError(error_msg)


def process_single_frame(pose_model, frame):
    """
    Process single frame through MediaPipe pose detection.
    
    Educational Note: MediaPipe expects RGB format, while OpenCV uses BGR.
    This conversion is critical for accurate detection. The color format
    mismatch can cause poor or failed pose detection if not handled properly.
    
    Computer Vision Context: Different computer vision libraries use different
    color channel orderings. OpenCV uses BGR (Blue-Green-Red) for historical
    reasons, while most other libraries including MediaPipe use RGB (Red-Green-Blue).
    
    Guitar Analysis Application: Accurate color format ensures reliable
    pose detection for guitar playing analysis, preventing false negatives
    due to incorrect color interpretation.
    
    Args:
        pose_model: Initialized MediaPipe pose detection model
        frame: Input frame in BGR format (numpy.ndarray from OpenCV/VideoLoader)
        
    Returns:
        MediaPipe pose detection results object containing landmarks
        
    Raises:
        ValueError: If frame format is invalid
        RuntimeError: If MediaPipe processing fails
    """

    logger.debug(f"Starting frame processing: shape={frame.shape if frame is not None else 'None'}")
    
    try:
        # Validate input frame
        if frame is None:
            error_msg = "Input frame cannot be None"
            logger.error(error_msg)
            raise ValueError(error_msg)
        if not isinstance(frame, np.ndarray):
            error_msg = "Input frame must be numpy.ndarray"
            logger.error(error_msg)
            raise ValueError(error_msg)
        if len(frame.shape) != 3 or frame.shape[2] != 3:
            error_msg = "Input frame must be 3-channel (height, width, 3)"
            logger.error(error_msg)
            raise ValueError(error_msg)
            
        logger.debug("Frame validation passed")
        
        # Convert BGR to RGB (critical for MediaPipe)
        # Educational Note: cv2.COLOR_BGR2RGB swaps the red and blue channels
        logger.debug("Converting frame from BGR to RGB format")
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process through MediaPipe
        # Educational Note: MediaPipe process() method runs the pose detection
        # inference on the input frame and returns structured results
        logger.debug("Processing frame through MediaPipe pose detection")
        start_time = time.time()
        results = pose_model.process(rgb_frame)
        processing_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        # Log results
        if results.pose_landmarks:
            landmark_count = len(results.pose_landmarks.landmark)
            logger.info(f"Pose detection successful: {landmark_count} landmarks detected in {processing_time:.1f}ms")
        else:
            logger.warning(f"No pose detected in frame (processing time: {processing_time:.1f}ms)")
        
        logger.debug(f"Frame processing completed in {processing_time:.1f}ms")
        return results
        
    except Exception as e:
        error_msg = f"MediaPipe frame processing failed: {e}"
        logger.error(error_msg)
        raise RuntimeError(error_msg)


if __name__ == "__main__":
    """
    Manual testing and demonstration of MediaPipe initialization.
    CRITICAL: Use dynamic printing, never hardcode values.
    """
    print("🎯 MEDIAPIPE INITIALIZATION DEMONSTRATION")
    print("=" * 50)
    
    def demonstrate_mediapipe_initialization():
        """Show MediaPipe pose model initialization capabilities"""
        try:
            print("⚡ Initializing MediaPipe pose detection model...")
            
            # Test model initialization
            pose_model = initialize_mediapipe_pose()
            
            # Dynamic demonstration of model properties
            print("✅ MediaPipe pose model initialized successfully")
            print(f"📊 Model type: {type(pose_model).__name__}")
            
            # Check if model has expected attributes dynamically
            model_attributes = [attr for attr in dir(pose_model) if not attr.startswith('_')]
            print(f"🔧 Available model methods: {len(model_attributes)}")
            
            # Show key configuration attributes if available
            if hasattr(pose_model, '_min_detection_confidence'):
                print(f"🎯 Detection confidence: {pose_model._min_detection_confidence}")
            if hasattr(pose_model, '_min_tracking_confidence'):
                print(f"📈 Tracking confidence: {pose_model._min_tracking_confidence}")
            if hasattr(pose_model, '_model_complexity'):
                print(f"⚙️ Model complexity: {pose_model._model_complexity}")
                
            print("🎸 Model ready for guitar technique pose detection")
            
            # Clean up resources
            pose_model.close()
            print("🧹 Model resources cleaned up")
            
        except ImportError as e:
            print(f"❌ Import Error: {e}")
            print("💡 Please ensure MediaPipe is installed: pip install mediapipe")
        except RuntimeError as e:
            print(f"❌ Runtime Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
    
    def demonstrate_frame_processing():
        """Show single frame processing with VideoLoader integration"""
        try:
            from src.video_input.video_loader import VideoLoader
            
            # Load test video using Component 1
            loader = VideoLoader()
            test_video = Path("tests/fixtures/First_video.mp4")
            
            if test_video.exists() and loader.load_video(test_video):
                print("\n⚡ Testing single frame processing...")
                
                # Get single frame for demonstration
                frame = loader.get_next_frame()
                if frame is not None:
                    print(f"✅ Frame loaded: {frame.shape} (height, width, channels)")
                    
                    # Initialize pose model
                    pose_model = initialize_mediapipe_pose()
                    print(f"✅ Pose model ready for processing")
                    
                    # Process single frame
                    print("\n📊 Processing frame through MediaPipe...")
                    results = process_single_frame(pose_model, frame)
                    
                    # Dynamic display of results
                    if results.pose_landmarks:
                        landmark_count = len(results.pose_landmarks.landmark)
                        print(f"✅ Pose detection successful: {landmark_count} landmarks detected")
                        
                        # Show sample landmark data dynamically
                        if landmark_count > 0:
                            sample_landmark = results.pose_landmarks.landmark[0]
                            print(f"📍 Sample landmark: x={sample_landmark.x:.3f}, y={sample_landmark.y:.3f}, confidence={sample_landmark.visibility:.3f}")
                    else:
                        print("⚠️ No pose detected in frame")
                        
                    # Clean up
                    pose_model.close()
                    loader.close_video()
                    print("🧹 Resources cleaned up")
                    
                else:
                    print("❌ No frame available from VideoLoader")
            else:
                print("❌ Test video not found or failed to load")
                print("📝 Note: Ensure test_video.mp4 exists in tests/fixtures/")
                
        except ImportError as e:
            print(f"❌ Import Error: {e}")
            print("📝 Note: This requires Component 1 (VideoLoader) to be available")
        except Exception as e:
            print(f"❌ Processing Error: {e}")
    
    print("🎯 POSE DETECTION DEMONSTRATION")
    print("=" * 50)
    demonstrate_mediapipe_initialization()
    demonstrate_frame_processing()
