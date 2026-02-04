import os
import time
from telegram import Bot

# ===== ENV =====
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

if not BOT_TOKEN or not CHANNEL_ID:
    raise Exception("Secrets not set")

bot = Bot(token=BOT_TOKEN)

def main():
    message = (
        "🔥 *Amazon Deal Test Post*\n\n"
        "📦 Sample Product\n"
        "💰 Price: ₹999\n"
        "🔗 https://www.amazon.in\n\n"
        "⚡ Auto post working!"
    )

    bot.send_message(
        chat_id=CHANNEL_ID,
        text=message,
        parse_mode="Markdown"
    )

    time.sleep(5)

if __name__ == "__main__":
    main()