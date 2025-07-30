from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8461610744:AAGhqcrnJBj9nPuCSHx2oE7ZuMezycJ9Uow"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "привет":
        await update.message.reply_text("Привет!")
    elif text == "как дела?":
        await update.message.reply_text("Всё хорошо, спасибо!")
    else:
        await update.message.reply_text("Я понимаю только 'Привет' и 'Как дела?'")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
