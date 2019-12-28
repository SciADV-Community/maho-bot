"""Tests for misc functionality."""
from maho.modules import maho
from maho.utils import get_logger


def test_logger():
    """Test that the logger can be accessed."""
    logger = get_logger()
    assert logger is not None
    logger.debug("Test was run successfully.")


def test_static_file():
    """Test behaviour when the file is found."""
    assert maho.load_static_text("test.txt") == "Test string."


def test_static_file_missing():
    """Test behaviour when a static file is missing."""
    assert maho.load_static_text("missing_file.txt") == ""
