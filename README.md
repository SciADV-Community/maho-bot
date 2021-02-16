# maho-bot

![Build Status](https://github.com/SciADV-Community/maho-bot/workflows/CI%20%26%20CD/badge.svg)
[![codecov](https://codecov.io/gh/SciADV-Community/maho-bot/branch/master/graph/badge.svg)](https://codecov.io/gh/SciADV-Community/maho-bot)

Fun utility bot on discord made for friends' servers with discord.py

## Development setup

1. Install [poetry](https://python-poetry.org/).
2. Run `poetry install`.
3. Run `poetry run config` to create a `.env` file containing important environment variables for the configuration of the bot.

## Running the bot

### Manually

Run `env $(<.env) poetry run start`

### Docker

1. Have `Docker` and `docker-compose` installed.
2. Run `docker-compose build`.
3. Configure the bot with `poetry run config`.
4. Run `docker-compose up`.

## Running tests

Run `poetry run test --cov-report=html`
