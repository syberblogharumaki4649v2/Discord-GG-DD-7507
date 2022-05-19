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

# 接続に必要なオブジェクトを生成
client = discord.Client()

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
    guild_count = len(client.guilds)
    game = discord.Game(f'ただいま起動しました')
    await client.change_presence(activity=discord.Game(name=game))
    time.sleep(3)
    game = discord.Game(f'{guild_count} サーバーに導入されています')
    await client.change_presence(activity=discord.Game(name=game))
    print('ログインしました {0.user}'.format(client))
    await ch.send("`BOTが起動しました！`")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    guild_count = len(client.guilds)
    game = discord.Game(f'{guild_count} サーバーに導入されています')
    await client.change_presence(activity=discord.Game(name=game))
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
      return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!run':
        print('メッセージを確認')
        await message.channel.send('`このコマンドは準備中です`')
        print('メッセージを送りました')
        print(message.author,' が ',message.content,' を送りました')


    if message.author.bot:
       return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!boturl':
        print('メッセージを確認')
        embed = discord.Embed(title="BOT導入URL", description='`通常導入URL`'+'\n'+'https://discord.com/api/oauth2/authorize?client_id=924945655414267934&permissions=414531968064&scope=bot'+'\n'+'`BOTが正常に動作しない場合`'+'\n'+'https://discord.com/api/oauth2/authorize?client_id=924945655414267934&permissions=8&scope=bot')
        await message.channel.send(embed=embed)
        print('メッセージを送りました')
        print(message.content)

    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!help':
        print('メッセージを確認')
        msg = '`開発段階のコマンドのヘルプを表示`'+'\n'+'spb!testcmdhelp'+'\n'+'`今後の予定を表示`'+'\n'+'spb!update'+'\n'+'`ヘルプを表示`'+'\n'+'spb!help'+'\n'+'`BOTの導入URLを表示`'+'\n'+'spb!boturl'+'\n'+'`グローバルチャット機能`'+'\n'+'[hrk_グローバルチャット] という名前のテキストチャンネルを作成してください' + '\n' + 'それだけでグローバルチャットが使えるようになります' + '\n' + 'ただしプライベートチャンネルに設定した際は権限設定でチャンネルを表示する権限をBOTに与えてください'+'\n'+'`チャットログ作成機能`'+'\n'+'[ログ_hrk] という名前のテキストチャンネルを作成してください' + '\n' + 'それだけでログ機能が使えるようになります' + '\n' + 'ただしプライベートチャンネルに設定した際は権限設定でチャンネルを表示する権限をBOTに与えてください'
        embed = discord.Embed(title="ボットコマンド", description=msg)
        await message.channel.send(embed=embed)

        print(message.content)
        print('メッセージを送りました')


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
            await ch.send("`BOTを再起動＆ボットを更新します`")
            game = discord.Game(f'再起動中です....')
            await client.change_presence(activity=discord.Game(name=game))
            proc = subprocess.Popen(['python3', '1.py'])
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
            guild_count = len(client.guilds)
            game = discord.Game(f'ボットはシャットダウンしています')
            ch = client.get_channel(947469205538762812)
            await ch.send("`BOTをシャットダウンします`")
            proc = subprocess.Popen(['python3', 'down.py'])
            await client.logout()
            proc.poll()
            exit

    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!vr':
        msg = "バージョン 1.7.6 早期リリース"
        embed = discord.Embed(title="ベータ版コマンド：ボットバージョン", description=msg)
        await message.channel.send(embed=embed)


    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!spam':
        if message.author.guild_permissions.administrator:
            msg = "スパムをしようとしたやつは誰だ～ ＾_＾"
            embed = discord.Embed(title="スパムは禁止されています", description=msg)
            await message.channel.send(embed=embed)

    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!update':
        if message.author.guild_permissions.administrator:
            msg = "ボットの機能追加 : 2022 05 のどこかでやる予定です"
            embed = discord.Embed(title="今後の予定", description=msg)
            await message.channel.send(embed=embed)

    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!testcmdhelp':
        print('メッセージを確認')
        msg = '`サーバー認証機能（開発段階）`'+'\n'+'spb!verify'+'\n'+'`ボットを再起動（開発者のみ）`'+'\n'+'spb!re'+'\n'+'`ボットをシャットダウン（開発者のみ）`'+'\n'+'spb!down'+'\n'+'`ボットのバージョン情報`'+'\n'+'spb!vr'
        embed = discord.Embed(title="ボット開発中＆開発者専用コマンド", description=msg)
        await message.channel.send(embed=embed)

        print(message.content)
        print('メッセージを送りました')

    if message.author.bot:
       return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!verify':

        passseta = random.randint(11111111, 9999999999)
        passsetb = random.randint(11111111, 9999999999)
        passsetc = random.randint(11111111, 9999999999)
        passsetd = random.randint(11111111, 9999999999)
        passsete = random.randint(11111111, 9999999999)
        print(passseta)
        print(passsetb)
        print(passsetc)
        print(passsetd)
        print(passsete)
        passlock = passseta*passsetb*passsetc-passsetd-passsete
        channel = message.channel
        await channel.send("認証コードを３０秒以内に送ってください")
        await channel.send(str('`認証コード : `')+str(passlock))
        path = str('./一時フォルダ/')+str(message.guild.id)+str(message.channel.id)+str(message.author.id)
        file_name = str('./一時フォルダ/')+str(message.guild.id)+str(message.channel.id)+str(message.author.id)
        file = open(file_name, 'w')
        file.write(str(passlock))
        file.close()
        file = open(file_name)
        file.close()

        # 待っているものに該当するかを確認する関数
        def check(m):
            # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
            # コマンドを打ったチャンネルという条件
            path = str('./一時フォルダ/')+str(message.guild.id)+str(message.channel.id)+str(message.author.id)
            file_name = str('./一時フォルダ/')+str(message.guild.id)+str(message.channel.id)+str(message.author.id)
            f = open(path)
            file = open(file_name)
            data = file.read()
            print(data)
            file.close()
            file = open(file_name)
            file.close()
            return m.content == data and m.channel == channel

        try:
            # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
            msg = await client.wait_for('message', check=check, timeout=30)
            # wait_forの1つ目のパラメータは、イベント名の on_がないもの
            # 2つ目は、待っているものに該当するかを確認する関数 (任意)
            # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

        # asyncio.TimeoutError が発生したらここに飛ぶ
        except asyncio.TimeoutError:
            await channel.send(f'{message.author.mention}さん、認証時間切れです')
        else:
            # メンション付きでメッセージを送信する。
            await channel.send(f'{msg.author.mention}さん、認証は成功しました')

    if message.content == 'spb!ログイン':

        passseta = random.randint(11111111, 9999999999)
        passsetb = random.randint(11111111, 9999999999)
        passsetc = random.randint(11111111, 9999999999)
        passsetd = random.randint(11111111, 9999999999)
        passsete = random.randint(11111111, 9999999999)
        print(passseta)
        print(passsetb)
        print(passsetc)
        print(passsetd)
        print(passsete)
        passlock = passseta*passsetb*passsetc-passsetd-passsete
        channel = message.channel
        await channel.send("認証コードを３０秒以内に送ってください")
        await channel.send(str('`認証コード : `')+str(passlock))
        path = str('./一時フォルダ/')+str(message.guild.id)+str(message.channel.id)+str(message.author.id)
        file_name = str('./一時フォルダ/')+str(message.guild.id)+str(message.channel.id)+str(message.author.id)
        file = open(file_name, 'w')
        file.write(str(passlock))
        file.close()
        file = open(file_name)
        file.close()

        # 待っているものに該当するかを確認する関数
        def check(m):
            # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
            # コマンドを打ったチャンネルという条件
            path = str('./一時フォルダ/')+str(message.guild.id)+str(message.channel.id)+str(message.author.id)
            file_name = str('./一時フォルダ/')+str(message.guild.id)+str(message.channel.id)+str(message.author.id)
            f = open(path)
            file = open(file_name)
            data = file.read()
            print(data)
            file.close()
            file = open(file_name)
            file.close()
            return m.content == data and m.channel == channel

        try:
            # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
            msg = await client.wait_for('message', check=check, timeout=30)
            # wait_forの1つ目のパラメータは、イベント名の on_がないもの
            # 2つ目は、待っているものに該当するかを確認する関数 (任意)
            # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

        # asyncio.TimeoutError が発生したらここに飛ぶ
        except asyncio.TimeoutError:
            await channel.send(f'{message.author.mention}さん、認証時間切れです')
        else:
            # メンション付きでメッセージを送信する。
            await channel.send(f'{msg.author.mention}さん、認証は成功しました')
            await channel.send(f'ユーザー名を入力してください')

            # 待っているものに該当するかを確認する関数
            def check(m):
                # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                # コマンドを打ったチャンネルという条件
                path = str('./アカウント/') + str(message.author.id)
                file_name = str('./アカウント/') + str(message.author.id)
                f = open(path)
                file = open(file_name)
                data = file.read()
                print(data)
                file.close()
                file = open(file_name)
                file.close()
                return m.content == data and m.channel == channel

            try:
                # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                msg = await client.wait_for('message', check=check, timeout=30)
                # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

            # asyncio.TimeoutError が発生したらここに飛ぶ
            except asyncio.TimeoutError:
                await channel.send(f'{message.author.mention}さん、認証時間切れです')
            else:
                # メンション付きでメッセージを送信する。
                await channel.send(f'パスワードを入力してください')

                # 待っているものに該当するかを確認する関数
                def check(m):
                    # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                    # コマンドを打ったチャンネルという条件
                    path = str('./アカウント/パスワード/') + str(message.author.id)
                    file_name = str('./アカウント/パスワード/') + str(
                        message.author.id)
                    f = open(path)
                    file = open(file_name)
                    data = file.read()
                    print(data)
                    file.close()
                    file = open(file_name)
                    file.close()
                    return m.content == data and m.channel == channel

                try:
                    # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                    msg = await client.wait_for('message', check=check, timeout=30)
                    # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                    # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                    # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

                # asyncio.TimeoutError が発生したらここに飛ぶ
                except asyncio.TimeoutError:
                    await channel.send(f'{message.author.mention}さん、認証時間切れです')
                else:
                    # メンション付きでメッセージを送信する。
                    await channel.send(f'{msg.author.mention}さん、ログインは成功しました')

# Botの起動とDiscordサーバーへの接続
client.run(data)
