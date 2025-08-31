import os, requests
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ["BOT_TOKEN"]  # التوكن من متغير البيئة

watchlist = ["kze", "abc", "faleh123"]

def check_username(username):
    url = f"https://www.instagram.com/{username}/"
    r = requests.get(url)
    return r.status_code == 404

def start(update, context):
    update.message.reply_text("أرسل /snipe لفحص اليوزرات 🔎")

def snipe(update, context):
    update.message.reply_text("جاري فحص اليوزرات...")
    for user in watchlist:
        if check_username(user):
            update.message.reply_text(f"✅ متاح الآن: {user}")
        else:
            update.message.reply_text(f"❌ محجوز: {user}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("snipe", snipe))
    print("Bot is up. Polling…")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
