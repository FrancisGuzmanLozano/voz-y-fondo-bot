import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 Voz y Fondo\n\nPrueba activa.\nA continuación escucharás dos audios."
    )

    await update.message.reply_audio(
        audio="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        caption="Canción 01"
    )

    await update.message.reply_audio(
        audio="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        caption="Canción 02"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
