import os
from telegram import Bot
from signal_logic import generate_signal
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

bot = Bot(token=BOT_TOKEN)

def send_signal():
    signal = generate_signal()
    if signal:
        bot.send_message(chat_id=USER_ID, text=signal)
