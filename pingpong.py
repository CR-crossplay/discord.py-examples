# *=== needed for discord ===*
import discord 
from discord.ext import commands 
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio

# Create a bot with ! for prefix.
client = commands.Bot(command_prefix="!")



@client.command(pass_context=True,name="ping", aliases=["pong","pingpong"]) #Registering a new command with name ping and also pong and pingpong.
async def ping(ctx): #command function
    await ctx.send("pong !"); #send the message pong

@client.event
async def on_ready():
    print("Bot Ready.") #In the console, we will see "bot ready"
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Cool Music")) #On change la presence du bot.
