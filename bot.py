import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Logging (VERY IMPORTANT for Render logs)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get token from environment
TOKEN = os.getenv("8648753740:AAHcWWwlO4U9-pXN69C4U5Cx1yQy0kSGp4A")

# Debug check (THIS WILL SHOW IN RENDER LOGS)
if not TOKEN:
    print("❌ ERROR: BOT_TOKEN is NOT set!")
else:
    print(f"✅ TOKEN LOADED: {TOKEN[:10]}...")  # show only part for safety

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is live and working!")

# Auto reply
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.lower()

        if "hello" in text:
            await update.message.reply_text("👋 Hey there!")
        elif "price" in text:
            await update.message.reply_text("💰 Check my Fiverr link here: https://yourlink.com")
        else:
            await update.message.reply_text("📩 Message received!")

    except Exception as e:
        logging.error(f"Error: {e}")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing. Check Render environment variables.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Bot is starting on Render...")
    app.run_polling()

if __name__ == "__main__":
    main()
