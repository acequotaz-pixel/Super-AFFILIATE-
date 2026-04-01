from ai_engine import generate_ai_response
from monetization import get_tools_message

async def start(update, context):
    await update.message.reply_text("Welcome to PRO AI Income Bot!")

async def tools(update, context):
    await update.message.reply_text(get_tools_message())

async def earn(update, context):
    await update.message.reply_text("Earn using AI tools and VIP system.")

async def handle_message(update, context):
    response = generate_ai_response(update.message.text)
    response += "\n\nUpgrade to VIP coming soon."
    await update.message.reply_text(response)
