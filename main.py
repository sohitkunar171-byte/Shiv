import os
from telegram.ext import ApplicationBuilder, CommandHandler
async def start(update, context):
              await update.message.reply_text("Bot is active!")
if __name__ == '__main__':
    application = ApplicationBuilder().token("YOUR_TOKEN").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
