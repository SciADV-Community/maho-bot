"""Cog wrapper module for general utility commands."""
import random
from discord.ext import commands
from maho import utils


class Utils(commands.Cog):
    """Cog for the utility commandset."""

    def __init__(self, client):
        """Create the cog."""
        self.client = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def rate(self, context, *, arg):
        """Rate something."""
        i = 0
        for c in arg:
            i = i * 37 + ord(c)
        i %= 11

        await context.send(f"I'd give {arg} a {i}/10")

    @commands.command(pass_context=True)
    async def choose(self, context, *, arg):
        """Choose between comma-separated choices."""
        choices = arg.split(",")
        await context.send(
            f"I choose {choices[random.randint(0, len(choices) - 1)]}"  # nosec
        )


def setup(client):
    """Add the cog to the client."""
    client.add_cog(Utils(client))
