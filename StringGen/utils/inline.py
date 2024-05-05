import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Define the command handler for the /start command
def start(update, context):
    reply_markup = create_inline_keyboard()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.", reply_markup=reply_markup)

# Define the callback handler for inline keyboard button clicks
def button_callback(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'next':
        context.bot.send_message(chat_id=query.message.chat_id, text="Next button clicked!")
    elif query.data == 'previous':
        context.bot.send_message(chat_id=query.message.chat_id, text="Previous button clicked!")

# Create the inline keyboard
def create_inline_keyboard():
    keyboard = [
        [InlineKeyboardButton("Previous", callback_data='previous'),
         InlineKeyboardButton("Next", callback_data='next')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Create an Updater and attach the handlers
updater = Updater(token='6571094339:AAGcENp3AmPPJslc88ERGsT_VdJ20hKTtvQ', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

button_handler = CallbackQueryHandler(button_callback)
dispatcher.add_handler(button_handler)

# Start the bot
updater.start_polling()
