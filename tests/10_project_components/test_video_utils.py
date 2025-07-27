"""
Test suite for Video Input Module - pytest version

Educational Focus: Demonstrates clean, efficient testing patterns for computer vision
file operations. Tests cover file existence validation and video format validation
with comprehensive edge case handling.

Author: GuitarTrainer Development
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))
from video_input.video_utils import check_file_exists, validate_video_format, get_supported_video_formats


@pytest.fixture
def temp_files(tmp_path):
    """
    Create test files for validation testing.
    
    Returns:
        dict: Dictionary containing paths to test files
    """
    # Create test files
    valid_file = tmp_path / "test_video.mp4"
    empty_file = tmp_path / "empty_video.mp4"
    
    # Write content to valid file
    valid_file.write_text("fake video content for testing")
    
    # Create empty file
    empty_file.touch()
    
    return {
        'valid_file': valid_file,
        'empty_file': empty_file,
        'test_dir': tmp_path
    }


# === FILE EXISTENCE TESTS ===

def test_check_file_exists_valid(temp_files):
    """Test that check_file_exists returns True for valid files."""
    assert check_file_exists(temp_files['valid_file']) is True


def test_check_file_exists_nonexistent(temp_files):
    """Test that check_file_exists returns False for non-existent files."""
    nonexistent_file = temp_files['test_dir'] / "does_not_exist.mp4"
    assert check_file_exists(nonexistent_file) is False


def test_check_file_exists_empty(temp_files):
    """Test that check_file_exists returns False for empty files."""
    assert check_file_exists(temp_files['empty_file']) is False


def test_check_file_exists_directory(temp_files):
    """Test that check_file_exists returns False when given a directory."""
    assert check_file_exists(temp_files['test_dir']) is False


@pytest.mark.parametrize("test_path", [
    Path("x" * 500 + ".mp4"),              # Very long path
    Path("test with spaces & symbols!.mp4"), # Special characters
    Path(""),                               # Empty path
    Path("."),                              # Current directory
    Path("/non/existent/deeply/nested/path/video.mp4"),  # Deep non-existent path
    Path("🎸🎵.mp4"),                       # Unicode characters
])

def test_check_file_exists_edge_cases(test_path):
    """Test that check_file_exists handles edge cases without crashing."""
    result = check_file_exists(test_path)
    assert result is False


# === VIDEO FORMAT VALIDATION TESTS ===

def test_validate_video_format_supported():
    """Test that validate_video_format returns True for all supported formats."""
    supported_formats = get_supported_video_formats()
    
    # Test each supported format
    for format_ext in supported_formats:
        test_file = Path(f"test_video{format_ext}")
        assert validate_video_format(test_file) is True


@pytest.mark.parametrize("format_extension", [
    ".mp4", ".MP4", ".Mp4", ".mP4",  # Various case combinations
    ".avi", ".AVI", ".Avi",
    ".mov", ".MOV", ".Mov",
    ".mkv", ".MKV", ".Mkv",
])

def test_validate_video_format_case_insensitive(format_extension):
    """Test that format validation is case-insensitive."""
    supported_formats = get_supported_video_formats()
    
    # Only test if this extension (in lowercase) is actually supported
    if format_extension.lower() in supported_formats:
        test_file = Path(f"test_video{format_extension}")
        assert validate_video_format(test_file) is True


def test_validate_video_format_unsupported():
    """Test that validate_video_format returns False for unsupported formats."""
    supported_formats = get_supported_video_formats()
    
    # Test arbitrary extensions that should not be in supported list
    test_extensions = ['.txt', '.jpg', '.exe', '.pdf', '.zip', '.xyz', '.abc']
    
    for ext in test_extensions:
        if ext not in supported_formats:  # Only test if actually unsupported
            test_file = Path(f"test_file{ext}")
            assert validate_video_format(test_file) is False


@pytest.mark.parametrize("test_file", [
    Path("no_extension"),           # No extension
    Path("empty_extension."),       # Empty extension
    Path("multiple.mp4.old"),       # Multiple extensions
    Path(".hidden_no_name"),        # Hidden file with no name
    Path(""),                       # Empty path
])

def test_validate_video_format_edge_cases(test_file):
    """Test that validate_video_format handles edge cases without crashing."""
    result = validate_video_format(test_file)
    assert result is False


# To run these tests:
# 1. Install pytest: pip install pytest
# 2. Run from project root: pytest tests/10_project_components/test_video_utils.py -v
# 3. Run with coverage: pytest tests/10_project_components/test_video_utils.py --cov=src/video_input -v
