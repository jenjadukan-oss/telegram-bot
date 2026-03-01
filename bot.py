import telebot

TOKEN = "8598047892:AAEydgq1ip8wHXkwpPS073j2KYchDtuQL8s"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Бот работает 🚀")

bot.infinity_polling()