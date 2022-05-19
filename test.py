import discord
import os
import os; print(os.getcwd())
import subprocess
import sys



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
    game = discord.Game(f'{guild_count} サーバーに導入されています')
    await client.change_presence(activity=discord.Game(name=game))
    print('ログインしました {0.user}'.format(client))
    await ch.send("BOTが起動しました！")


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
        embed = discord.Embed(title="BOT導入URL通常", description='https://discord.com/api/oauth2/authorize?client_id=924945655414267934&permissions=414531968064&scope=bot')
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="BOTが正常に動作しない場合 こちらから導入してください", description='https://discord.com/api/oauth2/authorize?client_id=924945655414267934&permissions=8&scope=bot')
        await message.channel.send(embed=embed)

        print('メッセージを送りました')
        print(message.content)

    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!help':
        print('メッセージを確認')
        await message.channel.send('`spb!help` _ヘルプを表示します_')
        await message.channel.send('`spb!run` _BOTを起動します_')
        await message.channel.send('`spb!boturl` _BOTの導入URLを表示します_')
        msg = '`グローバルチャット機能`'+'\n'+'[hrl_グローバルチャット] という名前のテキストチャンネルを作成してください' + '\n' + 'それだけでグローバルチャットが使えるようになります' + '\n' + 'ただしプライベートチャンネルに設定した際は権限設定でチャンネルを表示する権限をBOTに与えてください'+'\n'+'`チャットログ作成機能`'+'\n'+'[ログ_hrk] という名前のテキストチャンネルを作成してください' + '\n' + 'それだけでログ機能が使えるようになります' + '\n' + 'ただしプライベートチャンネルに設定した際は権限設定でチャンネルを表示する権限をBOTに与えてください'
        embed = discord.Embed(title="ボットコマンド", description=msg)
        await message.channel.send(embed=embed)

        print(message.content)
        print('メッセージを送りました')


    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!status':
        guild_count = len(client.guilds)
        game = discord.Game(f'{guild_count} サーバーに導入されています' + '\n' + '\n' + 'BOTは現在正常に起動中です')
        embed = discord.Embed(title="BOT : ステータス", description=game)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="BOT : バージョン : 1.57", description=game)
        await message.channel.send(embed=embed)


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
            await ch.send("BOTが再起動します")
            proc = subprocess.Popen(['python3', 'test.py'])
            await client.logout()
            proc.poll()
            exit

    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'spb!helptest':
        print('メッセージを確認')
        await message.channel.send('`spb!help` _ヘルプを表示します_')
        await message.channel.send('`spb!run` _BOTを起動します_')
        await message.channel.send('`spb!boturl` _BOTの導入URLを表示します_')
        msg = '`グローバルチャット機能`'+'\n'+'[hrl_グローバルチャット] という名前のテキストチャンネルを作成してください' + '\n' + 'それだけでグローバルチャットが使えるようになります' + '\n' + 'ただしプライベートチャンネルに設定した際は権限設定でチャンネルを表示する権限をBOTに与えてください'+'\n'+'`チャットログ作成機能`'+'\n'+'[ログ_hrk] という名前のテキストチャンネルを作成してください' + '\n' + 'それだけでログ機能が使えるようになります' + '\n' + 'ただしプライベートチャンネルに設定した際は権限設定でチャンネルを表示する権限をBOTに与えてください'
        embed = discord.Embed(title="ボットコマンド", description=msg)
        await message.channel.send(embed=embed)

        print(message.content)
        print('メッセージを送りました')

 
# Botの起動とDiscordサーバーへの接続
client.run(data)
