class script(object):
    START_TXT = """𝐇𝐄𝐋𝐋𝐎 {}🌝❤️‍🔥 
\n𝐈 𝐂𝐀𝐍 𝐏𝐑𝐎𝐕𝐈𝐃𝐄 𝐌𝐎𝐕𝐈𝐄𝐒 & 𝐒𝐄𝐑𝐈𝐄𝐒 𝐀𝐒 𝐏𝐄𝐑 𝐘𝐎𝐔𝐑 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐈𝐍 𝐆𝐑𝐎𝐔𝐏 🙃❤️‍🔥   \n𝐉𝐔𝐒𝐓 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 & 𝐄𝐍𝐉𝐎𝐘 🥳🎉"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✿  𝙼𝚈 𝙽𝙰𝙼𝙴: {}
\n✿  𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/ABHINAND3510>A҉B҉H҉I҉N҉A҉N҉D҉</a>
\n✿  𝙻𝙸𝙱𝚁𝙰𝚁𝚈 & 𝙻𝙰𝙽𝙶: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 | 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
\n✿  𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 & 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙼𝙾𝙽𝙶𝙾𝙳𝙱 | 𝙷𝙴𝚁𝙾𝙺𝚄
\n✿  𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Source - https://t.me/thefilmyspot
<b>DEVS:</b>
- <a href=https://t.me/thefilmyspotin>🌝🤍</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message
<b>NOTE:</b>
1. should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
-Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/thefilmyspotbot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message Hehe😆)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my database ."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Bot🌝🏷️
<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my Admins😼
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code> 📈
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙶𝚁𝙾𝚄𝙿𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser 🌝🤍
ID - <code>{}</code>
Name - {}
"""
ALRT_TXT = """ Hey {} 🙂,
This is Not Your ReQuest ,

Please Send The Movie/ Series Name You Want ! ..."""

OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 

ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""


    CUDNT_FND = """NOT FOUND ANYTHING RELATED TO /n{}
/nCHOOSE ANY NAME BELOW 👇🏼!
"""

I_CUDNT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {} 
Choose Any Name Given Below 👇🏼"""

I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.

ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ..."""

MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ 𝐭𝐡𝐞𝐟𝐢𝐥𝐦𝐲𝐬𝐩𝐨𝐭 ᴅᴀᴛᴀʙᴀꜱᴇ ...

Please Check The Name On Google & Check That Title is Released ( OTT / DVD )......."""

TOP_ALRT_MSG = """𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐦𝐨𝐯𝐢𝐞 𝐢𝐧 𝐭𝐡𝐞𝐟𝐢𝐥𝐦𝐲𝐬𝐩𝐨𝐭 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 💿..."""

MELCOW_ENG = """HELLO {MENTION}🌝❤️

WELCOME TO {GROUPNAME} 😻🥂 

THANKS FOR JOINING &
 KEEP SUPPORTING US 🤍🙌🏻.

Join our <a href='https://t.me/thefilmyspotin'>main channel</a> below to get access to the movies. Before requesting the movies, Must join our main channel. Only by joining will you get access to all the movies...

NB: You can only get the movie by typing in the correct spelling...

If you do not get the Movie / Series, mention the admin in the following format 👇

🤷 Example: @admin Avatar 2009 English 
            @admin Breaking Bad S05E07
Wᴇ Dᴏ Nᴏᴛ Oᴡɴ Aɴʏ Cᴏɴᴛᴇɴᴛ Pᴏsᴛᴇᴅ Hᴇʀᴇ. Wᴇ Oɴʟʏ Sʜᴀʀᴇ Tʜᴏsᴇ Fɪʟᴇs Wʜɪᴄʜ Aʀᴇ Aʟʀᴇᴀᴅʏ Sʜᴀʀᴇᴅ Bʏ Sᴏᴍᴇʙᴏᴅʏ Eʟsᴇ Oɴ Tʜᴇ Iɴᴛᴇʀɴᴇᴛ

⚠️ Iꜰ Yᴏᴜ Oᴡɴ Tʜᴇ Cᴏᴘʏʀɪɢʜᴛs Oꜰ Aɴʏ Sᴛᴜꜰꜰ, Iɴᴛɪᴍᴀᴛᴇ Us Wɪᴛʜ Pʀᴏᴏꜰ Wᴇ Wɪʟʟ Rᴇᴍᴏᴠᴇ

Do not contact Admin directly...

If you want to contact Admin, Please send the message to @thefilmyspothelpbot and the bot will deliver the message to the group Admin...

<a href='https://t.me/thefilmyspothelpbot'>If you are facing any problems with our movie files, bots or groups, report it in our Feedback Bot : @thefilmyspothelp</a>

For admin support type @admins with your message and the bot will forward the message to the admin...</b>"""

OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : A҉B҉H҉I҉N҉A҉N҉D҉
• ᴜꜱᴇʀɴᴀᴍᴇ : @Abhinand3510
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/abhinand3510'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""

