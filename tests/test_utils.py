"""Tests for the utility commands."""
from maho.modules import utils


def test_get_hash():
    """Test that the BLAKE2 hash is retrieved properly."""
    assert utils.get_b2_hash("test") == "44a8995dd50b6657a037a7839304535b"


def test_give_rating():
    """Test that ratings are given out consistently."""
    assert utils.give_rating("Test") == 7
    assert utils.give_rating("Test2") != 7


def test_get_choice():
    """Test that choices are made consistently."""
    assert utils.get_choice(["To test", "Not to test"]) == "To test"
