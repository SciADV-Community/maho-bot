"""Common fixtures."""
import pytest

from maho.models import DB, Festivity


@pytest.fixture(autouse=False)
def setup_db():
    """Set up the database."""
    DB.connect()
    DB.create_tables([Festivity])
    yield
    DB.close()
