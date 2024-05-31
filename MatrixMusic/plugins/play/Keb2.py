import os
import asyncio
import requests
import config
import random
import time
from config import START_IMG_URL
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint


lnk= "" +config.SUPPORT_CHANNEL
@app.on_message(command(["‹ قران ›", "قران"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/lllIIlIllIlIIlI/{rl}"
    await client.send_voice(message.chat.id,url,caption="↯︙تم اختيار اية قرآنية لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ خطبه ›", "خطبه"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(22,200)
    url = f"https://t.me/fresdewi/{rl}"
    await client.send_voice(message.chat.id,url,caption="↯︙تم اختيار خطبة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )
    
