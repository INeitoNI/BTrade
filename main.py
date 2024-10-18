import telebot
import api_key

API_TOKEN = api_key.KEY
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    web_app_info = telebot.types.WebAppInfo("https://username.github.io/your-repo")
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Open Web App", web_app=web_app_info))
    bot.send_message(message.chat.id, "Click the button to open the Web App:", reply_markup=markup)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
