#Quick Startup

print("Starting Server... \n")

prefix = ('A!')

import discord
from discord.ext import commands
from datetime import datetime
import os

bot = commands.Bot(
  command_prefix=(prefix),
  case_insensitive=True,

  #this will display what the bot is watching
  activity=discord.Activity(type=discord.ActivityType.watching,
                            name="use A!help for commands"),
  intents=discord.Intents.all())

  #removes built in help command
  bot.remove_command('help')

  #used for dev commands (only you can run them) Put your user ID here
bot.author_id = 885720186186006608

  @bot.event()
  async def on_ready():
    #disply loaded
    print("\nAPI Loaded " + datetime.now().strftime('%d %b %Y %H %M'),
          bot.user,
          "User ID " + str(bot.user.id),
          sep='\n  ')



# Fill with the path to all of your cogs (in `cogs` folder)
extensions = [
    'cogs.dev_cog_commands',

    'cogs.misc_cogs'
]

# Load and run bot
if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

from keep_alive import keep_alive

keep_alive()
bot.run(os.environ["DISCORD_API_TOKEN"])
