from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client , filters




@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
    text = """**Free Plan User**
Daily  Upload limit 2GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 49  ind /🌎 0.59$  per Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 99  ind /🌎 1.19$  per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 149  ind /🌎 2.16$  per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>akkumundro@okicici</code>
<b>➜ QR Code :</b> <a href='https://i.ibb.co/VYDtjjhd/image.jpg'>Click Here</a>

After Payment Send Screenshots Of Payment To Admin @ags_mods_bot"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/ags_mods_bot"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await update.message.edit(text = text,reply_markup = keybord, disable_web_page_preview=True)
    
    

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
    text = """**Free Plan User**
Daily  Upload limit 2GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 49  ind /🌎 0.59$  per Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 99  ind /🌎 1.19$  per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 179  ind /🌎 2.16$  per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>akkumundro@okicici</code>
<b>➜ QR Code :</b> <a href='https://i.ibb.co/VYDtjjhd/image.jpg'>Click Here</a>

After Payment Send Screenshots Of Payment To Admin @ags_mods_bot"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/ags_mods_bot"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await message.reply_text(text=text, reply_markup=keybord, quote=True, disable_web_page_preview=True)
    
	
    
    
    
# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper & @ags_mods_bot
