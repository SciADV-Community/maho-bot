import random
from collections import Counter
from discord.ext import commands
from maho import config, utils


class Maho(commands.Cog):
    def __init__(self, client):
        self.client = client
        logger = utils.get_logger()
        logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def lebby(self, context):
        await context.send("( Í¡Â° ÍœÊ– Í¡Â°)")

    @commands.command(pass_context=True)
    async def ChaosPomf(self, context):
        await context.send(
            "```Pomf pomf kimochi\nWhat's this sticky blood on me\nThey'll mess with me until\nI see delusions everywhere\nMorning, to no one\nToday I will fap to Seira-tan\nkiLL mE am I dead\nStomped by reporters```"
        )

    @commands.command(pass_context=True)
    async def rules(self, context):
        await context.send(
            "1, Be excellent to each other.\n1.1, The Enter Key isn't a correct punctuation.\n2,  Party on, dude.\n3, Don't be dicks to each other.\n4, NO ABUSE OF POWER. PLAYFUL TEASING IS ALLOWED, BUT OUTRIGHT DICKERY SHALL NOT BE TOLERATED. IN ADDITION, FALSE NOTICES OF OFFICIAL  LOCALISATION/FAN TRANSLATION ANNOUNCEMENTS WILL BE TREATED AS AN ABUSE OF POWER, AND WILL BE DEALT WITH APPROPRIATELY.\n4.1, Puns are both permitted and encouraged by Sir 𝓑𝓵𝓲𝓬𝓴 𝓦𝓲𝓷𝓴𝓮𝓵 himself. Any such puns are exempt from all previous rules so long as they are sufficiently funny as ruled by the coucil of 𝓑𝓵𝓲𝓬𝓴 𝓦𝓲𝓷𝓴𝓮𝓵, 𝕊𝕥𝕖𝕚𝕟𝕖𝕣, and the Captain. In case any of the 3 are absent at the time of judgement, the majority rule shall go to whoever's name is higher on the member list."
        )

    @commands.command(pass_context=True)
    async def lenny(self, context):
        await context.send("( ͡° ͜ʖ ͡°)")

    @commands.command(pass_context=True)
    async def ice(self, context):
        await context.send(
            "https://cdn.discordapp.com/attachments/124698456727093248/303973470180474901/iced.png"
        )

    @commands.command(pass_context=True)
    async def nudes(self, context):
        await context.send(
            "https://cdn.discordapp.com/attachments/128988222838669313/304093442454192138/PostingMemeOnline.png"
        )

    @commands.command(pass_context=True)
    async def stalker(self, context):
        await context.send("(´・ω・`)")

    @commands.command(pass_context=True)
    async def sonome(self, context):
        await context.send("その目、だれの目？")

    @commands.command(pass_context=True)
    async def IceBango(self, context):
        await context.send(
            "```Each morning, a missionary advertises neon sign\nHe tells the damn spaniard that Bango is fine\nAnd the spanish shota holler from an olive tree\nThat sexuality is a thing for me to see \nSo bango, bango, bango, I don't wanna cong her hoo, oh no no no no no\nBango, mingle, single, I'm so happy in wizardry, I refuse to go\nDon't want no sex life, false breasts, titfuck, sixty-nine, I make it clear\nThat no matter how they coax her, I'll stay 'ever pure```"
        )


def setup(client):
    client.add_cog(Maho(client))
