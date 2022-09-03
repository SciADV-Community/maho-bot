"""Cog wrapper module for the !log command and other markov operations."""
import random
from collections import Counter
from pathlib import Path

import discord

from maho import utils


def get_markov_message(lines: list[str]) -> str:
    """Get a random message based on a markov chain."""
    words_by_line = [line.split() for line in lines]
    words = [word for line in words_by_line for word in line]
    word_counts = Counter(words)
    first_words = [line[0] for line in words_by_line]

    # Get a random first word
    random_index = random.randint(0, len(first_words) - 1)
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
        count_threshold = random.randint(1, word_counts[last_added_word])
        while times_previous_seen < count_threshold:
            # Iterate over  all words until you have encountered the
            # previously added word count_threshold times
            if words[current_index] == last_added_word:
                times_previous_seen += 1

            current_index += 1

        word_to_add = words[current_index]
        out.append(word_to_add)
        last_added_word = word_to_add

        # Done when punctuation is encountered and there are at least 3 words
        done = last_added_word[-1] in [".", "?", "!"] and len(out) > 3

    return " ".join(out)


class Markov(discord.Cog):  # pragma: no cover
    """Cog for the markov commandset."""

    def __init__(self, client: discord.Bot):
        """Initialize the cog."""
        self.client: discord.Bot = client
        self.logger = utils.get_logger()
        self.logger.info("Module %s loaded", self.__class__.__name__)

    @discord.slash_command(
        description="Send out a random response using a markov chain."
    )
    async def log(self, ctx: discord.ApplicationContext):
        random_file = random.randint(1, 61)
        with open(Path(__file__).parent.parent / "Logs" / str(random_file)) as file:
            message = get_markov_message(file.readlines())

        await ctx.respond(message)


def setup(client):  # pragma: no cover
    """Add the cog to the client."""
    client.add_cog(Markov(client))
