import os
from telegram.ext import Updater, CommandHandler
from telegram import InputMediaVideo
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена!")

if not CHAT_ID:
    raise ValueError("Переменная окружения CHAT_ID не установлена!")

# Текст сообщения
message_text = (
    "Продержишься дольше?\n"
    "➡ https://1wbfqv.life/v3/2451/rocket-queen?p=2u70\n\n"
    "5к на карту тому, кто продержится дольше, скрины кидать сюда: \n"
    "https://t.me/+C1wUvbv1V7I1NWQy (в описании мой контакт)"
)

# URL на видеофайл на GitHub (если оно публичное)
video_url = "https://raw.githubusercontent.com/manilong/tgbot/blob/main/video.MP4"  # замените

# Обработчик команды /start
def start(update, context):
    context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=video_url,
        caption=message_text,
        parse_mode='HTML'
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    # Отправка сообщения с видео при старте
    updater.bot.send_video(
        chat_id=CHAT_ID,
        video=video_url,
        caption=message_text,
        parse_mode='HTML'
    )

    print("Бот запущен и отправил сообщение...")

    updater.idle()

if __name__ == '__main__':
    main()
