from cgitb import text
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(update, context):
    text = "Вызван /start"
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = (f'Привет {update.message.chat.first_name}! Ты написал: {update.message.text}')
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.first_name,
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.APY_KEY)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle() 

main()
