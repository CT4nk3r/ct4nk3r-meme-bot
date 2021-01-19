import discord
import asyncio
import random
import os

from discord.ext import commands

from authentication import reddit_authentication
from authentication import discord_authentication
print("Authenticating discord bot...")
TOKEN = discord_authentication()
print("Authenticating reddit bot...")
reddit = reddit_authentication()
print("Reddit authentication as: {}".format(reddit.user.me()))
subreddit = reddit.subreddit('memes')
bot = commands.Bot(command_prefix='$')

@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    total = 0
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    for roll in dice:
        total = total + int(roll)
        print(int(roll))
    print(total)
    await ctx.send(', '.join(dice))
    await ctx.send('total: {}'.format(total))
    pass

@bot.command(name='status', help='Change status of the bot' )
async def status(ctx, program: str):
    activity = discord.Game(name=program)
    await bot.change_presence(activity=activity)
    await ctx.reply('Status changed to: {}'.format(program))

@bot.command(name='meme', help='sends the newest meme into chat from r/memes')
async def meme(ctx):
    new_meme = subreddit.new(limit=1)
    for meme in new_meme:
        print(meme)
        print(meme.url)
        await ctx.reply(meme.url)

@bot.command(name='countdown', help='counting down from 10 to 0')
async def countdown(ctx):
    number = 10
    msg = await ctx.reply(number)
    await asyncio.sleep(1.0)
    while (number != 0):
        number = number - 1
        await msg.edit(content=number)
        await asyncio.sleep(1.0)

@bot.command(name='hello', help='hello command for the bot')
async def hello(ctx):
    print(ctx.author)
    await ctx.reply('Hello {0.author}'.format(ctx))

@bot.event
async def on_ready():
    print('Discord authentication as: {0.user}'.format(bot))
    activity = discord.Game(name='https://github.com/CT4nk3r/ct4nk3r-meme-bot')
    await bot.change_presence(activity=activity)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.event
async def logout():
    await bot.logout()

async def meme():
    await bot.wait_until_ready()
    while not bot.is_closed():
        new_meme = subreddit.new(limit=1)           
        for meme in new_meme:
            print(meme)
            print(meme.url)
            channel = bot.get_channel(800129380163518465)
            await channel.send(meme.url)
            await asyncio.sleep(50)

bot.loop.create_task(meme())
bot.run(TOKEN)