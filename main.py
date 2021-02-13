import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def link(ctx):
    """sends the link to the webpage in chat!"""
    await ctx.send('https://pythonexplainedto.me')

@bot.command()
async def instagram(ctx):
    """sends the link to the instagram in chat!"""
    await ctx.send('https://www.instagram.com/pythonexplainedto.me/')

@bot.command()
async def facebook(ctx):
    """sends the link to the facebook in chat!"""
    await ctx.send('https://www.facebook.com/pythonexplainedtome.me/')

@bot.command()
async def twitter(ctx):
    """sends the link to the twitter in chat!"""
    await ctx.send('https://twitter.com/pythonexplained')

@bot.command()
async def github(ctx):
    """sends the link to the github in chat!"""
    await ctx.send('https://github.com/Phaugt')


bot.run('token')