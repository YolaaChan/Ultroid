# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available

•`{i}invertgif`
  Make Gif Inverted(negative).

•`{i}bwgif`
  Make Gif black and white

•`{i}vtog`
  Reply To Video , It will Create Gif
  Video to Gif

•`{i}gif <query>`
   Send video regarding to query.
"""


import os
import time
import random

from . import *


@ultroid_cmd(pattern="bwgif$")
async def igif(e):
    a = await e.get_reply_message()
    if not (a and a.media):
        return await eod(e, "`Reply To gif only`")
    wut = mediainfo(a.media)
    if "gif" not in wut:
        return await eod(e, "`Reply To Gif Only`")
    xx = await eor(e, "`Processing...`")
    z = await ultroid_bot.download_media(a.media)
    try:
        await bash(f'ffmpeg -i "{z}" -vf format=gray ult.gif -y')
        await e.client.send_file(e.chat_id, "ult.gif", support_stream=True)
        os.remove(z)
        os.remove("ult.gif")
        await xx.delete()
    except Exception as er:
        LOGS.info(er)


@ultroid_cmd(pattern="invertgif$")
async def igif(e):
    a = await e.get_reply_message()
    if not (a and a.media):
        return await eod(e, "`Reply To gif only`")
    wut = mediainfo(a.media)
    if "gif" not in wut:
        return await eod(e, "`Reply To Gif Only`")
    xx = await eor(e, "`Processing...`")
    z = await ultroid_bot.download_media(a.media)
    try:
        await bash(
            f'ffmpeg -i "{z}" -vf lutyuv="y=negval:u=negval:v=negval" ult.gif -y'
        )
        await e.client.send_file(e.chat_id, "ult.gif", support_stream=True)
        os.remove(z)
        os.remove("ult.gif")
        await xx.delete()
    except Exception as er:
        LOGS.info(er)


@ultroid_cmd(pattern="gif ?(.*)")
async def gifs(ult):
    get = ult.pattern_match.group(1)
    ck = random.randint(0, 5)
    n = 0
    if ";" in get:
        try:
            n = int(get.split(";")[-1])
        except BaseException:
            pass
    if not get:
        return await eor(ult, "`.gif <query>`")
    m = await eor(ult, "`Searching gif ...`")
    gifs = await ultroid_bot.inline_query("gif", f"{get}")
    if not n:
        await gifs[ck].click(
            ult.chat.id, reply_to=ult.reply_to_msg_id, silent=True, hide_via=True
        )
    else:
        for x in range(n):
            await gifs[x].click(
                ult.chat.id, reply_to=ult.reply_to_msg_id, silent=True, hide_via=True
            )
    await m.delete()


@ultroid_cmd(pattern="vtog$")
async def vtogif(e):
    a = await e.get_reply_message()
    if not (a and a.media):
        return await eod(e, "`Reply To video only`")
    wut = mediainfo(a.media)
    if "video" not in wut:
        return await eod(e, "`Reply To Video Only`")
    xx = await eor(e, "`Processing...`")
    dur = a.media.document.attributes[0].duration
    tt = time.time()
    if int(dur) < 120:
        z = await ultroid_bot.download_media(a.media)
        await bash(
            f'ffmpeg -i {z} -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 ult.gif -y'
        )
        await e.client.send_file(e.chat_id, "ult.gif", support_stream=True)
        os.remove(z)
        os.remove("ult.gif")
        await xx.delete()
    else:
        a.media.document
        vid = await downloader(a.file.name, a.media.document, xx, tt, "Downloading...")
        z = vid.name
        await bash(
            f'ffmpeg -ss 3 -t 100 -i {z} -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 ult.gif'
        )
        await e.client.send_file(e.chat_id, "ult.gif", support_stream=True)
        os.remove(z)
        os.remove("ult.gif")
        await xx.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})