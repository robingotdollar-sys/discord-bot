import discord, os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("BOT ONLINE")

@client.event
async def on_message(msg):
    if msg.author.bot:
        return
    if msg.content == "!ping":
        await msg.channel.send("pong")

client.run(os.getenv("DISCORD_TOKEN"))
