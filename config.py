import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "19091945"))
API_HASH = os.getenv("API_HASH", "427b5829d76309c8b3c1d6d38609bf44")
SESSION = os.getenv("SESSION", "BQByXg96LsMdf7fsbHXCCY7HC3P_9vUTUJxYe1acGk3pmWjh0CSsnvRhL32llDGPvajEWNYoYZvmR2xixNpXAYmEuA26Mg8CZ-qWrZVyztvd95HPepI5RrQ2q5yOfhNbqwOk2K9az5pOd2H-G1b6I_T0uOr5k1ppmu4WoEdTe154_RSPye6db-Bs64T-uXV6OxQY8yz-LWU_vaQUSr3RRLUQhEj7NG5fNYA8t4N97yY0iQlJjzVXvvsCbqieDIorrqb12VLFyEizDuFOSEbq3IVdeRmZQH1MDDEdcMYo6UPiczpGpq70VNAoLvcq57qyhF2n4_wlz1emrmjcjeq1Qbd8AAAAAVBGSq4A")
HNDLR = os.getenv("HNDLR", "✓")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1784179805").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicUserbot"))
call_py = PyTgCalls(bot)
