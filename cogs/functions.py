from discord.ext import commands
import discord

class Functions(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name='status', help='Change status of the bot' )
    async def status(self, ctx, program: str):
        activity = discord.Game(name=program)
        await commands.change_presence(activity=activity)
        await ctx.reply('Status changed to: {}'.format(program))

def setup(client):
    client.add_cog(Functions(client))