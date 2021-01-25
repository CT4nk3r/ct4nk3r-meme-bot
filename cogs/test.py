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

def setup(client):
    client.add_cog(Test(client))