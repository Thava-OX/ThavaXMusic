from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from ThavaXMusic import app
from config import OWNER_ID
from ThavaXMusic.misc import SUDOERS
from pyrogram.types import Message
from ThavaXMusic.utils.daxx_ban import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from ThavaXMusic.utils.database import delete_served_chat

@app.on_message(filters.command("leavegroup")& SUDOERS)
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**sᴜᴄᴄᴇssғᴜʟʟʏ ʜɪʀᴏ !!.**"
    await message.reply_text(text)
    await delete_servred_chat(chat_id)
    await app.leave_chat(chat_id=chat_id, delete=True)
