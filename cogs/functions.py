import asyncio
import random
import discord

from discord.ext import commands

class Functions(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name='status', help='Change status of the bot' )
    async def status(self, ctx, program: str):
        print(program)
        activity = discord.Game(name=program)
        await self.client.change_presence(activity=activity)
        await ctx.reply('Status changed to: {}'.format(program))
    
    @commands.command(name='countdown', help='counting down from 10 to 0')
    async def countdown(self, ctx):
        number = 10
        msg = await ctx.reply(number)
        await asyncio.sleep(1.0)
        while (number != 0):
            number = number - 1
            await msg.edit(content=number)
            await asyncio.sleep(1.0)

    
def setup(client):
    client.add_cog(Functions(client))