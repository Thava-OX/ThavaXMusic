from pyrogram import filters
from ThavaXMusic import app

@app.on_message(filters.command(["stickerid","stid"]))
async def sticker_id(app: app, msg):
    if not msg.reply_to_message:
        await msg.reply_text("Reply to a sticker")        
    elif not msg.reply_to_message.sticker:
        await msg.reply_text("Reply to a sticker")        
    st_in = msg.reply_to_message.sticker
    await msg.reply_text(f"""
⊹ <u>**sᴛɪᴄᴋᴇʀ ɪɴғᴏ**</u> ⊹
**⊚ sᴛɪᴄᴋᴇʀ ɪᴅ **: `{st_in.file_id}`\n
**⊚ sᴛɪᴄᴋᴇʀ ᴜɴɪǫᴜᴇ ɪᴅ **: `{st_in.file_unique_id}`
""")
