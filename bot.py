import telebot

TOKEN = "8217794829:AAFiTQqlJw8t4GEqHYw8RbB-DjtqtWbrDR4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá, querida! Estou aqui para te ajudar. 😍")

@bot.message_handler(func=lambda message: True)
def responder(message):
    bot.reply_to(message, "Querida, recebi sua mensagem. Já já te respondo 💕")

bot.polling()
