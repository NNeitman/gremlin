import logging
import os
import discord
from discord.ext import commands


log = logging.getLogger(__name__)
bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ding(ctx):
    await ctx.send('dong')

@bot.command()
async def egg(ctx):
    await ctx.send('https://www.youtube.com/watch?v=XNyUALnj8V0')


try:
    token = os.environ['DISCORD_GREMLIN_TOKEN']
    bot.run(token)
except RuntimeError as e:
    log.error("Bot died")
    log.error(e)
    