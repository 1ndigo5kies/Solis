from xml.dom.expatbuilder import theDOMImplementation
import discord
from discord.ext import commands
import os

DISCORD_TOKEN = "OTY5NjAzMDE5MzM3NTIzMjMw.YmvzLg.7eLddBWFMsJkEUJ86JxqCF2vxlA"

bot = discord.Client()

@bot.event
async def on_ready():
   print('solis ready for intake of commands.')

bot = commands.Bot(command_prefix='sol!')

@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)

@bot.event
async def on_message(message):
    if message.content == "im kool":

        if message.author.id == 638842500924309568:
            await message.channel.send("hi swag gamer")

        elif message.author.id == 636201316577837066:
            await message.channel.send("sorry u arent kool u are a nerd")

        else:
            await message.channel.send("who... are you..")

@bot.command()
async def interview(ctx):
    user = ctx.author
#system name
    message = "Welcome to your Solar Systems interview! \nTo begin, What is your name\system name?"
    await user.send(message)
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check, timeout=120)
    name = message.content
    
#tag
    message = "What is your system tag? (for if you use proxies otherwise say N/A)"
    await user.send(message)
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check, timeout=120)
    tag = message.content

#age
    message = "What is your age? (minor/adult is fine)"
    await user.send(message)
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check, timeout=120)
    age = message.content
#opinion
    message = "How do you feel about other system origins, like endogenic systems, tulpas, and mixed origin systems?"
    await user.send(message)
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check, timeout=120)
    opinion = message.content

#systype
    message = "Are you a singlet or a system?"
    await user.send(message)
    def check(m):
        return m.author.id == ctx.author.id
    message = await bot.wait_for('message', check=check, timeout=120)
    systype = message.content

#send to log
    channel = bot.get_channel(969654290245369877)
    await channel.send("**__name:__**")
    await channel.send(name)
    await channel.send("**__tag:__**")
    await channel.send(tag)
    await channel.send("**__age:__**")
    await channel.send(age)
    await channel.send("**__opinion on endogenic etc:__**")
    await channel.send(opinion)
    await channel.send("**__system?:__**")
    await channel.send(systype)
    await channel.send("**__user:__**")
    await channel.send(user)
    await channel.send(ctx.author.id)
    

bot.run(DISCORD_TOKEN)