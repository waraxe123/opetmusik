import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "18124377"))
API_HASH = os.getenv("API_HASH", "b4a24da3bf670fefe3c0e719e1569b14")
SESSION = os.getenv("SESSION", "BQAQe9OEAuwzpmMXTDmlMSrDSRlG8nhxbRJDLlpMAEdR-4SCYh3lHo-cj6znHipduWYB2o3EMgFeCnCl8cw_1oFxR-088JbkKdsAw_s7kUopUy_M8oXpM2cTXXbtFXPbOZ9Pb1vR_MwlsIyQriMYUrPmbnSf2gsy1SwpTGcfe1CRBZem9vSez7w9udZ71pqvDthqoA564HoNW-tQXRjqkIgmOqgWtVTsrpWKf2kA0Y6140OouEuHiYMGth2vDqL8MwBLaUlt_8CNod2SvRs7k1iPXjWex58g9MVI2sUzwoW3twJyMmq196dbw5u1floxrOch0NV8MmJRTTZoqqdyLT4pAAAAAVTZ1jYA")
HNDLR = os.getenv("HNDLR", "✓")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "2027429081").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicUserbot"))
call_py = PyTgCalls(bot)
