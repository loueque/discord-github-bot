from discord.ext import commands
import discord

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx):
        await ctx.send('https://dontasktoask.com/')

    @commands.command()
    async def conventional(self, ctx):
        await ctx.send('https://www.conventionalcommits.org/en/v1.0.0/')

    @commands.codeblock()
    async def codeblock(self, ctx, *, lang, code):
        await ctx.send(f'```{lang}\n{code}```')

def setup(bot):
    bot.add_cog(Utility(bot))
