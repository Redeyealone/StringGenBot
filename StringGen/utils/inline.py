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
        ],
        [InlineKeyboardButton(text="Jᴜɪᴜᴛsᴜ ᴋᴀɪsᴇɴ", url=f"https://t.me/Jujustu_Kaisen_Season_2_Hindi")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
