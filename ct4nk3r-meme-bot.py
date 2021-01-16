import discord
import asyncio
import random
from discord.ext import commands

from authentication import reddit_authentication
from authentication import discord_authentication
print("Authenticating discord bot...")
TOKEN = discord_authentication()
print("Authenticating reddit bot...")
reddit = reddit_authentication()
client = discord.Client()
subreddit = reddit.subreddit('memes')

# 1
from discord.ext import commands

# 2
bot = commands.Bot(command_prefix='!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice, number_of_sides):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@client.event
async def on_ready():
    print('Discord authentication as: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.reply('Hello!', mention_author=True)

    # bot = commands.Bot(command_prefix="$")
    # bot = discord.Client()
    # @bot.command()
    # async def print(ctx, arg):
    #     await ctx.channel.send(arg)


    if message.content.startswith('!status'):
        activity = discord.Game(name="with codes")
        async def status(arg):
            if arg:
                activity = discord.Game(name = arg)        
        await client.change_presence(activity=activity)

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