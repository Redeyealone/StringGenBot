from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Aɴɪᴍᴇ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/doraemonbots"),
            InlineKeyboardButton(
                text="", url="https://github.com/AnonymousX1025/StringGenBot"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Aɴɪᴍᴇ 1", url=f"https://t.me/Dark_Support_Group"),
            InlineKeyboardButton(text="Aɴɪᴍᴇ 2", url=f"https://t.me/Dark_Support_Group"),
            InlineKeyboardButton('Close 🔐', callback_data='close')
     #       InlineKeyboardButton("Next ⏩", callback_data=f"navigate({index_val}|next|{query})"),
        ],
        [InlineKeyboardButton(text="VINCENZO", url=f"https://telegram.me/PublicFileStore01_Bot?start=PUBLIC_NjY1MQ==")],
    ]

       await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id



retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
