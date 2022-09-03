"""Command Cog wrapper module for general maho commands."""
from pathlib import Path

import discord

from maho import config, utils


def load_static_text(filename: str) -> str:
    """Load static text from a file."""
    logger = utils.get_logger()
    try:
        with open(Path(__file__).parent / "static" / filename) as f:
            return f.read()
    except FileNotFoundError:
        logger.warning("File %s not found.", filename)
        return ""


class Maho(discord.Cog):  # pragma: no cover
    """Cog for general maho commands."""

    def __init__(self, client: discord.Bot):
        """Initialize the cog."""
        self.client: discord.Bot = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @discord.slash_command(description="Send out a lebby.")
    async def lebby(self, ctx: discord.ApplicationContext):
        await ctx.respond("( Í¡Â° ÍœÊ– Í¡Â°)")

    @discord.slash_command(description="Send out the chaos pomf copypasta.")
    async def chaos_pomf(self, ctx: discord.ApplicationContext):
        await ctx.respond(load_static_text("chaos_pomf.txt"))

    @discord.slash_command(description="Print out the rules.")
    async def rules(self, ctx: discord.ApplicationContext):
        await ctx.respond(load_static_text("rules.txt"))

    @discord.slash_command(description="Send out a lenny.")
    async def lenny(self, ctx: discord.ApplicationContext):
        await ctx.respond("( ͡° ͜ʖ ͡°)")

    @discord.slash_command(description="Send out an ice meme.")
    async def ice(self, ctx: discord.ApplicationContext):
        await ctx.respond(load_static_text("ice.txt"))

    @discord.slash_command(description="Send out a meta meme.")
    async def nudes(self, ctx: discord.ApplicationContext):
        await ctx.respond(load_static_text("nudes.txt"))

    @discord.slash_command(description="Send out this kaomoji.")
    async def stalker(self, ctx: discord.ApplicationContext):
        await ctx.respond("(´・ω・`)")

    @discord.slash_command(description="Send out the iconic phrase.")
    async def sonome(self, ctx: discord.ApplicationContext):
        await ctx.respond("その目、だれの目？")

    @discord.slash_command(description="Send out the IceBango copypasta.")
    async def ice_bango(self, ctx: discord.ApplicationContext):
        await ctx.respond(load_static_text("ice_bango.txt"))

    @discord.slash_command(description="Ping everyone.")
    async def ping_everyone(self, ctx: discord.ApplicationContext):
        if ctx.author.id in config.ADMINS:
            await ctx.respond("@everyone (´・ω・`)")


def setup(client):  # pragma: no cover
    """Add the cog to the client."""
    client.add_cog(Maho(client))
