import json
import requests
from pyrogram import filters
from ..app import app
from pyrogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    Message
)

AUTH_USERS = [12345678, 12345678] # add user id of people who can use this bot

API = "https://meme-api.herokuapp.com/gimme"


@app.on_message(filters.command(["meme", "meme@redditx_bot"]) & filters.user(AUTH_USERS))
async def meme_(_, message: Message):
    """Random reddit post"""
    caption, subreddit, postlink, image = reddit_post(API)
    buttons = [[InlineKeyboardButton(text=f"Source: r/{subreddit}", url=postlink)]]          
    await message.reply_photo(
        image,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_message(filters.user(AUTH_USERS) & filters.incoming & filters.regex(pattern=r"^\/(?:sub|sub@redditx_bot)(?: )(.+)"))
async def subreddit_(_, message: Message):
    """ get post from specific subreddit """
    sub_r = message.matches[0].group(1)
    subreddit_api = f"{API}/{sub_r}"
    try:
        caption, subreddit, postlink, image = reddit_post(subreddit_api)
    except:
        return
    buttons = [[InlineKeyboardButton(text=f"Source: r/{subreddit}", url=postlink)]]          
    await message.reply_photo(
        image,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


def reddit_post(api):
    try:
        cn = requests.get(api)
        r = cn.json()
    except ValueError:
        return
    if "code" in r:  # for r['code'] in (404, 400)
        return
    postlink = r['postLink']
    subreddit = r['subreddit']
    title = r['title']
    image = r['url']
    author = r['author']
    upvote = r['ups']
    caption = f"<b>{title}</b>\n"
    caption += f"`Posted by u/{author}`\n"
    caption += f"↕️ <code>{upvote}</code>\n"
    if r['spoiler']:
        caption += "⚠️ Post marked as SPOILER\n"
    if r['nsfw']:
        caption += "🔞 Post marked Adult \n"
    return caption, subreddit, postlink, image
