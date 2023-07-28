import discord
from discord.ext import commands
import os 

intents = discord.Intents.all()
client = commands.Bot(command_prefix = 'mango ', intents=intents)

WORKINGDIR = "/home/josh/Documents/Code/Python/MangoAddons/"

@client.event
async def on_ready():
    channel = client.get_channel(1133918295574184017)
    await channel.send("MangoAddons Terminal - BOOT")

@client.command()
async def commands(ctx):
    await ctx.send("Run a module by running 'mango run name', run 'mango listmods' to see a list of mods")

@client.command()
async def run(ctx, mod):
    mod = str(mod+".py")
    if os.path.isfile(WORKINGDIR+mod):
        await ctx.send("Executing File...")
        os.system("python3 "+WORKINGDIR+mod+" & disown")
    else:
        pass

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def say(ctx, *, args):
    os.system('espeak "' +args+ '" & disown')

TOKEN = "MTEwNzY4MDI2Nzg3Njk2MjQzNQ.G86jqQ.S793nNWlPkhtEOTVKYVZctwBYSQ7U2mLL0nbWI"
client.run(TOKEN)