"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ephem import *
import logging
import datetime

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot1.log'
                    )
now = str(datetime.datetime.now())

def planet_ephem(bot, update):
    user_text = update.message.text.split()
    planet = user_text[-1]
    if planet == 'Mars':
        update.message.reply_text(constellation(Mars(now)))
    elif planet == 'Neptune':
        update.message.reply_text(constellation(Neptune(now)))
    elif planet == 'Mercury':
        update.message.reply_text(constellation(Mercury(now)))
    elif planet == 'Venus':
        update.message.reply_text(constellation(Venus(now)))
    elif planet == 'Earth':
        update.message.reply_text(constellation(Earth(now)))
    elif planet == 'Jupiter':
        update.message.reply_text(constellation(Jupiter(now)))
    elif planet == 'Saturn':
        update.message.reply_text(constellation(Saturn(now)))
    elif planet == 'Uranus':
        update.message.reply_text(constellation(Uranus(now)))
    elif planet == 'Pluto':
        update.message.reply_text(constellation(Pluto(now)))
    else:
        update.message.reply_text('Такой планеты не существует')

def main():
    mybot = Updater("907371138:AAGn-c7o5in-bBCen9M9FOVsob8XWvgIQbI", request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler('planet', planet_ephem))

    mybot.start_polling()
    mybot.idle()

main()