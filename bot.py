import requests
import asyncio
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

    results = data.get("result", [])

    if not results:
        await update.message.reply_text("No result found")
        return

    msg = ""

    for user in results:
        msg += (
            f"Name: {user.get('name')}\n"
            f"Father: {user.get('father_name')}\n"
            f"Mobile: {user.get('mobile')}\n"
            f"Address: {user.get('address')}\n"
            f"Circle: {user.get('circle')}\n"
            f"ID: {user.get('id')}\n"
            "--------------------\n"
        )

    await update.message.reply_text(msg)


async def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
