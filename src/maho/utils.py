"""Module with various utilities for the bot."""
import logging


def generate_logger():
    """Create the Logger."""
    logger = logging.getLogger("Maho")
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(filename="maho-log.log", encoding="utf-8", mode="a")
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )

    logger.addHandler(handler)
    logger.addHandler(logging.StreamHandler())

    return logger


_logger = generate_logger()


def get_logger():
    """Give access to the Logger."""
    return _logger
