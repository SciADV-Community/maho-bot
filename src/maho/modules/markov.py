"""Cog wrapper module for the !log command and other markov operations."""
import random
from pathlib import Path
from collections import Counter
from discord.ext import commands
from maho import utils


class Markov(commands.Cog):
    """Cog for the markov commandset."""

    def __init__(self, client):
        """Initialize the cog."""
        self.client = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @commands.command(pass_context=True)
    async def log(self, context):
        """Generate and send out a random response using a markov chain."""
        # This code is ugly but somehow works best? So not touching it.
        random_file = random.randint(1, 61)  # nosec
        with open(Path(__file__).parent.parent / "Logs" / random_file) as file:
            words_by_line = [line.split() for line in file]
            words = [word for line in words_by_line for word in line]
            word_counts = Counter(words)
            first_words = [line[0] for line in words_by_line]

            # Get a random first word
            random_index = random.randint(0, len(first_words) - 1)  # nosec
            random_first_word = first_words[random_index]

            # Initialize state
            out = [random_first_word]
            last_added_word = random_first_word
            done = False
            while not done:
                current_index = 0
                times_previous_seen = 0

                # Get random count threshold with upper bound the count of the
                # previously added word
                count_threshold = random.randint(  # nosec
                    1, word_counts[last_added_word]
                )
                while times_previous_seen < count_threshold:
                    current_index += 1

                    # Iterate over  all words until you have encountered the
                    # previously added word count_threshold times
                    if words[current_index] == last_added_word:
                        times_previous_seen += 1

                word_to_add = words[current_index]
                out.append(word_to_add)
                last_added_word = word_to_add

                # Done when punctuation is encountered and there are at least 3 words
                done = last_added_word[-1] in [".", "?", "!"] and len(out) > 3

            message = " ".join(out)
            await context.send(message)


def setup(client):
    """Add the cog to the client."""
    client.add_cog(Markov(client))
