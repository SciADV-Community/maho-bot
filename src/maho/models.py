"""Module to handle model operations."""
from peewee import Model, CharField, DateField, SqliteDatabase
from maho import config

DB = SqliteDatabase(config.DB)


class BaseModel(Model):
    """Abstract class to act as an ORM base."""

    class Meta:
        """Meta information for the class."""

        database = DB


class Festivity(BaseModel):
    """ORM model to represent a festivity."""

    date = DateField(unique=True, null=False)
    description = CharField(null=False)

    def __str__(self):
        """Get string representation of the object."""
        return f"{self.date.strftime('%B %d')}: {self.description}"


def setup_tables():
    """Set up the database."""
    DB.connect()
    DB.create_tables([Festivity])
    DB.close()
