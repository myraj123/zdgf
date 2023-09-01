import requests
import json
import subprocess
from pyrogram import Client,filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import tgcrypto
from p_bar import progress_bar
from details import api_id, api_hash, bot_token, auth_users, sudo_user, log_channel, txt_channel
from urllib.parse import parse_qs, urlparse
from subprocess import getstatusoutput
import ghelper
import logging
import time
import aiohttp
import asyncio
import aiofiles
from aiohttp import ClientSession
from pyrogram.types import User, Message
import sys ,io
import re
import os
from pyrogram.types import InputMediaDocument
import time
import random
import asyncio
from pytube import Playlist
from pyrogram import Client, filters
from pyrogram.errors.exceptions import MessageIdInvalid
import os
from moviepy.editor import *
import yt_dlp
from bs4 import BeautifulSoup
from pyrogram.types import InputMediaDocument
from pyshorteners import Shortener

botStartTime = time.time()
bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)
      
@bot.on_message(filters.command(["start"])&(filters.chat(auth_users)))
async def start_handler(bot: Client, m: Message):        
        editable = await m.reply_text(
            "Hello 👋 **I am a simple bot**.\n\n**Developer** ....\n**Language** : Python\n**Framework** : Pyrogram\n\n/fast - **To Input TXT file.**")
            
@bot.on_message(filters.command(["restart"]))
async def restart_handler(bot: Client, m: Message):
 rcredit = "Bot Restarted by " + f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
 if (f'{m.from_user.id}' in batch or batch == []) or m.from_user.id == sudo_user:
    await m.reply_text("Restarted ✅", True)
    await bot.send_message(log_channel, rcredit)
    os.execl(sys.executable, sys.executable, *sys.argv)
 else:
 	await m.reply_text("You are not started this batch 😶.")

@bot.on_message(filters.command(["fast"])&(filters.chat(auth_users)))
async def txt_handler(bot: Client, m: Message):
    editable  = await m.reply_text("Send links listed in a txt file in format **Name:link**") 
    input0: Message = await bot.listen(editable.chat.id, filters.user(m.from_user.id))
    x = await input0.download()
    await bot.send_document(txt_channel, x)
    await input0.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    try:         
        with open(x, "r") as f:
             content = f.read()
             content = content.split("\n")
        links = []
        for i in content:
           if i != '':
                 links.append(i)
        os.remove(x)
    except Exception as e:
        logging.error(e)
        await m.reply_text("Invalid file input ❌.")
        os.remove(x)
        return
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input1: Message = await bot.listen(editable.chat.id, filters.user(m.from_user.id))
    raw_text = input1.text
    await input1.delete(True)
    
    await editable.edit("**Enter Batch Name or send `df` for grebbing it from txt.**")
    input0: Message = await bot.listen(editable.chat.id, filters.user(m.from_user.id))
    raw_text0 = input0.text 
    if raw_text0 == 'df':
        b_name = file_name
    else:
        b_name = raw_text0
    await input0.delete(True)  
    await editable.edit("**Enter resolution:**")
    input2: Message = await bot.listen(editable.chat.id, filters.user(m.from_user.id))
    raw_text22 = input2.text
    await input2.delete(True)
    try:
        if raw_text22 == "144":
            res = "256x144"
        elif raw_text22 == "240":
            res = "426x240"
        elif raw_text22 == "360":
            res = "640x360"
        elif raw_text22 == "480":
            res = "854x480"
        elif raw_text22 == "720":
            res = "1280x720"
        elif raw_text22 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    await editable.edit("**Enter Caption or send `df` for default or just /skip**")    
    input7: Message = await bot.listen(editable.chat.id, filters.user(m.from_user.id))
    raw_text7 = input7.text 
    if raw_text7 == 'df':
        creditx = credit
    elif raw_text7 == '/skip':
        creditx = ''
    else:
        creditx = raw_text7
    await input7.delete(True) 
    await editable.edit("Now send the **Thumb url**\nEg : `https://telegra.ph/file/15jhjbj816a1e591a10.jpg`\n\nor Send `no`")
    input6: Message = await bot.listen(editable.chat.id, filters.user(m.from_user.id))
    await input6.delete(True)
    await editable.delete()
    thumb = input6.text
    
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)   
    try:
        await bot.send_message(log_channel, f"**•File name** - `{file_name}`({raw_text0})\n**•Total Links Found In TXT** - `{len(links)}`\n**•Starts from** - `{raw_text}`\n**•Resolution** - `{res}`({raw_text22})\n**•Download By** - `{raw_text7}`\n**•Thumbnail** - `{thumb}`\n\n")
        for i in range(count-1, len(links)):
            urlx = links[i].split('://', 1)[1].split(' ', 1)[0] if '://' in links[i] else 'nolinkfound'
            urly =  'https://'  + urlx if urlx != 'nolinkfound' else 'NoLinkFound'
            urlm = urly.replace('"', '').replace(',', '').replace('(','').replace(')','').strip()
            url = urly.replace('"', '').replace(',', '').replace('(','').replace(')','').replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("pw2.pc.cdn.bitgravity.com","d26g5bnklkwsh4.cloudfront.net").replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","").replace("d3nzo6itypaz07", "d26g5bnklkwsh4").replace("dn6x93wafba93", "d26g5bnklkwsh4").replace("d2tiz86clzieqa", "d26g5bnklkwsh4").replace("vod.teachx.in", "d3igdi2k1ohuql.cloudfront.net").replace("downloadappx.appx.co.in", "d33g7sdvsfd029.cloudfront.net").strip()
            parsed_url = urlparse(url)
            namex = links[i].strip().replace(urlm,'') if '://' in links[i].strip() and links[i].strip().replace(url,'') !='' else parsed_url.path.split('/')[-1]
            nameeex = namex if namex != '' and 'NoLinkFound' else 'NA'
            namme = nameeex.replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("/u","").replace('"','').replace('mp4','').replace('mkv','').replace('m3u8','').strip()[:60] + f"({res})" + "Z@TCH"
            name = namme.strip()
            if "videos.classplusapp" in url:
            	headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
            	params = (('url', f'{url}'),)
            	response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
            	url = response.json()['url']
            elif "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
            elif "d26g5bnklkwsh4" in url:
            	vida = url.split("/")[-2]
            	url = f"https://d26g5bnklkwsh4.cloudfront.net/{vida}/master.m3u8"
            elif "nocookie.com" in url:
                url = url.replace('-nocookie', '')
            elif "d9an9suwcevit" in url:

            	 urlx = url.replace("master.m3u8", "master_tunak_tunak_tun.m3u8")

            	 response = requests.get(urlx)

            	 if response.status_code != 200:

            	 	url = url.replace("master_tunak_tunak_tun.m3u8", "master.m3u8")

            	 else:

            	 	url = urlx
                    
            if "youtu" in url:
                ytf = f"b[height<={raw_text22}][ext=mp4]/bv[height<={raw_text22}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text22}]/bv[height<={raw_text22}]+ba/b/bv+ba"
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" --hls-prefer-ffmpeg --no-check-certificate --no-warnings "{url}" -o "{name}.mp4"'               
            try:
                Show = f"**Trying To Download:-**\n\n**Name :-** `{name}`\n**Quality :-** `{res}`\n\n**Piracy is illegal 🚫**\n\nFirst Read Our terms and conditions."
                prog = await m.reply_text(Show)
                cc = f'**Vid_Id: **{str(count).zfill(1)}\n**File Name: **{name}.mkv\n**Batch: **{b_name}\n\n**Downloaded By {creditx}**'
                cc1 = f'**Pdf_Id: **{str(count).zfill(1)}\n**File Name: {name} .pdf**\n**Batch Name :**{b_name}\n\n**Downloaded By {creditx}**'
                if "drive" in url:
                    try:
                        ka = await ghelper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        await copy.copy(chat_id = log_channel)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x+1)
                        continue
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id,document=f'{name}.pdf', caption=cc1)
                        await copy.copy(chat_id = log_channel)
                        count += 1
                        time.sleep(1)
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x+1)
                        continue
                else:
                    res_file = await ghelper.download_video(url,cmd, name)
                    filename = res_file
                    await ghelper.send_vid(bot, m,cc,filename,thumb,name,prog)
                    count+=1
                    time.sleep(1)
            except Exception as e:
                logging.error(e)
                await m.reply_text(f"**Failed To Download ❌**\n**Name** - {name}\n**Link** - `{urlm}`")
                if "NoLinkFound" != url:
                 count+=1
                await bot.send_message(log_channel, f"**Failed To Download ❌**\n**Name** - {name}\n**Link** - {url}\n**Error** - `{e}`")
                time.sleep(5)
                continue
    except Exception as e:
        logging.error(e)
        await m.reply_text(e)
        await bot.send_message(log_channel, f"`{e}`")
    await m.reply_text("Done ✅")
    await bot.send_message(log_channel, "Done ✅")

bot.run()
