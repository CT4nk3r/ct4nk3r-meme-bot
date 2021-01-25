from os import name
from discord.ext import commands
import random

class Dice(commands.Cog):

    def __init__(self, client):
        self.client = client

        
    @commands.command()
    async def r(self, ctx, roll : str):
        """Rolls a dice using #d# format.
        e.g .r 3d6"""
        
        resultTotal = 0
        resultString = ''
        try:
            try: 
                numDice = roll.split('d')[0]
                diceVal = roll.split('d')[1]
            except Exception as e:
                print(e)
                await ctx.send("Format has to be in #d# %s." % ctx.message.author.name)
                return

            if int(numDice) > 500:
                await ctx.send("I cant roll that many dice %s." % ctx.message.author.name)
                return
            
            await ctx.send("Rolling %s d%s for %s" % (numDice, diceVal, ctx.message.author.name))
            rolls, limit = map(int, roll.split('d'))

            for r in range(rolls):
                number = random.randint(1, limit)
                resultTotal = resultTotal + number
                
                if resultString == '':
                    resultString += str(number)
                else:
                    resultString += ', ' + str(number)
            
            if numDice == '1':
                await ctx.send(ctx.message.author.mention + "  :game_die:\n**Result:** " + resultString)
            else:
                await ctx.send(ctx.message.author.mention + "  :game_die:\n**Result:** " + resultString + "\n**Total:** " + str(resultTotal))

        except Exception as e:
            print(e)
            return

def setup(client):
    client.add_cog(Dice(client))