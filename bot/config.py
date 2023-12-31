from telebot import types, TeleBot

import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
bot = TeleBot(TELEGRAM_API_KEY, parse_mode="HTML")

USER_ID = os.getenv("USER_ID")
TRADED_QUANTITY = int(os.getenv("TRADED_QUANTITY"))
LARGE_TRADED_QUANTITY = int(os.getenv("LARGE_TRADED_QUANTITY"))
SYMBOL = os.getenv("SYMBOL")
POSTGRES_URL = os.getenv("POSTGRES_URL")

if TELEGRAM_API_KEY == None:
    raise Exception("TELEGRAM_API_KEY is not set in .env file")
elif USER_ID == None:
    raise Exception("USER_ID is not set in .env file")
elif TRADED_QUANTITY == None:
    raise Exception("TRADED_QUANTITY is not set in .env file")
elif LARGE_TRADED_QUANTITY == None:
    raise Exception("LARGE_TRADED_QUANTITY is not set in .env file")
elif SYMBOL == None:
    raise Exception("SYMBOL is not set in .env file")
elif POSTGRES_URL == None:
    raise Exception("POSTGRES_URL is not set in .env file")
else:
    print("All environment variables are set correctly")