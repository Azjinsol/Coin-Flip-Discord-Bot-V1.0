"""
@author: Neomunuke
"""

import discord
from discord.ext import commands
import os
from coinflip import flipCoin
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    print('Bot ID: {}'.format(client.user.id))
    await client.change_presence(activity=discord.Game(name="$flip"))

@client.command()
async def flip(ctx):
    if flipCoin() == "Heads":
        embed=discord.Embed(
        title="Flipping...",
            color=discord.Color.blue())
        embed.set_thumbnail(url='https://c.tenor.com/nEu74vu_sT4AAAAC/heads-coinflip.gif')
        await ctx.send(embed=embed)
    elif flipCoin() == "Tails":
        embed=discord.Embed(
        title="Flipping...",
            color=discord.Color.blue())
        embed.set_thumbnail(url='https://c.tenor.com/kK8D7hQXX5wAAAAC/coins-tails.gif')
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(
        title="ERROR 404", 
            color=discord.Color.blue())
        #embed.set_author(name=ctx.author.display_name)
        #embed.set_image(url='https://c.tenor.com/kK8D7hQXX5wAAAAC/coins-tails.gif')
        await ctx.send(embed=embed)
       
@client.command()
async def fliphelp(ctx):
    await ctx.send("$flip - flipping the coin")

keep_alive()

client.run(os.getenv('TOKEN'))
