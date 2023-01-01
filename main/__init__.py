#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "22652671"
API_HASH = "c42c23dbe7e986eefb58deb05ab7b7af"
BOT_TOKEN = "5842282445:AAFc67A6xEH3EP91dpOLtQzrFZkv9O7xTSU"
SESSION = "BACTQDhYIzPIqY0liYOzKlFS1tWdpQ1jJH-MqXiXlcTXc-3hCDAJRuYLX1DZkT4UnRXun6Sz8YYogbNyIjy-57D3yrbSVPY8ETMGk6LKj6IToglHRRVmiAeThyei2oZnp9OPhRwrVk8i9H_Ywo2sIu4xMX5tK6XKJzPpV4Q-kLGmnMxfVa5geg9tkuto5K6nVhyiw_tvhxsEDl5lNXlRleMi-x7Qj0TjVGZIdJi0i47gkXJEVmxHTSgd5LJqzwXdXEvj82w3KvzItN0RysxAQkXuM9Gaw-rNmw1clHZZYvmYxIrAt1qvN_i9qFhW3ajyE9jfbtbhTPj7jBVg5tgcF9koAAAAAVw6J80B"
FORCESUB = "https://t.me/allopepdfasd"
AUTH = "josh_1200"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
