import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "21414727"))
  API_HASH = os.environ.get("API_HASH", "b4135f6b8cd476d931e78787a0cb77c1")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7011387982:AAFDtR9OPpIpZuG5eNFxY9E8TiDVFacQv1Q")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Abhiistorebot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002084771326"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "ziplinker.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "8a600b4f9a84a1ea10f62afc0813bf3601d990e0")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6796937630"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abhishekkumar876:passpmongodb@cluster0.xobjcca.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001998607849")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821729200"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [AbhiiStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram]()
│
├🔸 Developer: [Mr. Abhii](https://telegram.me/Mr_ABHiiSHEK)
│
├🔸 Update Channel: [Channel](https://t.me/Movilious)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Mr. Abhii](https://telegram.me/Mr_ABHiiSHEK)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://telegram.me/Mr_ABHiiSHEK)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ PORNOGRAPHY CONTENTS are strictly prohibited & get Permanent Ban.
"""
