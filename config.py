import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "13237674"))
API_HASH = os.getenv("API_HASH", "6dab53715c41d7dc14e5d249aa95f704")
SESSION = os.getenv("SESSION", "BQAYu453SK4amN9267sRgm8YuCWhmhB5b8ReEC7LJax4SAusBzmXwdqAcxrt2xRGZjEOXCYubCv7seBibauCGwimOlKuPvXh7iLMtTwGETLCaEuD_vhzxuVhlrZJkoA7POoAGyO_hG2q94grVS5U79rqUa8sG38NX9DQM6C9AdRafaPg1Sg76SdYkOa0hxNG8zYODfJU8wysNO5XNhrZQ_ij98g51BGOltJkBn_SO1lgtHVUnKdOXcyJFJDICUo1lRScIK5o4yDdh2i4hOeTWf0lE6DQYkrcpEc3KRbnFiqNjli6VzIs0qTcYRXe8ADZOBHZ-2GCl5i8PzcvrJ1N9jUNAAAAAU3NrZcA")
HNDLR = os.getenv("HNDLR", "®")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "2027429081").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicUserbot"))
call_py = PyTgCalls(bot)
