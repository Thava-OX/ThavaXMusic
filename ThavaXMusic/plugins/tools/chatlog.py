from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from config import LOGGER_ID as LOG_GROUP_ID
from ThavaXMusic import app 
from ThavaXMusic.core.userbot import Userbot
from ThavaXMusic.utils.database import delete_served_chat

userbot = Userbot()

photo = [
    "https://telegra.ph/file/57833b98b817e6d9c6d65.jpg",
    "https://telegra.ph/file/49c00ae46b757080d7431.jpg",
    "https://telegra.ph/file/f5fc6b1050edd54c74bd5.jpg",
    "https://telegra.ph/file/c6159c4cca243947040d1.jpg",
    "https://telegra.ph/file/5f4484f995f9912d09f83.jpg",
]

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
        await delete_served_chat(chat_id)
        await userbot.one.start()
        await userbot.one.leave_chat(chat_id)
        await userbot.one.stop()
