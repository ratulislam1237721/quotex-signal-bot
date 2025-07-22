import os
import time
from datetime import datetime
from dotenv import load_dotenv
import telebot

# .env ফাইল থেকে টোকেন লোড করা
load_dotenv('config.env')
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = '7245678860'  # আপনার টেলিগ্রাম ইউজার আইডি

bot = telebot.TeleBot(TOKEN)

def generate_signal():
    # সিগনাল তৈরি করার জন্য সিম্পল র‍্যান্ডম বাছাই
    import random
    direction = random.choice(['⬆️ Call', '⬇️ Put'])
    result = random.choice(['✅ Win', '❌ Loss'])
    now = datetime.now().strftime('%H:%M:%S')
    message = f"""
📊 Quotex Signal Alert

🕒 Time: {now}
💹 Pair: URUUSD
📈 Direction: {direction}
⌛ Duration: 1 Minute

💡 Result: {result}

⚠️ Trade within next 5 seconds!
"""
    return message

def send_signal():
    signal = generate_signal()
    bot.send_message(CHAT_ID, signal, parse_mode='Markdown')

if __name__ == '__main__':
    while True:
        try:
            send_signal()
            time.sleep(300)  # প্রতি ৫ মিনিটে সিগনাল পাঠানো হবে
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)
