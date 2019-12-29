"""Cog wrapper module for the festive command."""
from pathlib import Path
from datetime import datetime
from discord.ext import commands
from peewee import IntegrityError
from maho import config, utils
from maho.models import Festivity


def get_festive_out(template: str) -> str:
    """Get a full list of festivities."""
    festivities = Festivity.select()
    festivity_list = "\n".join(
        [
            f"{festivity.date.strftime('%B %d')}: {festivity.description}"
            for festivity in festivities
        ]
    )
    return template.format(festivity_list)


def add_festivity(date_str: str, description: str) -> str:
    """Add a new festivity to the database."""
    logger = utils.get_logger()
    try:
        date = datetime.strptime(date_str, "%d/%m")
        Festivity.create(date=date, description=description)
        return f"Festivity: `{date.strftime('%B %d')}: {description}` added."
    except ValueError:
        logger.info("Invalid date was entered %s", date_str)
        return f"Invalid date: {date_str}, is it in the DD/MM format?"
    except IntegrityError:
        return f"Festivity at {date_str} already exists."


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
    async def add_festive(self, context, date, festivity):
        """Add a new festivity if you're an admin."""
        if context.author.id in config.ADMINS:
            await context.send(add_festivity(date, festivity))
        else:
            await context.send(
                "You are not authorized to add festivities. "
                + "Contact a bot administrator."
            )
            self.logger.info(
                "Unauthorized User %s tried to add festivity %s at date %s.",
                context.author,
                festivity,
                date,
            )


def setup(client):  # pragma: no cover
    """Add the cog to the client."""
    client.add_cog(Festive(client))
