"""Tests for the utility commands."""
from maho.modules import utils


def test_get_hash():
    """Test that the md5 hash is retrieved properly."""
    assert utils.get_md5_hash("test") == "098f6bcd4621d373cade4e832627b4f6"


def test_give_rating():
    """Test that ratings are given out consistently."""
    assert utils.give_rating("Test") == 10
    assert utils.give_rating("Test2") != 10


def test_get_choice():
    """Test that choices are made consistently."""
    assert utils.get_choice(["To test", "Not to test"]) == "To test"
