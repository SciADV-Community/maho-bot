#!/usr/bin/env python3

"""Main module to run the bot."""
import discord
from maho import config, models, utils

import sqlite3

# Logging
logger = utils.get_logger()

# Model setup
models.setup_tables()

# State
class Maho(discord.Bot):
    """The main Bot class for Maho!"""

    COGS = ["festive", "maho", "markov", "utils"]

    def __init__(self, description=None, *args, **options):
        """The main Bot class for Maho!

        :param description: The bot description.
        """
        super().__init__(description, *args, **options)

        # Load cogs
        extensions = [f"maho.cogs.{cog}" for cog in self.COGS]
        self.load_extensions(*extensions)

    async def on_ready(self):
        """Handle what happens when the bot is ready."""
        logger.info(f"Logged in as {client.user.name} - {client.user.id}")
        logger.info(f"------ Guilds ({len(client.guilds)}) ------")
        for guild in client.guilds:
            logger.info(guild.name)

    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.DiscordException
    ):
        """Handle errors globally."""
        logger.error("Error occurred for command %s: %s", ctx.command, error)


# Intents
# TODO proper research on this
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Running the client
client = Maho(
    description=config.DESCRIPTION,
    intents=intents,
)
client.run(config.TOKEN)

# TODO find some way to restore this functionality I guess
# @client.event
# async def on_message(message):
#     """Handle new messages."""
#     if message.author is not client:
#         if message.content.startswith("!!log"):
#             await message.channel.send("Are you fucking retarded")
#         elif message.content.startswith("!!!log"):
#             await message.channel.send(
#                 "On how many layers of idiocy are you right now?"
#             )
#         elif message.content.startswith("!!!!log"):
#             await message.channel.send("You gotta stop drinking, dude")
#         else:
#             await client.process_commands(message)
