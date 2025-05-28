import os
from telegram.ext import Updater, CommandHandler

# Получаем токен из переменной окружения
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена!")

# Обработчик команды /start
def start(update, context):
    update.message.reply_text("Привет! Бот работает 🟢")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Добавляем хендлер для /start
    dp.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()

    print("Бот запущен и слушает команды...")

    # Ждём завершения
    updater.idle()

if __name__ == '__main__':
    main()
