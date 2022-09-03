"""Cog wrapper module for general utility commands."""
import random
from hashlib import blake2b

import discord

from maho import utils


def get_b2_hash(text: str) -> str:
    """Get a string of the BLAKE2 hash of a string."""
    return blake2b(bytes(text, "utf8"), digest_size=16).hexdigest()


def give_rating(text: str) -> int:
    """Give a random rating on the input text."""
    random.seed(get_b2_hash(text))
    return random.randint(0, 10)


def get_choice(choices: list[str]) -> str:
    """Get a random choice between choices."""
    random.seed(get_b2_hash("".join(sorted(choices))))
    return random.choice(choices).strip()


class Utils(discord.Cog):  # pragma: no cover
    """Cog for the utility commandset."""

    def __init__(self, client: discord.Bot):
        """Create the cog."""
        self.client: discord.Bot = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @discord.slash_command(description="Rate something.")
    async def rate(
        self,
        ctx: discord.ApplicationContext,
        *,
        arg: discord.Option(str, "Thing to rate.", required=True),
    ):
        await ctx.response.send_message(f"I'd give {arg} a {give_rating(arg)}/10")

    @discord.slash_command(description="Choose between comma separated choices.")
    async def choose(
        self,
        ctx: discord.ApplicationContext,
        *,
        arg: discord.Option(str, "Comma separated choices.", required=True),
    ):
        choices = arg.split(",")
        await ctx.response.send_message(f"I choose {get_choice(choices)}")


def setup(client):  # pragma: no cover
    """Add the cog to the client."""
    client.add_cog(Utils(client))
