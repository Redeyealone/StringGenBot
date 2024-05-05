from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT

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

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ", url="https://github.com/AnonymousX1025/StringGenBot"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", url=SUPPORT_CHAT),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", url=SUPPORT_CHAT),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", url=SUPPORT_CHAT)],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
