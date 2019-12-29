"""Tests for models."""
from maho.models import Festivity, setup_tables


def test_setup_tables():
    """Test that the setup function runs correctly."""
    setup_tables()


def test_add_festivity(setup_db):
    """Test that adding a new festivity works."""
    festivity = Festivity.create(date="December 2", description="Test")
    assert festivity.date == "December 2"
    assert festivity.description == "Test"
