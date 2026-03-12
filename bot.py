import requests
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "8666830779:AAGaEn-Z3oDMQQ8vOM8NpdWOupbTdP0GEcY"

API = "https://ayaanmods.site/number.php?key=annonymous&number="

def search(update, context):

    number = update.message.text.strip()

    try:
        r = requests.get(API + number)
        data = r.json()
    except:
        update.message.reply_text("API Error")
        return

    results = data.get("result", [])

    if not results:
        update.message.reply_text("No result found")
        return

    msg = ""

    for user in results:

        msg += f"""
Name : {user.get('name')}
Father : {user.get('father_name')}
Mobile : {user.get('mobile')}
Address : {user.get('address')}
Circle : {user.get('circle')}
ID : {user.get('id')}
--------------------
"""

    update.message.reply_text(msg)

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, search))

updater.start_polling()
updater.idle()