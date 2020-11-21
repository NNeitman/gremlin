import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)
bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

try:
    token = os.environ['DISCORD_GREMLIN_TOKEN']
    bot.run(token)
except Error as e:
    log.error("Bot died")
    log.error(e)
    