"""
Pose Detection Module for GuitarTrainer

This module provides MediaPipe-based pose detection capabilities
specifically designed for guitar technique analysis.
"""

# Export main functions for Micro-Increments 1 and 2
from .mediapipe_detector import initialize_mediapipe_pose, process_single_frame

__all__ = ['initialize_mediapipe_pose', 'process_single_frame']
