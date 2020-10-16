import time
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from ..app import app


@app.on_message(filters.command("ping"))
async def ping(_, message: Message):
    """Ping the assistant"""
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    pong = delta_ping * 1000:.3f
    await reply.edit_text(f"🏓 <b>Pong!</b> <code>{pong} ms</code>")
