#Coded By @JonSnow11
class script(object):
    START_TXT = """<b> Hᴇʟʟᴏ {}</b> 😁
    
ɪ ᴀᴍ ᴀ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ + ᴍᴏᴠɪᴇ sᴇᴀʀᴄʜ + ᴍᴀɴᴜᴀʟ ꜰɪʟᴛᴇʀ ʙᴏᴛ. ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs. ʏᴏᴜ ᴄᴀɴ sᴇᴀʀᴄʜ ᴍᴏᴠɪᴇs ᴠɪᴀ ɪɴʟɪɴᴇ. ɪ ᴄᴀɴ ᴀʟsᴏ ᴀᴅᴅ ꜰɪʟᴛᴇʀs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ😌"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""

    ABOUT_TXT = """<b><i>👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/JonSnow11><b>ᴊᴏɴ sɴᴏᴡ</b></a>\n
📝 ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org><b>ᴘʏᴛʜᴏɴ</b></a>\n
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : <a href=https://github.com/pyrogram/pyrogram><b>ᴘʏʀᴏɢʀᴀᴍ</b></a>\n
📡 ʜᴏsᴛᴇᴅ ᴏɴ : <a href=heroku.com><b>ʜᴇʀᴏᴋᴜ</b></a>\n
👥 sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/RolexMoviesOX><b>ʀᴏʟᴇx ᴄᴏᴍᴍᴜɴɪᴛʏ</b></a>\n
"""

    SOURCE_TXT = """<b>Hᴇʀᴇ ɪs ᴛʜᴇ Exᴛʀᴀ Pᴏᴡᴇʀғᴜʟ Fᴇᴀᴛᴜʀᴇs 🥂</b>"""

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/MrperfectOffcial)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>
<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    EARN_TXT = """𝟭. 𝗠𝗔𝗞𝗘 𝗦𝗨𝗥𝗘 𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗛𝗔𝗦 𝟭𝟬𝟬+ 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 !!!

𝟮. 𝗔𝗗𝗗 𝗕𝗢𝗧 𝗧𝗼 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗪𝗜𝗧𝗛 𝗙𝗨𝗟𝗟 𝗔𝗗𝗠𝗜𝗡 𝗥𝗜𝗚𝗛𝗧𝗦

𝟯. 𝗔𝗙𝗧𝗘𝗥 𝗔𝗗𝗗𝗜𝗡𝗚 𝗜𝗡 𝗚𝗥𝗢𝗨𝗣, 𝗖𝗥𝗘𝗔𝗧𝗘 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗜𝗡 𝗔𝗡𝗬 𝗨𝗥𝗟 𝗦𝗛𝗢𝗥𝗧𝗡𝗘𝗥 𝗪𝗘𝗕𝗦𝗜𝗧𝗘

𝗠𝗬 𝗦𝗨𝗚𝗚𝗘𝗦𝗧𝗜𝗢𝗡(𝗖𝗣𝗠 𝟳+) : <a href='https://tnshort.net/ref/Bharathraj'>𝗧𝗡𝗦𝗛𝗢𝗥𝗧.𝗡𝗘𝗧</a>

𝟰. 𝗔𝗙𝗧𝗘𝗥 𝗠𝗔𝗞𝗜𝗡𝗚 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗜𝗡 𝗦𝗛𝗢𝗥𝗧𝗡𝗘𝗥 𝗪𝗘𝗕𝗦𝗜𝗧𝗘 𝗦𝗘𝗡𝗗 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣


—> /𝗦𝗛𝗢𝗥𝗧𝗟𝗜𝗡𝗞 𝗬𝗢𝗨𝗥_𝗦𝗛𝗢𝗥𝗧𝗘𝗡𝗘𝗥_𝗪𝗘𝗕𝗦𝗜𝗧𝗘_𝗡𝗔𝗠𝗘 (𝗬𝗢𝗨𝗥_𝗦𝗛𝗢𝗥𝗧𝗡𝗘𝗥_𝗔𝗣𝗜)

#𝗘𝗫𝗔𝗠𝗣𝗟𝗘:-

/𝗦𝗛𝗢𝗥𝗧𝗟𝗜𝗡𝗞 𝗧𝗡𝗦𝗛𝗢𝗥𝗧.𝗡𝗘𝗧 𝗕𝟲𝗔𝗔𝗖𝗘𝟰𝟲𝗗𝟰𝟬𝗖𝟲𝟬𝟱𝗙𝗙𝗙𝟴𝗘𝗢𝗖𝗔𝗙𝗕𝗖𝗗𝟴𝗙𝗕𝗘𝟰𝟭𝟲𝟴𝟱𝟭𝗙𝟰𝗗

𝟱. 𝗔𝗗𝗗 𝗠𝗢𝗥𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗧𝗼 𝗘𝗔𝗥𝗡 𝗠𝗢𝗡𝗘𝗬"""

    ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.</code>"""

    STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """#NᴇᴡGʀᴏᴜᴘ
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NᴇᴡUsᴇʀ
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """🔆 Hey {}, Its Not For You❗"""

    OLD_ALRT_TXT = """🔆 Hey {}, ❗Link Expired, Please Request Again ♻"""

    CUDNT_FND = """<b><i>⚠ No Results, Please Follow Request Tips !!</i></b> \n <b><i>♀ Request Tips › [Click Here](https://t.me/c/1637849188/118909)</i></b>"""

    I_CUDNT = """<b><i>⚠ No Results, Please Follow Request Tips !!</i></b> \n <b><i>♀ Request Tips › [Click Here](https://t.me/c/1637849188/118909)</i></b>"""

    I_CUD_NT = """<b><i>⚠ No Results, Please Follow Request Tips !!</i></b> \n <b><i>♀ Request Tips › [Click Here](https://t.me/c/1637849188/118909)</i></b>"""

    MVE_NT_FND = """<b><i>⚠ No Results, Please Follow Request Tips !!</i></b> \n <b><i>♀ Request Tips › [Click Here](https://t.me/c/1637849188/118909)</i></b>"""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ 1 Million Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : ᴊᴏɴ sɴᴏᴡ
• ᴜꜱᴇʀɴᴀᴍᴇ : JonSnow11
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/JonSnow11'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""

    REQINFO = """
Check Your Spelling, Release Date, If You Still Don't Get The Movie Then Type Like This...
⊱⋅ ──────────────────── ⋅⊰
 #Request Avatar 2009 720p
 
Owner Will Update The Movie Within 24Hour"""

    MINFO = """
⚠ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs ⁉️ »
⊱⋅ ─────────────── ⋅⊰
› Avatar ✅
› Avatar 2009 720p ✅
› Avatar 2009 720p Tamil ✅

› Don't Type Movie, Upload, Please, Symbol ❌
"""

    SINFO = """
⚠ How To Request Series ⁉️ »
⊱⋅ ─────────────── ⋅⊰
› Flash S01 ✅
› Flash Tamil ✅
› Flash S01E02 Tamil ✅

› Don't Type Movie, Upload, Please, Symbol ❌
"""

    NORSLTS = """
★ #Aᴜᴛᴏ_Rᴇǫᴜᴇsᴛ ★

♦️ <b>Usᴇʀ_ID</b> : `{}`
♦️ <b>Rᴇǫᴜᴇsᴛᴇᴅ Bʏ : {}</b>
🔆 <b>Rᴇǫᴜᴇsᴛ</b> : 🎗️`{}`🎗️ """

    CAPTION = """
ɴᴀᴍᴇ : <code>{file_name}</code> \n\nɴᴏᴛᴇ: ᴀꜰᴛᴇʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ꜰɪʟᴇꜱ, ꜱᴀᴠᴇ ᴛʜᴇ ꜰɪʟᴇ ᴛᴏ ɢᴀʟʟᴇʀʏ ᴀɴᴅ ᴄʟɪᴄᴋ ᴛʜᴇ ᴅᴇʟᴇᴛᴇ ʙᴜᴛᴛᴏɴ, ᴅᴏɴ'ᴛ ᴄʟɪᴄᴋ ʙᴇꜰᴏʀᴇ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ꜰɪʟᴇꜱ"""

    IMDB_TEMPLATE_TXT = """<i>IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 </i>"""
    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>⏰Tɪᴍᴇ : <code>{}</code>

🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>TamilNadua</code></b>"""
    
    TELE_TXT = """<b>»HELP: Tᴇʟᴇɢʀᴀᴘʜ▪️

Dᴏ ᴀs ʏᴏᴜ ᴡɪsʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀ.ᴘʜ ᴍᴏᴅᴜʟᴇ!

USAGE:

🤧 /ᴛᴇʟᴇɢʀᴀᴘʜ - Sᴇɴᴅ ᴍᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ Pɪᴄᴛᴜʀᴇ ᴏʀ Vɪᴅᴇ Uɴᴅᴇʀ (𝟻MB) 

NOTE:

• Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Aᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢᴏᴜᴘs ᴀɴᴅ ᴘᴍs
• Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ</b>"""
    
    YTDL_TXT = """<b>»YOUTUBE DOWNLOAD MODULE</b>

🍁Usᴀɢᴇ : Yᴏᴜ Cᴀɴ Dᴏᴡɴʟᴏᴀᴅ Aɴʏ Vɪᴅᴇᴏ Oʀ Aᴜᴅɪᴏ Fʀᴏᴍ Yᴏᴜᴛᴜʙᴇ

» Hᴏᴡ Tᴏ Usᴇ
• Isᴏɴɢ SONG NAME
• /ᴠɪᴅᴇᴏ ᴏʀ /ᴍᴘ𝟺 Aɴᴅ ʜᴛᴛᴘs://ʏᴏᴜᴛᴜ.ʙᴇ/*****

• Exᴀᴍᴘʟᴇ:

<ᴄᴏᴅᴇ>/sᴏɴɢ RXM</ᴄᴏᴅᴇ>
<ᴄᴏᴅᴇ>/ᴍᴘ𝟺 ʜᴛᴛᴘs://ʏᴏᴜᴛᴜ.ʙᴇ/*******</ᴄᴏᴅᴇ>
<ᴄᴏᴅᴇ>/ᴠɪᴅᴇᴏ ʜᴛᴛᴘs://ʏᴏᴜᴛᴜ.ʙᴇ/*****</ᴄᴏᴅᴇ>"""
    
    FOND_TXT = """<b>« HELP FOR FONTS »
FONT IS A MODULE FOR MAKE YOUR TEXT STYLISH.
FOR USE THAT FEUTURE TYPE /ғᴏɴᴛ <ʏᴏᴜʀ ᴛᴇxᴛ> THEN YOUR TEXT IS READY.</b>"""
    
    TTS_TXT = """Hᴇʟᴘ: <b> TTS 🎤 ᴍᴏᴅᴜʟᴇ:</b>

Tʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>

• /ᴛᴛs <ᴛᴇxᴛ> : ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ

<b>NOTE:</b>

• IMDʙ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• IMDʙ ᴄᴀɴ ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛs ᴛᴏ 𝟸𝟶𝟶+ ʟᴀɴɢᴜᴀɢᴇs."""
    
    
    IMAGE_TXT = """➤ 𝐇𝐞𝐥𝐩: Iᴍᴀɢᴇ

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ ᴇᴅɪᴛ ɪᴍᴀɢᴇ Vᴇʀʏ ᴇᴀsɪʟʏ

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ Jᴜsᴛ Sᴇɴᴅ ᴍᴇ ᴀ ɪᴍᴀɢᴇ ᴛᴏ ᴇᴅɪᴛ ✨"""
    
    CARB_TXT = """☾𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗖𝗔𝗥𝗕𝗢𝗡☽
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /ᴄᴀʀʙᴏɴ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""
