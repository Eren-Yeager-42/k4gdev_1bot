from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
import random
import os

TOKEN = os.getenv(8670896395:AAGQM-LstfFMpqkv59Jtdu-LfNg7QfnG4SU)

# ✅ Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I am K4G Bot")

# 🤖 Smart + random reply
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "hi" in text:
        response = "Hello 👋"
    elif "bye" in text:
        response = "Goodbye 👋"
    elif "how are you" in text:
        response = "I'm fine 😄"
    else:
        response = random.choice([
            "Nice 👍",
            "Hmm 🤔",
            "Lol 😂"
        ])

    await update.message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()

# ✅ Add BOTH handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
