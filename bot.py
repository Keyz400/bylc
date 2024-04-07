from telegram import Update
from telegram.parsemode import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "6592552636:AAEk_MWhr3IoYuuKggs8ZA24NK_4NXYEnFg"
DOWNLOAD_LOCATION = "downloads/"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Send me the YouTube URLs you want to download.")

def download_url(update: Update, context: CallbackContext):
    urls = context.args
    
    for url in urls:
        try:
            subprocess.run(["yt-dlp", "-o", f"{DOWNLOAD_LOCATION}/%(title)s.%(ext)s", url])
        except Exception as e:
            update.message.reply_text(f"An error occurred: {str(e)}")
    
    update.message.reply_text("Videos downloaded successfully!")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download_url))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
