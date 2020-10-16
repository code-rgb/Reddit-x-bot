#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) code-rgb

from pyrogram import Client
from pyrogram import __version__
from pyrogram.raw.all import layer

from pyrobot import (
    APP_ID,
    API_HASH,
    TG_BOT_TOKEN,
    TMP_DOWNLOAD_DIRECTORY,
    LOGGER
)


class app(Client):

    def __init__(self):
        name = self.__class__.__name__.lower()

        
        super().__init__(
                ":memory:",
                plugins=dict(root="pyrobot/plugins"),
                workdir=TMP_DOWNLOAD_DIRECTORY,
                api_id=APP_ID,
                api_hash=API_HASH,
                bot_token=TG_BOT_TOKEN
        )
        

    async def start(self):
        await super().start()

        usr_bot_me = await self.get_me()
        LOGGER.info(
            f"Reddit-X Bot based on Pyrogram v{__version__} "
            f"(Layer {layer}) started on @{usr_bot_me.username}. "
            "Hi."
        )

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("Reddit-X Bot stopped. Bye.")
