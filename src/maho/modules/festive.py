import random
from collections import Counter
from datetime import date
from discord.ext import commands
from maho import config, utils, model

months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def get_date(festivity):
    newdate = date
    date_str = festivity[0].split()
    month = months[date_str[0].lower()]
    day = int(date_str[1])
    return date(2016, month, day)


class Festive(commands.Cog):
    def __init__(self, client):
        self.client = client
        logger = utils.get_logger()
        logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def festive(self, context):
        festivities = model.get_festivities()

        msg = ""
        for festivity in sorted(festivities, key=get_date):
            msg += f"{festivity[0]}: {festivity[1]}\n"

        msg += "\nNext month: Kevin appreciation day.\nEnder remembrance day: All days.\nReal Spic Hours: from when spics start talking in spanish to until spics start speaking english again.\n\n*only applies to: Aluido, Bango, loo, Magnificient, Marco, Raniel.\n*Ice , Cypert, Nizharu, Valkyrio and Majaraja may take part on this if they want."

        await context.send(msg)

    @commands.command(pass_context=True)
    async def add_festive(self, context, date, festivity):
        if context.author.id in config.ADMINS:
            try:
                dates = date.split()
                if dates[0].lower() not in months.keys():
                    await context.send("Invalid month")
                elif int(dates[1]) > 31 or int(dates[1]) < 1:
                    await context.send("Invalid day")
                else:
                    model.add_festivity(date, festivity)
                    await context.send("Added festivity")
            except:
                await context.send(
                    "Error occured when adding festivity, invalid first argument likely, reminder to wrap them in quotations!"
                )

    @commands.command(pass_context=True)
    async def ping_everyone(self, context):
        if context.author.id in config.ADMINS:
            await context.send("@everyone (´・ω・`)")


def setup(client):
    client.add_cog(Festive(client))
