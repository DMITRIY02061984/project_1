import telebot
import random



answer = ("бесспорно", "предрешено", "никаких сомнений", "определенно да",
          "можеш быть уверен в этом",
          "мне кажется - да",
          "вероятнее всего",
          "хорошие перспективы",
          "знаки говорят - да",
          "да",
          "пока не ясно, попробуй снова",
          "спроси позже",
          "лучше не рассказывать",
          "сейчас нельзя предсказать",
          "сконцентрируйся и спроси опять",
          "даже не думай",
          "мой ответ - нет",
          "по моим данным - нет",
          "перспективы не очень хорошие",
          "весьма сомнительно")



bot = telebot.TeleBot('5335670598:AAEcLYOVHzTt6nokZzeelNxdmAXntImvbQc')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, 'Хочешь узнать предсказание, задай вопрос.', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    bot.send_message(message.chat.id, random.choice(answer), parse_mode='html')




bot.polling()
