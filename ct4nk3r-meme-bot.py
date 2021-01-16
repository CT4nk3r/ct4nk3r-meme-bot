import discord
import asyncio

from authentication import reddit_authentication
from authentication import discord_authentication
print("Authenticating discord bot...")
TOKEN = discord_authentication()
print("Authenticating reddit bot...")
reddit = reddit_authentication()
client = discord.Client()
subreddit = reddit.subreddit('memes')

@client.event
async def on_ready():
    print('Discord authentication as: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.reply('Hello!', mention_author=True)

    if message.content.startswith('!status'):
        activity = discord.Game(name="with the API")
        await client.change_presence(status=discord.Status.idle, activity=activity)

    if message.content.startswith('!meme'):
        new_meme_of_the_day = subreddit.new(limit=1)
        for meme in new_meme_of_the_day:
            print(meme.url)
            await message.channel.send(meme.url)

    if message.content.startswith('!test'):
        await message.channel.send('test done')
    
    if message.content.startswith('!countdown'):
        number = 10
        msg = await message.channel.send(number)
        await asyncio.sleep(1.0)
        while (number != 0):
            number = number - 1
            await msg.edit(content=number)
            await asyncio.sleep(1.0)
    
client.run(TOKEN)