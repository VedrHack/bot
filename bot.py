# -*- coding: utf-8 -*-
import telebot

import config

bot = telebot.TeleBot(config.tocen)

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.from_user.id, "Привет я бот Вася Пупкин!") 
	
bot.polling(none_stop=True)