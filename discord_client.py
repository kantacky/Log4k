import discord

async def postToDiscordChannel(token, channel_id, content):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    await client.login(token)
    channel = client.get_channel(channel_id)
    await channel.send(content)
