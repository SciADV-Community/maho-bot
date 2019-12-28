"""Cog wrapper module for the festive command."""
from pathlib import Path
from discord.ext import commands
from maho import config, utils, models


class Festive(commands.Cog):
    """Cog for the festive commandset."""

    def __init__(self, client):
        """Create the cog."""
        self.client = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def festive(self, context):
        """Print the full list of festivities."""
        festivities = models.get_festivities()
        template_file = Path(__file__).parent / "static" / "festive_template.txt"
        with open(template_file) as f:
            template = f.read()

        msg = "\n".join([festivity for festivity in festivities])

        await context.send(template.format(msg))

    @commands.command(pass_context=True)
    async def add_festive(self, context, date, festivity):
        """Add a new festivity if you're an admin."""
        if context.author.id in config.ADMINS:
            try:
                dates = date.split()
                if dates[0].lower():
                    await context.send("Invalid month")
                elif int(dates[1]) > 31 or int(dates[1]) < 1:
                    await context.send("Invalid day")
                else:
                    models.add_festivity(date, festivity)
                    await context.send("Added festivity")
            except Exception:
                self.logger.warning(
                    "User %s failed in adding festivity %s at date %s",
                    context.author,
                    festivity,
                    date,
                )
                await context.send(
                    "Error occured when adding festivity, invalid first "
                    + "argument likely, reminder to wrap them in quotations!"
                )


def setup(client):
    """Add the cog to the client."""
    client.add_cog(Festive(client))
