from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "YOUR TELEGRAM TOKEN"
Bot_username: Final = "@PyTelegrambot"


# COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, thanks for chatting with me. ")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a telegram Bot! i will try to answer your questions. ")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")


def handle_responses(text: str) -> str:
    processed: str = text.lower()
    salute = ["ok", "leave", "bye", "good bye", "see you", "later"]
    if "hello" in processed:
        return "Hi There"

    if "how are you" in processed:
        return "I'm fine, Thank You"

    if "I love python" in processed:
        return """that's great!, 
there are free recourses on Youtube, you can learn there"""

    if "hi" in processed:
        return "Hello!, how are you"

    if "what is your name" in processed:
        return "I am a simple telegram Bot intended for research"

    if "what can you do" in processed:
        return "What any other Bot can do Obviously!"

    if any(salute in processed for salute in salute):
        return "Nice Chatting with you! see you later."

    return """I do not understand what you wrote....
try googling it. Thank You"""


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User: ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == "group":
        if Bot_username in text:
            new_text: str = text.replace(Bot_username, "").strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses(text)

    print("Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"update: {update} caused the following error, {context.error}")


if __name__ == "__main__":
    print("Starting Bot....")
    app = Application.builder().token(TOKEN).build()

    # COMMANDS
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # ERROR
    app.add_error_handler(error)

    # check for updates
    # poll the bot
    print("Polling...")
    app.run_polling(poll_interval=5)  # for 5 seconds
