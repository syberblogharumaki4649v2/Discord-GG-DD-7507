import discord
import os
import os;

from discord import Client

print(os.getcwd())
import subprocess
import sys
import os
import os;
print(os.getcwd())
import random
import asyncio
import string
import secrets
import discord
import os
from discord.ext import commands
import random
import asyncio
import time
# 自分のBotのアクセストークンに置き換えてください
# 読込むファイルのパスを宣言する
file_name = "./token.txt"

try:
    file = open(file_name)
    data = file.read()
    print(data)
except Exception as e:
    print(e)
finally:
    file.close()

# 接続に必要なオブジェクトを生成
client: Client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('----------------')
    print('ログインしました')
    print('----------------')
    print('')
    print('BOT表示名：', client.user.name)  # Botの名前
    print('BOTのID：', client.user.id)  # ID
    print('Dicord.pyのバージョン：', discord.__version__)
    ch = client.get_channel(947469205538762812)
    print('')
    ch = client.get_channel(947469205538762812)
    game = discord.Game(f'ボットを停止しました')
    await client.change_presence(activity=discord.Game(name=game))
    print('ログインしました {0.user}'.format(client))
    await ch.send("`BOTを停止しました！`")


@client.event
async def on_message(message):
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!start':
        setmsg = message.author.id
        print(setmsg)
        if setmsg == 812275752904163358:
            guild_count = len(client.guilds)
            game = discord.Game(f'{guild_count} サーバーに導入されています' + '\n' + '\n' + 'BOTは現在正常に起動中です')
            ch = client.get_channel(947469205538762812)
            await ch.send("`BOTを起動＆ボットを更新します`")
            game = discord.Game(f'ボットを起動中です....')
            await client.change_presence(activity=discord.Game(name=game))
            proc = subprocess.Popen(['python3', '1.py'])
            await client.logout()
            proc.poll()
            exit


    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    botcmdlist = 'help boturl re down vr spam update testcmdhelp test verify ログイン'
    if (
            message.content in "spb!" + botcmdlist or "help" or "boturl" or "re" or "down" or "spam" or "update" or "testcmdhelp" or "test" or "verify" or "ログイン"):
        embed = discord.Embed(title="エラー", description='`ただいまボットは停止しています`')
        await message.channel.send(embed=embed)

# Botの起動とDiscordサーバーへの接続
client.run(data)

