import discord
from discord.ext import commands

# Intents設定
intents = discord.Intents.default()
intents.messages = True  # メッセージイベントを監視
intents.guilds = True  # サーバーイベントを監視

# Botのインスタンスを作成
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Botがログインしたときに実行されるイベントハンドラ
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    # 新しいメッセージが投稿されたときに実行されるイベントハンドラ
    if message.channel.id == 00000000:  # チャンネルID
        if message.type == discord.MessageType.default and message.author != bot.user:
            try:
                await message.publish()  # メッセージを公開
            except discord.HTTPException:
                pass  # メッセージが公開チャンネルにないか、すでに公開されている場合

# Botを起動
bot.run('Discord-TOKEN')