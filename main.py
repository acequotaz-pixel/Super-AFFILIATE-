import json
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start, tools, earn, handle_message
from scheduler import start_scheduler

with open("config/config.json") as f:
    config = json.load(f)

app = ApplicationBuilder().token(config["bot_token"]).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tools", tools))
app.add_handler(CommandHandler("earn", earn))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

start_scheduler(app)

print("PRO Bot running...")
app.run_polling()
