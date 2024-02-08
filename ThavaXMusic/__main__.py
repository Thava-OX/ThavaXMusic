import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ThavaXMusic import LOGGER, app, userbot
from ThavaXMusic.core.call import THAVA
from ThavaXMusic.misc import sudo
from ThavaXMusic.plugins import ALL_MODULES
from ThavaXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ThavaXMusic.plugins" + all_module)
    LOGGER("ThavaXMusic.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await THAVA.start()
    try:
        await THAVA.stream_call("https://telegra.ph/file/26541097b8833e61f603d.mp4")
    except NoActiveGroupCall:
        LOGGER("ThavaXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await THAVA.decorators()
    LOGGER("ThavaXMusic").info(
        "Music bot Started Successfully, Power By @TBNBotsNetwork"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ThavaXMusic").info("Stopping Thava X Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
