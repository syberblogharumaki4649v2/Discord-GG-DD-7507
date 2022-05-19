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

client = discord.Client() #接続に必要なオブジェクトを生成
print("起動しました")

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
    await ch.send("`グローバル機能2が起動しました！`")

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
            await ch.send("`グローバル機能2を再起動＆を更新します`")
            game = discord.Game(f'再起動中です....')
            await client.change_presence(activity=discord.Game(name=game))
            proc = subprocess.Popen(['python3', '4.py'])
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
            await ch.send("`グローバル機能2をシャットダウンします`")
            proc = subprocess.Popen(['python3', 'down3.py'])
            await client.logout()
            proc.poll()
            exit



    file_name = str("./サーバー設定/")+str(message.guild.id)

    try:
        file = open(file_name)
        global_channel_name = file.read()
        print(data)
    except Exception as e:
       print(e)
    finally:
        file.close()

    if message.channel.name == global_channel_name: #グローバルチャットにメッセージが来たとき
        #メッセージ受信部
        if message.author.bot: #BOTの場合は何もせず終了
            return
        #メッセージ送信部
        for channel in client.get_all_channels(): #BOTが所属する全てのチャンネルをループ
            if channel.name == global_channel_name: #グローバルチャット用のチャンネルが見つかったとき
                if channel == message.channel: #発言したチャンネルには送らない
                    continue

                embed=discord.Embed(description=message.content, color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
                embed.set_author(name="{}#{}".format(message.author.name, message.author.discriminator),icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
                embed.set_footer(text="{} / mID:{}".format(message.guild.name, message.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
                if message.attachments != []: #添付ファイルが存在するとき
                    embed.set_image(url=message.attachments[0].url)

                if message.reference: #返信メッセージであるとき
                    reference_msg = await message.channel.fetch_message(message.reference.message_id) #メッセージIDから、元のメッセージを取得
                    if reference_msg.embeds and reference_msg.author == client.user: #返信の元のメッセージが、埋め込みメッセージかつ、このBOTが送信したメッセージのとき→グローバルチャットの他のサーバーからのメッセージと判断
                        reference_message_content = reference_msg.embeds[0].description #メッセージの内容を埋め込みから取得
                        reference_message_author = reference_msg.embeds[0].author.name #メッセージのユーザーを埋め込みから取得
                    elif reference_msg.author != client.user: #返信の元のメッセージが、このBOTが送信したメッセージでは無い時→同じチャンネルのメッセージと判断
                        reference_message_content = reference_msg.content #メッセージの内容を取得
                        reference_message_author = reference_msg.author.name+'#'+reference_msg.author.discriminator #メッセージのユーザーを取得
                    reference_content = ""
                    for string in reference_message_content.splitlines(): #埋め込みのメッセージを行で分割してループ
                        reference_content += "> " + string + "\n" #各行の先頭に`> `をつけて結合
                    reference_value = "**@{}**\n{}".format(reference_message_author, reference_content) #返信メッセージを生成
                    embed.add_field(name='返信しました', value=reference_value, inline=True) #埋め込みに返信メッセージを追加

                await channel.send(embed=embed) #メッセージを送信

client.run(data)
