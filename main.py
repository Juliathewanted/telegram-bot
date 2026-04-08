import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

def load_list(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except:
        return []
    
ideas = load_list("ideas.txt")
compliments = load_list("compliments.txt")
ideas_pool = []
compliments_pool = []

def get_random_item(main_list, pool):
    if not pool:
        pool.extend(main_list)
        random.shuffle(pool)
    return pool.pop()

# Старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚨 ЭТО ТОЧНО НОВАЯ ВЕРСИЯ 🚨")
    keyboard = [
    ["📄 Помощь", "🔥 Идея"],
    ["💬 Написать", "✨ Комплимент дня"]
]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Привет 👋\nЯ твой первый бот.\nВыбери, что сделать:",
        reply_markup=reply_markup
    )

# Ответы на кнопки
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "Помощь" in text:
        await update.message.reply_text("Я первый тестовый бот Юли, нажми на кнопки и увидишь что будет 😎")

    elif "Идея" in text:
        if ideas:
            idea = get_random_item(ideas, ideas_pool)
            await update.message.reply_text(f"💡 {idea}")
        else:
            await update.message.reply_text("Идей пока нет")

    elif "Комплимент" in text:
        if compliments:
            compliment = get_random_item(compliments, compliments_pool)
            await update.message.reply_text(f"✨ {compliment}")
        else:
            await update.message.reply_text("Комплиментов пока нет")

    elif "Написать" in text:
        await update.message.reply_text("Напиши что угодно — я отвечу!")

    else:
        await update.message.reply_text(f"Ты написал: {text}")

# Запуск
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
