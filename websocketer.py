from config import USER_ID, TRADED_QUANTITY, SYMBOL, bot
import websocket
import json
from datetime import datetime, timezone
import pytz
from telebot import formatting

new_york_tz = pytz.timezone('America/New_York')

class WebSocketer:
    def __init__(self):
        self.user_id = USER_ID
        self.traded_quantity = TRADED_QUANTITY
        self.symbol = SYMBOL
        
    def on_message(self, ws, message):
        trade = json.loads(message)
        
        symbol = trade['s']
        timestamp = datetime.fromtimestamp(trade['T']/1000, tz=timezone.utc).replace(microsecond=0)
        timestamp = timestamp.astimezone(new_york_tz).strftime("%Y-%m-%d %H:%M:%S")
        # make sure there is only 2 decimal places
        price = "{:.2f}".format(float(trade['p']))
        price_bold = formatting.hbold(price)
        qty = "{:.2f}".format(float(trade['q']))
        side = "🟥" if bool(trade['m']) == True else "🟩"
        
        if float(qty) > self.traded_quantity:
    # text = f"Subscription for CryptoJab 🚀🚀🚀: {product['name']}\n" \
    #        f"Price: {product['price']} {product['currency']}\n"
            # string = f"""{side} - {timestamp} - {price_bold}$ - {qty}x - {side}""",
            string = f"{side} {side} {side} {side} {side} {side} {side}\n" \
                     f"{timestamp} \n" \
                     f"\n" \
                     f"{price_bold} $ \n" \
                     f"{qty} qty. \n" \
                
            # print(string)
            bot.send_message(self.user_id, string)
            
    def on_error(self, ws, error):
        print(error)

    def on_close(self, close_msg):
        print(close_msg)

    def streamTrade(self):
        socket = f"wss://stream.binance.com:9443/ws/{self.symbol}@trade"
        ws = websocket.WebSocketApp(socket, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)
        ws.run_forever()