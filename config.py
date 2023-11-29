from telebot import types, TeleBot

import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
bot = TeleBot(TELEGRAM_API_KEY, parse_mode="HTML")

USER_ID = os.getenv("USER_ID")
TRADED_QUANTITY = int(os.getenv("TRADED_QUANTITY"))
SYMBOL = os.getenv("SYMBOL")

if TELEGRAM_API_KEY == None:
    raise Exception("TELEGRAM_API_KEY is not set in .env file")
elif USER_ID == None:
    raise Exception("USER_ID is not set in .env file")
elif TRADED_QUANTITY == None:
    raise Exception("TRADED_QUANTITY is not set in .env file")
elif SYMBOL == None:
    raise Exception("SYMBOL is not set in .env file")