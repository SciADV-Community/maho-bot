#!/usr/bin/env python

"""Command-line utility to interact with the bot."""
import re
import runpy
import subprocess
from pathlib import Path

import click
import yaml

from maho.models import Festivity, setup_tables


def stringify_list(values, process=None):
    """Change a python list into its string representation."""
    strings = [f'"{value}"' for value in values if value]
    if process:
        strings = [process(string) for string in strings]
    return f"[{', '.join(strings)}]"


@click.group()
def scripts():
    pass


@scripts.command()
@click.option(
    "--prefix", "-p", prompt="Prefix to use for bot commands", type=str, default="$"
)
@click.option(
    "--description", "-d", prompt="The bot's description text", type=str, default=""
)
@click.option("--token", "-t", prompt="The bot's access token", type=str)
@click.option("--admins", "-a", prompt="User IDs of Bot admins", type=str, default="")
@click.option(
    "--database", "-db", prompt="The database file to use", type=str, default="maho.db"
)
def config(prefix, description, token, admins, database):
    """Initialize the bot's configuration."""
    root_dir = Path(__file__).parent

    # Admin parsing
    admins = ";".join(re.split(r", |,| ", admins))

    # Save into .env file
    dotenv = root_dir / ".env"
    with dotenv.open(mode="w") as f:
        f.writelines(
            [
                f"BOT_PREFIX={prefix}\n",
                f"BOT_TOKEN={token}\n",
                f"BOT_DESCRIPTION={description}\n",
                f"BOT_ADMINS={admins}\n",
                f"BOT_DB={database}\n",
            ]
        )

    click.secho("Config initialized successfully.", fg="green")


@scripts.command()
def test():
    """Run tests."""
    subprocess.run("pytest")


@scripts.command()
def start():
    """Run the bot."""
    runpy.run_module("maho.main", run_name="__main__")


@scripts.command()
def init_db():
    """Initialize the database from a fixture."""
    setup_tables()
    festive_fixtures = (
        Path(__file__).parent / "src" / "maho" / "fixtures" / "festive.yml"
    )
    try:
        with festive_fixtures.open() as f:
            festivities = yaml.load(f, Loader=yaml.FullLoader)
            for festivity in festivities:
                festivity = next(iter(festivity.values()))
                Festivity.get_or_create(
                    date=festivity["date"], description=festivity["description"]
                )
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    scripts()
