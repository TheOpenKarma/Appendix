import discord
import random
from diacord.ext import commands

class MiscCogs(commands.Cog, name="Miscellaneous Commands"):
  '''Thses are Miscellaneous Commands'''

  def __init__(self, bot):
    self.bot = bot

  #a simple command to make sure the bot is working correctly
  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'Hello there {ctx.autor.mention}')

  @commands.command()
  async def help(self, ctx):
    embed = discord.Embed(title="Command List", description="A list of commands")
    embed.add_field(name="Ping", value="To make sure the bot is working correctly")
    embed.add_field(name="__", value="More commands to come in the future!")
    await ctx.send(embed=embed)


# needed per cog
def setup(bot):  bot.add_cog(MiscCogs(bot))