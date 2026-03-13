import os
import requests
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8666830779:AAGaEn-Z3oDMQQ8vOM8NpdWOupbTdP0GEcY"
API = "https://ayaanmods.site/number.php?key=annonymous&number="

# -------- Render ke liye Web Server --------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_server).start()
# ------------------------------------------


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Mobile number bhejo aur detail pao"
    )


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    number = update.message.text.strip()

    if not number.isdigit():
        await update.message.reply_text("❌ Valid mobile number bhejo")
        return

    try:
        r = requests.get(API + number, timeout=10)
        data = r.json()
    except:
        await update.message.reply_text("⚠️ API Error")
        return

    results = data.get("result", [])

    if not results:
        await update.message.reply_text("❌ No result found")
        return

    msg = ""

    for user in results:
        msg += (
            f"👤 Name: {user.get('name')}\n"
            f"👨 Father Name: {user.get('father_name')}\n"
            f"📱 Mobile: {user.get('mobile')}\n"
            f"📍 Address: {user.get('address')}\n"
            f"🌐 Circle: {user.get('circle')}\n"
            f"🆔 ID: {user.get('id')}\n"
            f"📅 DOB: {user.get('dob')}\n"
            f"📧 Email: {user.get('email')}\n"
            f"🪪 Aadhaar: {user.get('aadhar')}\n"
            "━━━━━━━━━━━━━━\n"
        )

    await update.message.reply_text(msg)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

print("Bot Started...")

app.run_polling()
