from discord.ext import commands

from json import load
from pathlib import Path
from pkgutil import iter_modules

# Load config json file

with Path("config.json").open() as f:
    config = load(f)

# Create the discord bot
bot = commands.Bot(command_prefix=config["prefix"])


# Events
@bot.event
async def on_ready():
    print("Bot online!")
    status_channel = bot.get_channel(config["status_channel"])
    await status_channel.send('Bot is online!')


@commands.command(pass_context=True)
@bot.event
async def on_message(message):
    # Don't do anything if the message is from the bot (prevent a constant loop of spam)
    if message.author == bot.user:
        return

    if message.content.startswith(config["prefix"]):
        await bot.process_commands(message)


# Load cogs and run the bot
for cog in iter_modules(["cogs"]):
    bot.load_extension(f'cogs.{cog.name}')

bot.run(config["token"])
