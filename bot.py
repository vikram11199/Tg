import os
import requests
import asyncio
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8666830779:AAGaEn-Z3oDMQQ8vOM8NpdWOupbTdP0GEcY"
API = "https://ayaanmods.site/number.php?key=annonymous&number="

# -------- Web Server (Render ke liye) --------
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
# --------------------------------------------

# -------- Telegram Commands --------
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
            f"📡 Operator: {user.get('name','N/A')}\n"
            f"👤 Name: {user.get('address','N/A')}\n"
            f"👨 Father: {user.get('alternate','N/A')}\n"
            f"📱 Mobile: {user.get('mobile','N/A')}\n"
            f"📍 Location: {user.get('circle','N/A')}\n"
            f"📧 Email: {user.get('email','N/A')}\n"
            f"🆔 ID: {user.get('id','N/A')}\n"
            "━━━━━━━━━━━━━━\n"
        )

    await update.message.reply_text(msg)
# -------- Bot Start --------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

print("Bot Started...")

async def main():
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

asyncio.run(main())
