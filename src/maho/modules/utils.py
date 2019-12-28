"""Cog wrapper module for general utility commands."""
import random
import hashlib
from discord.ext import commands
from maho import utils


def get_md5_hash(text: str) -> str:
    """Get a string of the md5 hash of a string."""
    return hashlib.md5(bytes(text, "utf8")).hexdigest()


def give_rating(text: str) -> int:
    """Give a random rating on the input text."""
    random.seed(get_md5_hash(text))
    return random.randint(0, 10)


def get_choice(choices) -> str:
    """Get a random choice between choices."""
    random.seed(get_md5_hash("".join(sorted(choices))))
    return choices[random.randint(0, len(choices) - 1)]


class Utils(commands.Cog):  # pragma: no cover
    """Cog for the utility commandset."""

    def __init__(self, client):
        """Create the cog."""
        self.client = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def rate(self, context, *, arg):
        """Rate something."""
        await context.send(f"I'd give {arg} a {give_rating(arg)}/10")

    @commands.command(pass_context=True)
    async def choose(self, context, *, arg):
        """Choose between comma-separated choices."""
        choices = arg.split(",")
        await context.send(f"I choose {get_choice(choices)}")


def setup(client):  # pragma: no cover
    """Add the cog to the client."""
    client.add_cog(Utils(client))
