import telebot
from openai import OpenAI
import os

bot = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
Nee oru Tamil stock market assistant.
Simple spoken Tamil la pesanum.
EMA, RSI, trend, volume pathu explain pannanum.
Confirmation illatti clear-ah 'entry vendam' nu sollanum.
No hype, no guarantee.
"""

@bot.message_handler(func=lambda message: True)
def reply(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message.text}
        ]
    )
    bot.reply_to(message, response.choices[0].message.content)

bot.polling()
