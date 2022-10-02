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
SESSION = os.getenv("SESSION", "BQCCoB_Qr8j3d_BJrkpmtemoi24GA4HGWvpAYbxCOBt2-9mGr31LUvXs3Ku9C35tck4WeQbrkcgnb-yxDdbceyp0FEL2IkDT3_d1aK9o2tcYSsXGNvKZVh5ptMFrwbYKGyzEZ54jHwwZ-in_1GlfKJLWXIEdtLM5WN39Rhv2LrH8ckiKB5wLpmLpYLc4CBqxlT6mYNXlLJNyg-DJni44jeUaEg_60pdl8bcW6GlcGf_ySlg6R6vtJZxt25cJzkk_oWP4ziH1864EE0jRo3NfQjrpMzq7egZCWOFY1jjeZMxaCJif-8BhjeB8Nya2zW5IdbCht58Nuen073EA6Ee89rK2AAAAAU3NrZcA")
HNDLR = os.getenv("HNDLR", "®")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "2027429081").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicUserbot"))
call_py = PyTgCalls(bot)
