from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from downloader import download_video
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك.\n\nأرسل رابط TikTok أو Instagram أو Facebook أو YouTube."
    )


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    try:
        await update.message.reply_text("⏳ جاري التحميل...")

        file_path = download_video(url)

        with open(file_path, "rb") as video:
            await update.message.reply_video(video=video)

        os.remove(file_path)

    except Exception as e:
        await update.message.reply_text(f"❌ حدث خطأ:\n{e}")


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("Bot Started...")

app.run_polling()
