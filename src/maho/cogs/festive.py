"""Cog wrapper module for the festive command."""
from datetime import datetime
from pathlib import Path

import discord
from discord.ext.commands import Converter
from peewee import DoesNotExist, IntegrityError

from maho import utils
from maho.checks import is_bot_admin
from maho.models import Festivity


def get_festive_out(template: str) -> str:
    """Get a full list of festivities."""
    festivities = Festivity.select().order_by(Festivity.date)
    festivity_list = "\n".join([str(festivity) for festivity in festivities])
    return template.format(festivity_list)


class DateTimeConverter(Converter):
    async def convert(
        self, ctx: discord.ApplicationContext, argument: str
    ) -> datetime | None:
        """Get a datetime objects from a DD/MM string."""
        try:
            date = datetime.strptime(argument, "%d/%m")
            return date.replace(year=2016)
        except ValueError:
            await ctx.interaction.response.send_message(
                f"Invalid date string {argument}. Is it in DD/MM?", ephemeral=True
            )
            return


class Festive(discord.Cog):  # pragma: no cover
    """Cog for the festive commandset."""

    def __init__(self, client):
        """Create the cog."""
        self.client = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @discord.slash_command(description="Print the full list of festivities.")
    async def festive(self, ctx: discord.ApplicationContext):
        template_file = Path(__file__).parent / "static" / "festive_template.txt"
        with open(template_file) as f:
            template = f.read()
        await ctx.respond(get_festive_out(template))

    @discord.slash_command(
        description="Add a new festivity if you're admin.", checks=[is_bot_admin]
    )
    async def add_festive(
        self,
        ctx: discord.ApplicationContext,
        date: discord.Option(
            DateTimeConverter, "Date of the festivity.", required=True
        ),
        *,
        festivity: discord.Option(str, "The festivity.", required=True),
    ):
        try:
            result = Festivity.create(date=date, description=festivity)
            await ctx.response.send_message(
                f"Festivity: `{result}` added.", ephemeral=True
            )
        except IntegrityError:
            await ctx.response.send_message(
                f"Festivity at {date} already exists.", ephemeral=True
            )

    @discord.slash_command(
        description="Edit a festivity if you're admin.", checks=[is_bot_admin]
    )
    async def edit_festive(
        self,
        ctx: discord.ApplicationContext,
        date: discord.Option(
            DateTimeConverter, "The date of the festivity in DD/MM.", required=True
        ),
        *,
        new_text: discord.Option(str, "The new text for the festivity.", required=True),
    ):
        try:
            festivity = Festivity.get(date=date)
            festivity.description = new_text
            festivity.save()
            await ctx.response.send_message(
                f"Festivity updated: `{festivity}`", ephemeral=True
            )
        except DoesNotExist:
            await ctx.response.send_message(
                f"Festivity at date: {date} not found.", ephemeral=True
            )


def setup(client):  # pragma: no cover
    """Add the cog to the client."""
    client.add_cog(Festive(client))
