import requests
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = "8666830779:AAGaEn-Z3oDMQQ8vOM8NpdWOupbTdP0GEcY"
API = "https://ayaanmods.site/number.php?key=annonymous&number="

# ---- simple web server ----
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    server.serve_forever()

threading.Thread(target=run_server).start()
# ---------------------------


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send mobile number")


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    number = update.message.text.strip()

    try:
        r = requests.get(API + number)
        data = r.json()
    except:
        await update.message.reply_text("API Error")
        return

    results = data.get("result", [])

    if not results:
        await update.message.reply_text("No result")
        return

    msg = ""
    for user in results:
        msg += f"{user.get('name')} - {user.get('mobile')}\n"

    await update.message.reply_text(msg)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

print("Bot Started")

app.run_polling()
