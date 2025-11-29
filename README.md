# ─「<u>Lɪɴᴋ sʜᴀʀᴇ ʙᴏᴛ</u>」─

<p align="center">
  <img src="assets/img.jpg" alt="Bot Channels" width="1920"/>
</p>

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=THIS+IS+A+ADVANCE+LINK+SHARE!+BOT;CREATED+BY+REX+BOTS)</p>
</p>

<b><i>A powerful and dynamic Telegram bot designed to share links from specific channels, protecting them from copyright issues. It features a fully interactive, button-based UI and can be configured dynamically by the owner.</i></b>

---

## 🚀 Features

-   **Advanced Link Sharing:** _Securely share links from your channels._
-   **FORCE SUBSCRIBE:** _Ensure users join designated channels before they can access links._
-   **Button-Based UI:** _Modern, easy-to-use interface with inline buttons instead of text commands._
-   **Dynamic Content:** _Rich messages with images and styled text using blockquotes._
-   **In-Bot Configuration:** _The bot owner can manage all important settings directly from the bot's UI._
-   **Secure:** _No hardcoded credentials. All sensitive information is loaded from environment variables._

---

## 🤖 Bot Commands

```
/start - Sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ 
/settings - Tᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙᴏᴛ sᴇᴛᴛɪɴɢs ᴅʏɴᴀᴍɪᴄᴀʟʟʏ (ᴀᴅᴍɪɴ)
/genlink - Tᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋs sɪɴɢʟᴇ (ᴀᴅᴍɪɴ)
/batch - Tᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋs ɪɴ ᴀ ʙᴀᴛᴄʜ (ᴀᴅᴍɪɴ)
/broadcast - Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ Yᴏᴜʀ ᴍᴇssᴀɢᴇ (ᴀᴅᴍɪɴ)
```

---

## 🛠️ How to Deploy

_You can easily deploy this bot yourself. Follow the steps below._

### **Prerequisites**

-   _A Telegram Bot Token. Get one from [@BotFather](https://t.me/BotFather)._
-   _Your Telegram API ID and API Hash. Get them from [my.telegram.org](https://my.telegram.org)._
-   _A MongoDB database URL. Get one for free from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)._

### **Deployment Steps**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/abhinai2244/LINK-SHAREBOT.git
    cd LINK-SHAREBOT
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables:**
    Create a `.env` file in the root directory or set the following environment variables in your deployment environment:

    | Variable           | Description                                             |
    | ------------------ | ------------------------------------------------------- |
    | `TG_BOT_TOKEN`     | Your Telegram bot token from @BotFather.                |
    | `API_ID`           | Your Telegram App ID.                                   |
    | `API_HASH`         | Your Telegram App Hash.                                 |
    | `DB_URI`           | Your MongoDB connection URL.                            |
    | `OWNER_ID`         | Your numerical Telegram User ID.                        |
    | `DATABASE_CHANNEL` | The ID of the channel where the bot will send logs/notifications. |

    **Optional Variables:**
    You can customize the bot further with these optional variables: `DB_NAME`, `START_PIC`, `FSUB_PIC`, `HELP_PIC`, etc.

4.  **Run the bot:**
    ```bash
    python3 bot.py
    ```

---

## Credits:-

_This bot was made possible with the help and support of the following individuals:_

-   **[ABHINAI](https://t.me/about_zani)**
-   **[ABHINAV](https://t.me/adityaabhinav)**
-   **[MASTER](https://t.me/V_Sbotmaker)**

- **[REx BOTs](https://t.me/RexBots_Official)**

- **Base Repo**:- **[CodeFlix](https://github.com/Codeflix-Bots/Links-Share-Bot.git)**
---
