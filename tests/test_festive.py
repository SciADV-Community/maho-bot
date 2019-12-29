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


def test_get_date():
    """Test that get_date works as it should."""
    assert festive.get_date("01/10").day == 1
    assert festive.get_date("01/10").month == 10
    assert festive.get_date("01/10").year == 2016
    assert festive.get_date("01/32") is None
    assert festive.get_date("random string") is None
    assert festive.get_date("31/02") is None
