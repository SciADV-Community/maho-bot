"""Command Cog wrapper module for general maho commands."""
from pathlib import Path
from discord.ext import commands
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


class Maho(commands.Cog):
    """Cog for general maho commands."""

    def __init__(self, client):
        """Initialize the cog."""
        self.client = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def lebby(self, context):
        """Send out a lebby."""
        await context.send("( Í¡Â° ÍœÊ– Í¡Â°)")

    @commands.command(pass_context=True)
    async def ChaosPomf(self, context):
        """Send out the chaos pomf copypasta."""
        await context.send(load_static_text("chaos_pomf.txt"))

    @commands.command(pass_context=True)
    async def rules(self, context):
        """Print out the rules."""
        await context.send(load_static_text("rules.txt"))

    @commands.command(pass_context=True)
    async def lenny(self, context):
        """Send out a lenny."""
        await context.send("( ͡° ͜ʖ ͡°)")

    @commands.command(pass_context=True)
    async def ice(self, context):
        """Send out an ice meme."""
        await context.send(load_static_text("ice.txt"))

    @commands.command(pass_context=True)
    async def nudes(self, context):
        """Send out a meta meme."""
        await context.send(load_static_text("nudes.txt"))

    @commands.command(pass_context=True)
    async def stalker(self, context):
        """Send out this kaomoji."""
        await context.send("(´・ω・`)")

    @commands.command(pass_context=True)
    async def sonome(self, context):
        """Send out the iconic phrase."""
        await context.send("その目、だれの目？")

    @commands.command(pass_context=True)
    async def IceBango(self, context):
        """Send out the IceBango copypasta."""
        await context.send(load_static_text("ice_bango.txt"))

    @commands.command(pass_context=True)
    async def ping_everyone(self, context):
        """Ping everyone."""
        if context.author.id in config.ADMINS:
            await context.send("@everyone (´・ω・`)")


def setup(client):
    """Add the cog to the client."""
    client.add_cog(Maho(client))
