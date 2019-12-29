"""Cog wrapper module for the festive command."""
from pathlib import Path
from datetime import datetime
from discord.ext import commands
from peewee import IntegrityError, DoesNotExist
from maho import config, utils
from maho.models import Festivity


def get_festive_out(template: str) -> str:
    """Get a full list of festivities."""
    festivities = Festivity.select()
    festivity_list = "\n".join([str(festivity) for festivity in festivities])
    return template.format(festivity_list)


def get_date(date_str: str):
    """Get a datetime objects from a DD/MM string."""
    try:
        return datetime.strptime(date_str, "%d/%m")
    except ValueError:
        return None


class Festive(commands.Cog):  # pragma: no cover
    """Cog for the festive commandset."""

    def __init__(self, client):
        """Create the cog."""
        self.client = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def festive(self, context):
        """Print the full list of festivities."""
        template_file = Path(__file__).parent / "static" / "festive_template.txt"
        with open(template_file) as f:
            template = f.read()
        await context.send(get_festive_out(template))

    @commands.command(pass_context=True)
    async def add_festive(self, context, date_str, *, festivity):
        """Add a new festivity if you're an admin."""
        if context.author.id not in config.ADMINS:
            await context.send("You are not authorized to add festivities.")
            return

        date = get_date(date_str)
        if not date:
            await context.send(f"Invalid date string {date_str}. Is it in DD/MM?")
            return

        try:
            result = Festivity.create(date=date, description=festivity)
            await context.send(f"Festivity: `{result}` added.")
        except IntegrityError:
            await context.send(f"Festivity at {date_str} already exists.")

    @commands.command(pass_context=True)
    async def edit_festive(self, context, date_str, *, new_text):
        """Edit a festivity."""
        if context.author.id not in config.ADMINS:
            await context.send("You are not authoirzed to edit festivities.")
            return

        date = get_date(date_str)
        if not date:
            await context.send(f"Invalid date string {date_str}. Is it in DD/MM?")
            return

        try:
            festivity = Festivity.get(date=date)
            festivity.description = new_text
            festivity.save()
            await context.send(f"Festivity updated: `{festivity}`")
        except DoesNotExist:
            await context.send(f"Festivity at date: {date_str} not found.")


def setup(client):  # pragma: no cover
    """Add the cog to the client."""
    client.add_cog(Festive(client))
