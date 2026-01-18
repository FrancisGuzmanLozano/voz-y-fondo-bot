import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 Voz y Fondo\n\nEl sistema está vivo."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Arranca el bot (polling)
    app.run_polling(close_loop=False)

    # Mantiene el proceso vivo para Render
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
