from telegram.ext import Updater, CommandHandler

TOKEN = "YOUR_BOT_TOKEN"

def username_search(update, context):
    if not context.args:
        update.message.reply_text("Use: /username ram123")
        return

    user = context.args[0]
    found = False
    result = []

    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == f"username: {user}":
                found = True
                result.append(line)
                continue
            if found and line.strip() == "---":
                break
            if found:
                result.append(line)

    if result:
        update.message.reply_text("".join(result))
    else:
        update.message.reply_text("❌ Username nahi mila")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("username", username_search))

updater.start_polling()
updater.idle()
