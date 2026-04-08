import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

# Старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["📄 Помощь", "🔥 Идея"], ["💬 Написать"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Привет 👋\nЯ твой первый бот.\nВыбери, что сделать:",
        reply_markup=reply_markup
    )

# Ответы на кнопки
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📄 Помощь":
        await update.message.reply_text("Я простой бот. Скоро стану умнее 😎")

    elif text == "🔥 Идея":
        await update.message.reply_text("Сделай AI-бота для анализа PDF 🔥")

    elif text == "💬 Написать":
        await update.message.reply_text("Напиши что угодно — я отвечу!")

    else:
        await update.message.reply_text(f"Ты написал: {text}")

# Запуск
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()