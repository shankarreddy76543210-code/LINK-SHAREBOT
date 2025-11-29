import os
import asyncio
from bot import Bot
from config import *
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, ChatAdminRequired, UserNotParticipant, UserAlreadyParticipant
from helper_func import *

AUTO_APPROVE_ENABLED = True

@Client.on_chat_join_request((filters.group | filters.channel))
async def auto_approve(client: Bot, message: ChatJoinRequest):
    global AUTO_APPROVE_ENABLED
    chat = message.chat
    user = message.from_user
    print(f"{user.first_name} requested to join {chat.title}")
    
    await asyncio.sleep(2)
    
    # Check if user is already a participant before approving
    try:
        member = await client.get_chat_member(chat.id, user.id)
        if member.status in ["member", "administrator", "creator"]:
            print(f"User {user.id} is already a participant of {chat.id}, skipping approval.")
            return
    except UserNotParticipant:
        # User is not a participant, proceed with approval
        pass
    except Exception as e:
        print(f"Error checking membership: {e}")
        return
    
    # Approve the join request
    try:
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        print(f"Approved join request for {user.first_name} ({user.id})")
    except UserAlreadyParticipant:
        print(f"User {user.id} is already a participant.")
        return
    except Exception as e:
        print(f"Error approving join request: {e}")
        return
    
    # Send welcome message with invite link
    try:
        invite_link = await client.export_chat_invite_link(chat.id)
        buttons = [
            [InlineKeyboardButton('• Cʟɪᴄᴋ ʜᴇʀᴇ •', url=invite_link)]
        ]
        markup = InlineKeyboardMarkup(buttons)
        caption_approve_ka = (
            f"<b>⁉️ Bᴀᴋᴀᴀᴀ!!!... {user.mention}</b>,\n\n"
            f"<b><blockquote>ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {chat.title} ʜᴀs ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ ᴀᴅᴍɪɴ/ᴏᴡɴᴇʀ.</blockquote></b>"
        )
        
        await client.send_photo(
            chat_id=user.id,
            photo='https://ibb.co/mVkSySr7',
            caption=caption_approve_ka,
            reply_markup=markup
        )
        print(f"Sent welcome message to {user.first_name} ({user.id})")
    except Exception as e:
        print(f"Error sending welcome message: {e}")
