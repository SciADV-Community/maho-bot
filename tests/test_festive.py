"""Tests for teh festive commandset."""
from datetime import datetime
from maho.models import Festivity
from maho.modules import festive


def test_get_festive_text(setup_db):
    """Test that the output is generated correctly."""
    template = "{0}\n\nTest 123"
    date = datetime.strptime("10/10", "%d/%m")
    Festivity.create(date=date, description="Test")

    assert festive.get_festive_out(template) == "October 10: Test\n\nTest 123"


def test_add_festivity_valid(setup_db):
    """Test that a new festivity can be successfully added from string parameters."""
    ret = festive.add_festivity("10/10", "Test Festivity")
    assert ret == "Festivity: `October 10: Test Festivity` added."
    assert Festivity.get(description="Test Festivity")


def test_add_festivity_invalid_integrity(setup_db):
    """Test that a new festivity can not be added for the same date as another one."""
    festive.add_festivity("10/10", "Test Festivity")
    ret = festive.add_festivity("10/10", "Test Festivity 2")
    assert ret == "Festivity at 10/10 already exists."


def test_add_festivity_invalid_date_syntax(setup_db):
    """Test that a new festivity can not be added if the format is invalid."""
    ret = festive.add_festivity("October 10", "Test Festivity")
    assert ret.startswith("Invalid date: October 10")


def test_add_festivity_invalid_date_logic(setup_db):
    """Test that a new festivity can't be added on an invalid date."""
    ret = festive.add_festivity("31/02", "Test Festivity")
    assert ret.startswith("Invalid date: 31/02")


def test_fail(setup_db):
    assert False
