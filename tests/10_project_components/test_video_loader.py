"""
Test suite for VideoLoader class.

Focuses on core functionality using real video files with minimal strategic mocking
for error conditions that cannot be tested with real files.
"""

import pytest
import cv2
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch
import sys

# Add project root to Python path for proper imports
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Import the class under test
from src.video_input.video_loader import VideoLoader


@pytest.fixture
def test_video_files():
    """
    Provide paths to test video files in fixtures directory.
    
    Returns:
        dict: Dictionary with test video file paths for different test scenarios
    """
    fixtures_dir = Path(__file__).parent.parent / "fixtures"
    
    # Define available test files - easy to extend in future
    available_files = {
        'valid_video': fixtures_dir / "test_video.mp4",
        # Future test files can be added here:
        # 'high_res_video': fixtures_dir / "high_res_test.mp4",
        # 'different_format': fixtures_dir / "test_video.avi",
        # 'short_video': fixtures_dir / "short_test.mp4",
    }
    
    # Verify files exist before returning
    existing_files = {}
    for name, path in available_files.items():
        if path.exists():
            existing_files[name] = path
        else:
            pytest.skip(f"Test video file not found: {path}")
    
    return existing_files


class TestVideoLoader:
    """Test VideoLoader core functionality with real files and strategic mocks."""
    
    def test_initialization(self):
        """Test VideoLoader initializes correctly."""
        loader = VideoLoader()
        
        # Check initial state
        assert loader.current_video is None
        assert loader.current_file_path is None
        assert loader.video_info == {}
        assert not loader.is_video_loaded()
        
        # Check infrastructure is available
        assert loader.logger is not None
        assert hasattr(loader, 'config')
    
    def test_load_nonexistent_file(self):
        """Test loading non-existent file fails gracefully."""
        loader = VideoLoader()
        
        result = loader.load_video(Path("nonexistent_video.mp4"))
        
        assert result is False
        assert not loader.is_video_loaded()
        assert loader.get_video_info() == {}
    
    def test_load_invalid_format(self, tmp_path):
        """Test loading unsupported format fails gracefully."""
        loader = VideoLoader()
        
        # Create a temporary text file
        test_file = tmp_path / "test.txt"
        test_file.write_text("not a video file")
        
        result = loader.load_video(test_file)
        
        assert result is False
        assert not loader.is_video_loaded()
        assert loader.get_video_info() == {}
    
    def test_load_directory_fails(self, tmp_path):
        """Test that loading a directory fails gracefully."""
        loader = VideoLoader()
        
        result = loader.load_video(tmp_path)  # tmp_path is a directory
        
        assert result is False
        assert not loader.is_video_loaded()
        assert loader.get_video_info() == {}
    
    def test_load_real_video_success(self, test_video_files):
        """Test successful video loading with real video file."""
        loader = VideoLoader()
        video_path = test_video_files['valid_video']
        
        result = loader.load_video(video_path)
        
        assert result is True
        assert loader.is_video_loaded()
        assert loader.current_file_path == video_path
        
        # Check video info contains all required fields
        info = loader.get_video_info()
        required_keys = ['fps', 'frame_count', 'width', 'height', 'duration_seconds', 'resolution', 'file_path']
        for key in required_keys:
            assert key in info
        
        # Verify properties are reasonable
        assert info['fps'] > 0
        assert info['frame_count'] > 0
        assert info['width'] > 0
        assert info['height'] > 0
        assert info['duration_seconds'] > 0
        assert 'x' in info['resolution']  # Format: "WIDTHxHEIGHT"
        assert str(video_path) in info['file_path']
        
        loader.close_video()
    
    def test_multiple_video_loading(self, test_video_files):
        """Test loading same video multiple times (resource reuse)."""
        loader = VideoLoader()
        video_path = test_video_files['valid_video']
        
        # Load first time
        result1 = loader.load_video(video_path)
        assert result1 is True
        first_info = loader.get_video_info()
        
        # Load same video again (should close and reload)
        result2 = loader.load_video(video_path)
        assert result2 is True
        second_info = loader.get_video_info()
        
        # Info should be identical
        assert first_info == second_info
        assert loader.current_file_path == video_path
        
        loader.close_video()
    
    def test_video_info_immutability(self, test_video_files):
        """Test that video info cannot be modified externally."""
        loader = VideoLoader()
        video_path = test_video_files['valid_video']
        
        loader.load_video(video_path)
        
        # Get video info and try to modify it
        info = loader.get_video_info()
        original_fps = info['fps']
        info['fps'] = 999
        info['new_key'] = 'malicious_value'
        
        # Get info again - should be unchanged
        fresh_info = loader.get_video_info()
        assert fresh_info['fps'] == original_fps
        assert 'new_key' not in fresh_info
        
        loader.close_video()
    
    def test_close_video_functionality(self, test_video_files):
        """Test video closing and resource cleanup with real file."""
        loader = VideoLoader()
        video_path = test_video_files['valid_video']
        
        # Load real video
        loader.load_video(video_path)
        assert loader.is_video_loaded()
        assert len(loader.get_video_info()) > 0
        
        # Close video
        loader.close_video()
        
        # Verify cleanup
        assert loader.current_video is None
        assert loader.current_file_path is None
        assert loader.video_info == {}
        assert not loader.is_video_loaded()
        assert loader.get_video_info() == {}
    
    def test_complete_workflow(self, test_video_files):
        """Test complete workflow from load to cleanup."""
        loader = VideoLoader()
        video_path = test_video_files['valid_video']
        
        # Step 1: Initial state
        assert not loader.is_video_loaded()
        assert loader.get_video_info() == {}
        
        # Step 2: Load video
        result = loader.load_video(video_path)
        assert result is True
        assert loader.is_video_loaded()
        
        # Step 3: Verify video properties
        info = loader.get_video_info()
        assert len(info) == 7  # All expected keys
        
        # Step 4: Clean shutdown
        loader.close_video()
        assert not loader.is_video_loaded()
        assert loader.get_video_info() == {}
    
 