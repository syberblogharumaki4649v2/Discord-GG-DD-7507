import discord
import os
import os; print(os.getcwd())
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

global_channel_name = "ログ_hrk" #設定したいチャンネル名を入力

client = discord.Client() #接続に必要なオブジェクトを生成
print("起動しました")

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
    await ch.send("`ログ機能2が起動しました！`")
@client.event
async def on_message(message):

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!re':
            setmsg = message.author.id
            print(setmsg)
            if setmsg == 812275752904163358:
                guild_count = len(client.guilds)
                game = discord.Game(f'{guild_count} サーバーに導入されています' + '\n' + '\n' + 'BOTは現在正常に起動中です')
                ch = client.get_channel(947469205538762812)
                await ch.send("`ログ機能2を再起動＆を更新します`")
                game = discord.Game(f'ログ機能2を再起動中です....')
                await client.change_presence(activity=discord.Game(name=game))
                proc = subprocess.Popen(['python3', '5.py'])
                await client.logout()
                proc.poll()
                exit


        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!down':
            setmsg = message.author.id
            print(setmsg)
            if setmsg == 812275752904163358:
                ch = client.get_channel(947469205538762812)
                await ch.send("`ログ機能2をシャットダウンします`")
                proc = subprocess.Popen(['python3', 'down4.py'])
                await client.logout()
                proc.poll()
                exit

        #メッセージ受信部
        if message.author.bot: #BOTの場合は何もせず終了
            return
        #メッセージ送信部
        for channel in message.guild.text_channels: #BOTが所属する全てのチャンネルをループ
            if channel.name == global_channel_name: #グローバルチャット用のチャンネルが見つかったとき
                if channel == message.channel: #発言したチャンネルには送らない
                    continue
                seta = 'https://discord.com/channels/'
                setc = seta,message.guild.id,message.channel.id,message.id
                embed = discord.Embed(title="メッセージURL", description=setc)
                await channel.send(embed=embed) #メッセージを送信

client.run(data)