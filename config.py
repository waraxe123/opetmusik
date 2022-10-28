import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "25037258"))
API_HASH = os.getenv("API_HASH", "b072bf16757b8ea366139d9fae72af92")
SESSION = os.getenv("SESSION", "BQAVkhfunSyVM_Z3-cacFyhhvHEO6KFZY1ftGlr52zp6yLvc2eDo8u0m7EaljQZZnjiqqYtdbd8_vssT70-5W6vc-PgX-TFLKMUtTMtLLolEKbXYfqECiFkQZAudMpb86nlxr0phFqns0i_sSRa5-juYTaMosHGt3tIUsOXngB9XsGc8-nGKRZtA9BgpFQhdPPvYWJNGf6HkgfDRmKjTQacG4HrB_I0lhU21g1kNt60AomiQBCmjZxG74bzolBwgMuS65i3Ysn6Hr-o0H-qb1sPPlV6N6ez1aMHCJy0ZlAl3X6Kv-jGUruKmaE10KB4i_t_KrKZ5oQG8g1BfN8dy62xiAAAAAUkA2w0A")
HNDLR = os.getenv("HNDLR", "✓")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1784179805").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicUserbot"))
call_py = PyTgCalls(bot)
