import discord
from discord.ext import commands
import os
import time
import asyncio

intents = discord.Intents.all()
client = commands.Bot(command_prefix = 'mango ', intents=intents)

CHANNEL_ID = 1136020828195127406
WORKINGDIR = "NULL"
TOKEN = "MTEwNzY4MDI2Nzg3Njk2MjQzNQ.GlkaYy.-xpS3vNzY-K5RD_z7SeWcMK4J4zHGR2Zo2O9TY"

@client.event
async def on_ready():
    channel = client.get_channel(1136020828195127406)
    await channel.send("i only talk through bot now")
    '''
    await channel.send("MangoAddons, programmed by @joshubruh")
    await channel.send("Run 'mango help' for assistance on usage")
    '''

@client.command()
async def commands(ctx):
    await ctx.send("Run a module by running 'mango run name', run 'mango listmods' to see a list of mods")

@client.command()
async def listmods(ctx):
    await ctx.send("Current Mods: clay_flipper, baz_flip")
    await ctx.send("For documentation on the modules, refer to the README")

@client.command()
async def LBogo(ctx):
    while True:
        await ctx.send("Get fucked <@1123798472336879676>")
        time.sleep(1)

@client.command()
async def shutup(ctx):
    await ctx.send("Shutting down uwu big daddy")
    exit()

@client.command()
async def run(ctx, mod):
    mod = str(mod+".py")
    if os.path.isfile(WORKINGDIR+mod):
        await ctx.send("Started Executing Module: "+mod)
        os.system("python3 "+WORKINGDIR+mod+" & disown")
    else:
        pass

client.run(TOKEN)