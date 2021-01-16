import discord
from datetime import datetime,timedelta

from praw.models.listing.mixins import subreddit
from prawcore.exceptions import UnavailableForLegalReasons

from authentication import reddit_authentication
from authentication import discord_authentication
TOKEN = discord_authentication()
reddit = reddit_authentication()
client = discord.Client()

subreddit = reddit.subreddit('memes')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.random_meme'):
        new_meme_of_the_day = subreddit.new(limit=1)
        for meme in new_meme_of_the_day:
            print(meme.url)
            await message.channel.send(meme.url)
    if message.content.startswith('.test'):
        await message.channel.send('test done')

client.run(TOKEN)