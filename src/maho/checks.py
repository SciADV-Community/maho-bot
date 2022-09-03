from discord import ApplicationContext

from maho import config


async def is_bot_admin(ctx: ApplicationContext) -> bool:  # pragma: no cover
    """A Pycord predicate to see if a user is a bot admin according to the db.

    :param context: the command invocation context. Mainly need the author.
    :return: whether or not the user is a bot admin.
    """
    if ctx.author.id not in config.ADMINS:
        await ctx.interaction.response.send_message(
            "You are not authorized.", ephemeral=True
        )
        return False
    return True
