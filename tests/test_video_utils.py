"""
Test suite for Video Input Module - pytest version

Educational Focus: Demonstrates modern testing patterns for computer vision
file operations using pytest's clean syntax and fixtures.

Author: GuitarTrainer Development
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from video_input.video_utils import check_file_exists


@pytest.fixture
def test_files(tmp_path):
    """
    Create test files for validation testing.
    
    Educational Note: pytest fixtures provide a clean way to set up
    test data. The tmp_path fixture automatically creates a temporary
    directory that's cleaned up after tests complete.
    
    Args:
        tmp_path: pytest built-in fixture providing temporary directory
        
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


def test_valid_file_exists(test_files):
    """
    Test that check_file_exists returns True for valid files.
    
    Educational Note: pytest uses simple assert statements instead of
    unittest's assertEqual methods. This makes tests more readable
    and provides better error messages.
    """
    result = check_file_exists(test_files['valid_file'])
    assert result is True, "Should return True for existing file with content"


def test_nonexistent_file(test_files):
    """
    Test that check_file_exists returns False for non-existent files.
    
    Educational Note: Testing the most common user error - providing
    a path that doesn't exist. pytest's assert provides clear output
    when this test fails.
    """
    nonexistent_file = test_files['test_dir'] / "does_not_exist.mp4"
    result = check_file_exists(nonexistent_file)
    assert result is False, "Should return False for non-existent file"


def test_empty_file(test_files):
    """
    Test that check_file_exists returns False for empty files.
    
    Educational Note: Empty files should be rejected for video processing.
    pytest makes this test case very clear and concise.
    """
    result = check_file_exists(test_files['empty_file'])
    assert result is False, "Should return False for empty file"


def test_directory_instead_of_file(test_files):
    """
    Test that check_file_exists returns False when given a directory.
    
    Educational Note: Users might accidentally select a directory.
    Our function should handle this gracefully.
    """
    result = check_file_exists(test_files['test_dir'])
    assert result is False, "Should return False for directory path"


def test_path_object_handling(test_files):
    """
    Test that function properly handles pathlib.Path objects.
    
    Educational Note: Modern Python uses pathlib.Path objects.
    This test ensures our function works with both Path objects
    and string paths converted to Path objects.
    """
    # Test with Path object
    result = check_file_exists(test_files['valid_file'])
    assert result is True, "Should handle pathlib.Path objects"
    
    # Test with string path converted to Path
    string_path = str(test_files['valid_file'])
    path_object = Path(string_path)
    result = check_file_exists(path_object)
    assert result is True, "Should handle converted Path objects"


@pytest.mark.parametrize("invalid_path", [
    Path("x" * 500 + ".mp4"),  # Very long path
    Path("test with spaces & symbols!.mp4"),  # Special characters
    Path(""),  # Empty path
    Path("."),  # Current directory
])
def test_edge_cases(invalid_path):
    """
    Test that function handles edge cases without crashing.
    
    Educational Note: pytest.mark.parametrize allows testing multiple
    inputs with a single test function. This is much cleaner than
    writing separate test methods for each edge case.
    
    Args:
        invalid_path: Various problematic path inputs to test
    """
    result = check_file_exists(invalid_path)
    assert result is False, f"Should handle edge case gracefully: {invalid_path}"


def test_function_robustness():
    """
    Test that function doesn't crash on extreme edge cases.
    
    Educational Note: Robust functions should handle unexpected
    input gracefully. pytest makes it easy to test these scenarios.
    """
    # Test various edge cases that might cause crashes
    test_cases = [
        Path("/non/existent/deeply/nested/path/video.mp4"),
        Path("C:\\Windows\\System32\\kernel32.dll"),  # System file (if on Windows)
        Path("🎸🎵.mp4"),  # Unicode characters
    ]
    
    for test_path in test_cases:
        result = check_file_exists(test_path)
        # Should not crash, regardless of result
        assert isinstance(result, bool), f"Should return boolean for: {test_path}"


# Educational Note: pytest automatically discovers and runs all functions
# starting with 'test_'. No need for unittest.main() or test class setup.

# To run these tests:
# 1. Install pytest: pip install pytest
# 2. Run from project root: pytest tests/test_video_utils.py -v
# 3. Run with coverage: pytest tests/test_video_utils.py --cov=src/video_input -v
