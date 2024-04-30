from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters


# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Telegram bot.")

# Define a function to handle regular messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(token='58e4e3aecb62907549a2a9f46c65489a', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Register a message handler to echo all messages
    echo_handler = MessageHandler(filters.text & (~filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
