from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from strings import get_string, helpers
from ThavaXMusic import app
from pyrogram.types import InputMediaVideo
from ThavaXMusic.misc import SUDOERS
from ThavaXMusic.utils.database import add_sudo, remove_sudo
from ThavaXMusic.utils.decorators.language import language
from ThavaXMusic.utils.extraction import extract_user
from ThavaXMusic.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID, START_IMG_URL


@app.on_message(filters.command(["addsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["delsudo", "rmsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])



GAMDOP = START_IMG_URL

@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
async def sudoers_list(client, message: Message):
    keyboard = [[InlineKeyboardButton(" sᴜᴅᴏʟɪsᴛ ", callback_data="check_sudo_list")]]
    reply_markups = InlineKeyboardMarkup(keyboard)
    await message.reply_photo(photo=GAMDOP, caption="➤ ᴄʜᴇᴄᴋ ᴛᴏ sᴇᴇɴ ᴛʜᴇ ᴍᴀɢɪᴄ ʙʟɪɴɢ ʙʟɪɴɢ ✨.\n\n <u><b>ɴᴏᴛᴇ:</b></u> ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ.", reply_markup=reply_markups)


@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):
    keyboard = []
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer("➤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴜᴅᴏ 😝 ᴛʜɪꜱ ʟɪꜱᴛ ᴏɴʟʏ ᴏᴘᴇɴ ᴏᴡɴᴇʀ ᴀɴᴅ ꜱᴜᴅᴏ ᴏɴʟʏ 😏", show_alert=True)
    else:
        user = await app.get_users(OWNER_ID)

        user_mention = (user.first_name if not user.mention else user.mention)
        caption = f"<u><b>**˹ʟɪsᴛ ᴏғ ʙᴏᴛ ᴍᴏᴅᴇʀᴀᴛᴏʀs˼**\n\n🥀 ᴏᴡɴᴇʀ :</b></u>\n ‣ {user_mention}\n\n"
        sudo_users_caption = "<u><b>✨ sᴜᴅᴏ ᴜsᴇʀs :</b></u>\n"

        keyboard.append([InlineKeyboardButton("« ᴠɪᴇᴡ ᴏᴡɴᴇʀ »", url=f"tg://openmessage?user_id={OWNER_ID}")])
        keyboard.append([InlineKeyboardButton("« ᴄʟᴏsᴇ »",callback_data="close_data")])
        
        count = 1
        for user_id in SUDOERS:
            if user_id != OWNER_ID:
                try:
                    user = await app.get_users(user_id)
                    user_mention = user.mention if user else f"**✨ sᴜᴅᴏ ᴜsᴇʀs {count} ɪᴅ:** {user_id}"
                    caption += f"**✨ sᴜᴅᴏ ᴜsᴇʀs** {count} **»** {user_mention}\n"
                    button_text = f"➤ ᴠɪᴇᴡ sᴜᴅᴏ {count}"
                    keyboard.append([InlineKeyboardButton(button_text, url=f"tg://openmessage?user_id={user_id}")]
                    )
                    count += 1
                except:
                    continue

        # Add a "Back" button at the end
        keyboard.append([InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="back_to_main_menu")])

        if keyboard:
            reply_markup = InlineKeyboardMarkup(keyboard)
            await callback_query.message.edit_caption(caption=caption, reply_markup=reply_markup)

@app.on_callback_query(filters.regex("^back_to_main_menu$"))
async def back_to_main_menu(client, callback_query: CallbackQuery):
    keyboard = [[InlineKeyboardButton("✨ ᴠɪᴇᴡ sᴜᴅᴏʟɪsᴛ ✨", callback_data="check_sudo_list")]]
    reply_markupes = InlineKeyboardMarkup(keyboard)
    await callback_query.message.edit_caption(caption="**» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n**» ɴᴏᴛᴇ:**  ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ. ", reply_markup=reply_markupes)




@app.on_message(filters.command(["delallsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def del_all_sudo(client, message: Message, _):
    count = len(SUDOERS) - 1  # Exclude the admin from the count
    for user_id in SUDOERS.copy():
        if user_id != OWNER_ID:
            removed = await remove_sudo(user_id)
            if removed:
                SUDOERS.remove(user_id)
                count -= 1
    await message.reply_text(f"Removed {count} users from the sudo list.")
