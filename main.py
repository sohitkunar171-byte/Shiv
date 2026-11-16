import os
from telegram.ext import ApplicationBuilder, CommandHandler
async def start(update, context):
              await update.message.reply_text("Bot is active!")
if __name__ == '__main__':
    application = ApplicationBuilder().token("9064919172:AAG4EitoqS-j2q0M7XMUNozLSa0J_GzRyaY").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
