from ThavaXMusic.core.bot import THAVA
from ThavaXMusic.core.dir import dirr
from ThavaXMusic.core.git import git
from ThavaXMusic.core.userbot import Userbot
from ThavaXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = THAVA()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
