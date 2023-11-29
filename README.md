# crypto-tape-telegram-bot

Description
This project is a Python script that uses the pyTelegramBotAPI and websocket libraries to stream trade data from Binance and send it to a Telegram bot. The trade data includes the symbol, timestamp, price, and quantity of trades. The script is designed to send a message to a Telegram bot whenever the quantity of a trade is greater than a specified threshold.
Table of Contents

    Installation
    Usage
    Contributing

Installation

To install the necessary dependencies, you can use pip:

pip install pyTelegramBotAPI websocket-client pytz

You will also need to create a Telegram bot and get its API token. You can do this by talking to the BotFather on Telegram.
Usage

Before running the script, you need to set up a few environment variables:

    USER_ID: The ID of the Telegram user to send the messages to.
    TRADED_QUANTITY: The minimum quantity of a trade to trigger a message.
    SYMBOL: The symbol of the cryptocurrency to track.
    TELEGRAM_BOT_TOKEN: The API token of your Telegram bot.

You can set these environment variables in a .env file in the root of your project.

To run the script, use the following command:

python main.py

The script will start streaming trade data from Binance and send a message to the specified Telegram user whenever a trade with a quantity greater than TRADED_QUANTITY is made.

Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.