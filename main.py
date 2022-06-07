import os
import json
from dotenv import load_dotenv

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

load_dotenv()
TOKEN = os.getenv('TOKEN')


def start(update, context):
    keyboard = [
        [
            KeyboardButton(
                "Webapp", web_app=WebAppInfo(url="https://python-telegram-bot.org/static/webappbot"),)
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('Hi!', reply_markup=reply_markup)

# Handle incoming WebAppData


def webapp(update, context):
    data = json.loads(update.effective_message.web_app_data.data)
    print(data)
    update.message.reply_text('Webapp data: {}'.format(data))


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(
        Filters.status_update.web_app_data, webapp))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
