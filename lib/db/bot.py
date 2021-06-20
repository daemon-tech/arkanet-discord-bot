#bot.py
import os
import dotenv
import discord

from time import sleep
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

from extensions import clear

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = Bot(command_prefix='$', intents=intents)
client = discord.Client(intents=intents)

# TODO: connecting syntax on all on_message(message) with elif  CHECK
# TODO: connect all on_raw_reaction_add(payload) with elif      CHECK
# TODO: make a auto !d bump for disboard bot every 2 hours

#Await $Hello -> Test message
@bot.command()
async def Hello(ctx):
    await ctx.send("Hello! 👋")

#Send Embed Message in Channel Roles
@bot.event
async def on_message(message):
    if message.channel.id == 854826582639640626:
        if message.content.startswith('Roles'):
            embedvar = discord.Embed(title="React to this Emoji!",
                                     description="Click the corresponding emoji to accept the rules.\n<:yes:855447870466555914> "
                                                    "- Member", color=0x00ff00)
            await message.channel.send(embed=embedvar)
            print("Changed message embed color.")
        elif message.content.startswith('update'):
            embedvar2 = discord.Embed(title="React to this Emoji!",
                                      description="Click the corresponding emoji to accept the rules. \n<:yes:855447870466555914> "
                                                    "- Member", color=0x00ff00)
            channel = client.get_channel(854826582639640626)
            msg = await channel.fetch_message(855579785408938002)
            await msg.edit(embed=embedvar2)
            print("Updated: Embed Role Message")
            await message.channel.send("Updated: Embed Role Message")
            
            
    elif message.channel.id == 855963293997989888:
        if message.content.startswith('$rolemenu'):
            embedvar = discord.Embed(title="React to this message to get your roles!",
                                     description="Click the corresponding emoji to receive your role.\n<:europeanunionflag:855972418915663912>"
                                                    "- Europe\n<:america:855972648109735936> "
                                                    "- America\n<:asia:855966897349722122> "
                                                    "- Asia", color=0x00ff00)
            await message.channel.send(embed=embedvar)
            print("Changed message embed color.")
        elif message.content.startswith('refresh'):
            embedvar2 = discord.Embed(title="React to this message to get your roles!",
                                     description="Click the corresponding emoji to receive your role.\n<:europeanunionflag:855972418915663912> "
                                                    "- Europe\n<:america:855972648109735936> "
                                                    "- America\n<:asia:855966897349722122> "
                                                    "- Asia", color=0x00ff00)
            channel = client.get_channel(855963293997989888)
            msg = await channel.fetch_message(855973402459373579)
            await msg.edit(embed=embedvar2)
            print("Updated!")
    else:
        return
    

#on_raw_reaction_add add role for Member; EUROPE; AMERICA; ASIA 
@bot.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 854826582639640626 and payload.message_id == 855579785408938002:
        if str(payload.emoji) == "<:yes:855447870466555914>":
            message_id = payload.message_id
            guild_id = payload.guild_id
            guild = client.get_guild(guild_id) 
            role = get(payload.member.guild.roles, name='Member')
            if role is not None:
                member = payload.member
                if member is not None:
                    await payload.member.add_roles(role)
                    print("Member added")
                    
                    
    elif payload.channel_id == 855963293997989888 and payload.message_id == 855973402459373579:
        if str(payload.emoji) == "<:europeanunionflag:855972418915663912>":
            message_id = payload.message_id
            guild_id = payload.guild_id
            guild = client.get_guild(guild_id) 
            role = get(payload.member.guild.roles, name='Europe')
            if role is not None:
                member = payload.member
                if member is not None:
                    await payload.member.add_roles(role)
                    print("Europe added") 
                    
                    
    elif payload.channel_id == 855963293997989888 and payload.message_id == 855973402459373579:
        if str(payload.emoji) == "<:america:855972648109735936>":
            message_id = payload.message_id
            guild_id = payload.guild_id
            guild = client.get_guild(guild_id) 
            role = get(payload.member.guild.roles, name='America')
            if role is not None:
                member = payload.member
                if member is not None:
                    await payload.member.add_roles(role)
                    print("America added")
                    
                    
    elif payload.channel_id == 855963293997989888 and payload.message_id == 855973402459373579:
        if str(payload.emoji) == "<:asia:855966897349722122>":
            message_id = payload.message_id       
            guild_id = payload.guild_id
            guild = client.get_guild(guild_id) 
            role = get(payload.member.guild.roles, name='Asia')
            if role is not None:
                member = payload.member
                if member is not None:
                    await payload.member.add_roles(role)
                    print("Member added")
                    
                    
    else:
        print("ERROR: Role not found")
        pass
    
 
@bot.event
async def on_member_join(member):
    channel = client.get_channel(854826568361443328)
    await channel.send('Welcome {} 👋'.format(member))

bot.run(TOKEN)