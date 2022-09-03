"""Tests for the festive commandset."""
from datetime import datetime

from maho.cogs import festive
from maho.models import Festivity

import pytest


def test_get_festive_text(setup_db):
    """Test that the output is generated correctly."""
    template = "{0}\n\nTest 123"
    date = datetime.strptime("10/10", "%d/%m")
    Festivity.create(date=date, description="Test")

    assert festive.get_festive_out(template) == "October 10: Test\n\nTest 123"


@pytest.mark.asyncio
async def test_get_date():
    """Test that get_date works as it should."""
    converter = festive.DateTimeConverter()
    ctx = None

    date = await converter.convert(ctx, "01/10")
    assert date.day == 1
    assert date.month == 10
    assert date.year == 2016

    with pytest.raises(AttributeError):  # Will try to use discord APIs
        date = await converter.convert(ctx, "01/32")
        date = await converter.convert(ctx, "random string")
        date = await converter.convert(ctx, "31/02")
