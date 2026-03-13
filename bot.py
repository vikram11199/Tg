import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8666830779:AAGaEn-Z3oDMQQ8vOM8NpdWOupbTdP0GEcY"
API = "https://ayaanmods.site/number.php?key=annonymous&number="


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    number = update.message.text.strip()

    try:
        r = requests.get(API + number, timeout=10)
        data = r.json()
    except:
        await update.message.reply_text("API Error")
        return

    if not data:
        await update.message.reply_text("No result found")
        return

    msg = ""

    for user in data:
        msg += f"""
Name : {user.get('name')}
Father : {user.get('father_name')}
Mobile : {user.get('mobile')}
Address : {user.get('address')}
Circle : {user.get('circle')}
ID : {user.get('id')}
--------------------
"""

    await update.message.reply_text(msg)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    print("Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
