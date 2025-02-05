import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from joke import *
import time

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bye, Bye!")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    a = get_joke()
    print(a)
    if (a["type"] == 'single'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=a["joke"])
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=a["setup"])
        time.sleep(2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=a["delivery"])

if __name__ == '__main__':
    application = ApplicationBuilder().token('7856920665:AAFzjHcn85QXAQOj0gcWgu2YDyq8oeZDjmk').build()
    
    start_handler = CommandHandler('start', start)
    end_handler = CommandHandler('end', end)
    joke_handler = CommandHandler('joke', joke)
    application.add_handler(start_handler)
    application.add_handler(end_handler)
    application.add_handler(joke_handler)

    
    application.run_polling()