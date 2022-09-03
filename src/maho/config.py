"""Configuration bindings for the bot."""
import os

DESCRIPTION = os.getenv("BOT_DESCRIPTION", "")
TOKEN = os.getenv("BOT_TOKEN")
DB = os.getenv("BOT_DB", "maho.db")

ADMINS = [
    int(admin) if admin else 0 for admin in os.getenv("BOT_ADMINS", "").split(";")
]
