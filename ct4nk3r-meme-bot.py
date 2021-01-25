from asyncio import events
import os
import discord
import asyncio

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

@bot.command(name='meme', help='sends the newest meme into chat from r/memes')
async def meme(ctx):
    new_meme = subreddit.new(limit=1)
    for meme in new_meme:
        print(meme)
        print(meme.url)
        await ctx.reply(meme.url)

async def meme():
    await bot.wait_until_ready()
    await asyncio.sleep(1.5)
    while not bot.is_closed():
        new_meme = subreddit.new(limit=1)           
        for meme in new_meme:
            print(meme)
            print(meme.url)
            channel = bot.get_channel(800129380163518465)
            await channel.send(meme.url)
            await asyncio.sleep(50)
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

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.loop.create_task(meme())
bot.run(TOKEN)