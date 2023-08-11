from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "6164330121:AAGPwIjwQ0bTd8xrv-B0_CKSB3YeWxrxDBA")
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1sBu3Qz3jGivB7cVcPdCsMuI1Btgq80RmejiNKBahXXwO8-erOQe3mzBpxs2Pb2OgyuVTrZ3hoZmYfKCCUMDIagVuDwBwsKiwFEeYPmHBH7WRuKX31eb1WSbMmftm3t320Jo_YnyEZRqF6Hr7fOJLhrc3N8D5Q4zN0MGcJdPFBkY2Je7pfVPr1pHRRy-nb8tSPAXmNIJGDPD_LGhy4etkhjx57IsA2apMaJGhYiLmPIGW3xgWj6Osgz8S5S-vmfaKCecEXCdRE-5bXx6H_1G4rF9eoqFjZMTsdjaKForGHOsg63C1NM7SdHmIfi-RS8wfaR4WeQzsXRG-N23VghF7rqSkw=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "vip757w7") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "𝟕𝟓𝟕𝐖𝟕") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "sssssbot1_bot") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "vipanstabot") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "vipansta") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5924623813").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5924623813").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
