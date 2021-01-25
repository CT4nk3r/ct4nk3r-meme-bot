import asyncio
from os import name
from discord.ext import commands
import random

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name='roll', help='Simulates rolling dice.')
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
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
    
    @commands.command(name='ping', help='Writes back Pong in response')
    async def ping(self,ctx):
        await ctx.send("Pong")

    @commands.command(name='hello', help='hello command for the bot')
    async def hello(self, ctx):
        print(ctx.author)
        await ctx.reply('Hello {0.author}'.format(ctx))

    @commands.command(name='hi', help='hello command with delay')
    async def hi(self, ctx):
        print(ctx.author)
        await asyncio.sleep(5)
        await ctx.reply('Hello {0.author}'.format(ctx))
def setup(client):
    client.add_cog(Test(client))