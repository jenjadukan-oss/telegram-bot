from telebot import types

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
button = types.KeyboardButton("Отправить номер", request_contact=True)
markup.add(button)

bot.send_message(message.chat.id, "Нажми кнопку чтобы отправить номер", reply_markup=markup)