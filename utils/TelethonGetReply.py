from telethon import TelegramClient
from telethon.tl.types import Message
import asyncio

async def get_reply(bot: TelegramClient, event: Message) ->  Message:
     """
    Waits for user reply in private chat.
    Uses recursion to except TimeoutError.
    
    :param bot: Bot client or user client.
    :param event: Update event to extract chat and user.
    :return: Telethon Message.
    """
    try:
        async with bot.conversation(event.chat_id) as conv:
            handle = conv.wait_event(events.NewMessage(chats=event.chat_id, from_users=event.chat_id))
            return await handle
    except asyncio.TimeoutError:
        return await get_reply(event)
