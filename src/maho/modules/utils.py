import random
from collections import Counter
from discord.ext import commands
from maho import config, utils


class Utils(commands.Cog):
    ### Fields ###
    def __init__(self, client):
        self.client = client
		logger = utils.get_logger()
        logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def rate(self, context, *, arg):
        i = 0
        for c in arg:
            i = i * 37 + ord(c)
        i %= 11

        await context.send(f"I'd give {arg} a {i}/10")


def setup(client):
    client.add_cog(Utils(client))
