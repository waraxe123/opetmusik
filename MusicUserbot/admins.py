from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, call_py
from MusicUserbot.helpers.decorators import authorized_users_only
from MusicUserbot.helpers.handlers import skip_current_song, skip_item
from MusicUserbot.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["skip"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴀᴘᴀᴘᴜɴ ᴅɪᴅᴀʟᴀᴍ ᴀɴᴛʀɪᴀɴ ᴜɴᴛᴜᴋ ᴅɪʟᴇᴡᴀᴛɪ!**")
        elif op == 1:
            await m.reply("ᴀɴᴛʀɪᴀɴ ᴋᴏsᴏɴɢ, ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ**")
        else:
            await m.reply(
                f"**⏭ ᴍᴇʟᴇᴡᴀᴛɪ ᴘᴇᴍᴜᴛᴀʀᴀɴ** \n**🎵 sᴇᴋᴀʀᴀɴɢ ᴍᴇᴍᴜᴛᴀʀ** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀɢᴜ-ʟᴀɢᴜ ʙᴇʀɪᴋᴜᴛ ᴅᴀʀɪ ᴀɴᴛʀɪᴀɴ: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.command(["end", "stop"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✅ ᴍᴇɴɢᴀᴋʜɪʀɪ ᴘᴇᴍᴜᴛᴀʀᴀɴ**")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴀᴘᴀᴘᴜɴ ʏᴀɴɢ sᴇᴅᴀɴɢ ᴅɪᴘᴜᴛᴀʀ!**")


@Client.on_message(filters.command(["pause"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ ᴘᴇᴍᴜᴛᴀʀᴀɴ ᴅɪᴊᴇᴅᴀ.**\n\n• ᴜɴᴛᴜᴋ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ ᴘᴇᴍᴜᴛᴀʀᴀɴ, ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ » {HNDLR}resume"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("** ❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴀᴘᴀᴘᴜɴ ʏᴀɴɢ sᴇᴅᴀɴɢ ᴅɪᴘᴜᴛᴀʀ!**")


@Client.on_message(filters.command(["resume"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ ᴘᴇᴍᴜᴛᴀʀᴀɴ ʏᴀɴɢ ᴅɪᴊᴇᴅᴀ**\n\n• ᴜɴᴛᴜᴋ ᴍᴇɴᴊᴇᴅᴀ ᴘᴇᴍᴜᴛᴀʀᴀɴ, ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ » {HNDLR}pause**"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴀᴘᴀᴘᴜɴ ʏᴀɴɢ sᴇᴅᴀɴɢ ᴅɪᴊᴇᴅᴀ!**")
