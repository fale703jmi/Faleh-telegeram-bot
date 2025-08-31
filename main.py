import requests
from telegram.ext import ApplicationBuilder, CommandHandler

import os
TOKEN = os.getenv("BOT_TOKEN")  # يقرأ التوكن من Environment Variables

# قائمة اليوزرات
watchlist = ["kze", "abc", "faleh123"]

def check_username(username):
    url = f"https://www.instagram.com/{username}/"
    r = requests.get(url)
    return r.status_code == 404

async def start(update, context):
    await update.message.reply_text("أرسل /snipe لفحص اليوزرات 🔍")

async def snipe(update, context):
    await update.message.reply_text("جاري فحص اليوزرات...")
    for user in watchlist:
        if check_username(user):
            await update.message.reply_text(f"✅ متاح الآن: {user}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("snipe", snipe))

    app.run_polling()

if __name__ == "__main__":
    main()
