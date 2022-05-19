import discord
import os
import os; print(os.getcwd())

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
async def on_message(message):
    if client.user != message.author:
        print(message.id) #メッセージのid
        print(message.content) #メッセージのcontent 
        
        await message.delete()#メッセージの削除
        
        await client.send_message(message.channel, "自動でメッセージを消去しました") 

client.run(data)