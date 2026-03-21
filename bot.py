import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

TOKEN = "8666830779:AAGaEn-Z3oDMQQ8vOM8NpdWOupbTdP0GEcY"

API = "https://ayaanmods.site/number.php?key=annonymous&number="


def num(update, context):

    if len(context.args) == 0:
        update.message.reply_text("❌ Example:\n/num 8292929929")
        return

    number = context.args[0]

    try:
        r = requests.get(API + number)
        data = r.json()
    except:
        update.message.reply_text("⚠️ API Error")
        return

    results = data.get("result", [])

    if not results:
        update.message.reply_text("❌ No Result Found")
        return

    msg = f"""
╭━━━〔 🔎 NUMBER LOOKUP 〕━━━╮

📱 <b>Search Number</b>
<code>{number}</code>

━━━━━━━━━━━━━━━━━━━━
"""

    for user in results:

        msg += f"""
👤 <b>Name</b>      : <code>{user.get('name')}</code>
👨 <b>Father</b>    : <code>{user.get('father_name')}</code>
📞 <b>Mobile</b>    : <code>{user.get('mobile')}</code>
📍 <b>Address</b>   : <code>{user.get('address')}</code>
🌐 <b>Circle</b>    : <code>{user.get('circle')}</code>
🆔 <b>ID</b>        : <code>{user.get('id')}</code>

━━━━━━━━━━━━━━━━━━━━
"""

    msg += """
🤖 <b>BOT :</b> Number Information Service
╰━━━━━━━━━━━━━━━━━━━━╯
"""

    keyboard = [
        [
            InlineKeyboardButton("📢 Join Channel", url="https://t.me/YOUR_CHANNEL")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(msg, parse_mode="HTML", reply_markup=reply_markup)


updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("num", num))

print("Bot Running...")

updater.start_polling()
updater.idle()