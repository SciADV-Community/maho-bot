"""Configuration bindings for the bot."""
import os

PREFIX = os.getenv("BOT_PREFIX", "$")
DESCRIPTION = os.getenv("BOT_DESCRIPTION", "")
TOKEN = os.getenv("BOT_TOKEN")
DB = os.getenv("BOT_DB", "maho.db")

ADMINS = [
    int(admin) if admin else 0 for admin in os.getenv("BOT_ADMINS", "").split(";")
]
MODULES = os.getenv("BOT_MODULES", "").split(";")
STARTUP = os.getenv("BOT_STARTUP_MODULES", "").split(";")
