import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("Pʀᴇss 👉 /movies Fᴏʀ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\nPʀᴇss 👉 /series Fᴏʀ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Sᴇʀɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\n\nPʀᴇss 👉 /tutorial Fᴏʀ Tᴜᴛᴏʀɪᴀʟ Aʙᴏᴜᴛ Hᴏᴡ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Fʀᴏᴍ Mᴇ 🤗")

@Client.on_message(filters.command("credits", CMD))
async def help(_, message):
    await message.reply_text("Tʜɪs Is Cᴏᴅᴇᴅ Bʏ @Tamilan_BotsZ/n/Tʜᴀɴᴋs Tᴏ Eᴠᴀ Mᴀʀɪᴇ ﹝ ʙᴀsᴇ ᴄᴏᴅᴇ ﹞/n/nTʜɪs Is Aɴ Oᴩᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ Sᴏ Sᴜᴩᴩᴏʀᴛ Aɴᴅ Dᴏɴ´ᴛ Sᴇʟʟ Fᴏʀ Mᴏɴᴇʏ")

@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴀᴠᴀᴛᴀʀ: ᴛʜᴇ ᴡᴀʏ ᴏғ ᴡᴀᴛᴇʀ\n\n🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)\n\nᴄᴏᴅᴇᴅ ʙʏ ᴛᴀᴍɪʟᴀɴʙᴏᴛsᴢ")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n⚠️  MOVIES REQUEST TIPS »\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\n❤️Iғ Yᴏᴜ Wᴀɴᴛ A Mᴏᴠɪᴇ Jᴜsᴛ Tʏᴘᴇ Tʜᴇ Nᴀᴍᴇ ❤️\n彡Exᴀᴍᴘʟᴇs\n › Avatar ✔️\n Titanic ✔️\n› Avatar movie ❌\n› #Request Titanic ❌\n› Upload Avatar ❌\n\n❤️Iғ Tʜᴇʀᴇ Aʀᴇ Mᴀɴʏ Mᴏᴠɪᴇs Wɪᴛʜ Tʜᴇ Sᴀᴍᴇ Nᴀᴍᴇ Tʜᴇɴ Tʏᴘᴇ Yᴇᴀʀ ❤️\n彡 Exᴀᴍᴘʟᴇs \n› Avatar 2009 ✔️\n› Titanic 1997 ✔️\n\n❤️Iғ Mᴏᴠɪᴇ Nᴀᴍᴇ Is Lᴏɴɢ Mᴀᴋᴇ Iᴛ Sɪᴍᴘʟᴇ Iɴ Rᴇǫᴜᴇsᴛ ❤️\n彡 Exᴀᴍᴘʟᴇs \n› Last Night in Soho 2021 ❌\n› Soho 2021 ✔️\n› Godzilla vs Kong 2021 ❌\n› Kong 2021 ✔️\n\n❤️Iғ Yᴏᴜ Wᴀɴᴛ Sᴘᴇᴄɪғɪᴄ Lᴀɴɢᴜᴀɢᴇ Tʜᴇɴ Tʏᴘᴇ Lᴀɴɢᴜᴀɢᴇ Wɪᴛʜ Nᴀᴍᴇ❤️\n彡 Exᴀᴍᴘʟᴇs\n › Iron Man Tamil  ✔️\n› Iron Man English ✔️\n› Iron Man Tamil Dubbed  ❌\n› Iron Man In English ❌")

@Client.on_message(filters.command("tutorial", CMD))
async def tutorial(_, message):
    await message.reply_text("Tᴜᴛᴏʀɪᴀʟ Vɪᴅᴇᴏ 👉 https://t.me/tnlinkdown/6 \n\nFᴏʀ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ Tɪᴘs : <code>/ᴍᴏᴠɪᴇs</code>\n\nFᴏʀ Sᴇʀɪᴇs Rᴇǫᴜᴇsᴛ Tɪᴘs : <code>/sᴇʀɪᴇs</code>")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")
