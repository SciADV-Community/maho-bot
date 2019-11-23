import random
from collections import Counter
from discord.ext import commands
from maho import config, utils


class Markov(commands.Cog):
    def __init__(self, client):
        self.client = client
		logger = utils.get_logger()
        logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def log(self, context):
        # This code is ugly but somehow works best? So not touching it.
        rand = random.randint(1, 61)
        with open("./Logs/{}".format(rand)) as file:
            kongroo = [line.split() for line in file]
            flat = [item for sublist in kongroo for item in sublist]
            Cunt = Counter(flat)
            one = [row[0] for row in kongroo]
            punc = [".", "?", "!"]

            A = random.randint(0, len(one) - 1)
            Sent = []
            Sent.append(one[A])
            a = 0
            flag = 0
            l = 0
            while flag < 1:
                b = 0
                c = 0
                A = random.randint(1, Cunt[Sent[a]])
                while c < A:
                    if flat[b] == Sent[a]:
                        c += 1
                    b += 1
                Sent.append(flat[b])
                a = a + 1
                str1 = " ".join(str(x) for x in Sent)
                l = len(str1) - 1

                if (str1[l:] == "." or str1[l:] == "?" or str1[l:] == "!") and (
                    len(Sent) > 3
                ):
                    flag = 1

            message = " ".join(Sent)
            await context.send(message)


def setup(client):
    client.add_cog(Markov(client))
