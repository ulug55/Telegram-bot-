from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.getenv("8135642639:AAH0Vp2yoy5cKAdVCVpcw2BaQxegza8jBkY")

def start(update, context):
    update.message.reply_text("Salom! kino kodini yozing🎬")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
print("8135642639:AAH0Vp2yoy5cKAdVCVpcw2BaQxegza8jBkY"BOT_TOKEN)
