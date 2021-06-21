#bot.py
import os
import dotenv
import discord

from time import sleep
from discord import Intents
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

from extensions.clear import clear_

print("ARKANET: BOOTING: Done!")
clear_()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
bot = Bot(command_prefix='sudo', intents=intents)
client = discord.Client(intents=intents)

#-----------------------------------------------------------------------------------------

# TODO: connecting syntax on all on_message(message) with elif      CHECK
# TODO: connect all on_raw_reaction_add(payload) with elif          CHECK
# TODO: Fix Add roles with Elif after if channel...                 CHECK
# TODO: on_raw_reaction_remove(payload) for all reaction roles
# TODO: make a auto !d bump for disboard bot every 2 hours
# TODO: su flag {flag - ctf} if input = variable ctf then add role
# TODO: Bot description: Plays Araknet reading TCP

#-----------------------------------------------------------------------------------------

print("ARKANET: Awaiting Action")

#Await $Hello -> Test message
@bot.command()
async def Hello(ctx):
    print("ARKANET: Hello got called")
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
            print("ARKANET: Updated!")
        else:
            print("ARKANET: ERROR: wrong context")
            pass
    else:
        print("ARKANET: ERROR: wrong channel id")
        pass
    
    
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
                    print("ARKANET: Member added") 
                else:
                    print("ARKANET: DEBUG: member is null")
                    pass
            else:
                print("ARKANET: DEBUG: role is null")
                pass
        else:
            print("ARKANET: DEBUG: not yes emoji")
            pass           
    elif  payload.channel_id == 855963293997989888 and payload.message_id == 855973402459373579:              
        if str(payload.emoji) == "<:europeanunionflag:855972418915663912>":
            message_id = payload.message_id
            guild_id = payload.guild_id
            guild = client.get_guild(guild_id) 
            role = get(payload.member.guild.roles, name='Europe')
            if role is not None:
                member = payload.member
                if member is not None:
                    await payload.member.add_roles(role)
                    print("ARKANET: Europe added")
                else:
                    print("ARKANET: DEBUG: member is null")
                    pass
            else:
                print("ARKANET: DEBUG: role is null")
                pass
        elif str(payload.emoji) == "<:america:855972648109735936>":
            message_id = payload.message_id
            guild_id = payload.guild_id
            guild = client.get_guild(guild_id) 
            role = get(payload.member.guild.roles, name='America')
            if role is not None:
                member = payload.member
                if member is not None:
                    await payload.member.add_roles(role)
                    print("ARKANET: America added")           
                else:
                    print("ARKANET: DEBUG: member is null")
                    pass
            else:
                print("ARKANET: DEBUG: role is null")
                pass      
        elif str(payload.emoji) == "<:asia:855966897349722122>":
            message_id = payload.message_id       
            guild_id = payload.guild_id
            guild = client.get_guild(guild_id) 
            role = get(payload.member.guild.roles, name='Asia')
            if role is not None:
                member = payload.member
                if member is not None:
                    await payload.member.add_roles(role)
                    print(f"Added {role} to {member}.")
                else:
                    print("ARKANET: DEBUG: member is null")
                    pass
            else:
                print("ARKANET: DEBUG: role is null")
                pass
        else:
            print("ARKANET: ERROR: [yes] [europe] [america] [asia]")
            pass    
    else:
         print("ARKANET: ERROR: No Statement")
         pass  


@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    if guild is not None:
        print("ARKANET: DEBUG: guild is not Null")
        member = get(guild.members, id=payload.user_id)
        if member is not None:
            print("ARKANET: DEBUG: member is not None")
            if payload.channel_id == 854826582639640626 and payload.message_id == 855579785408938002:
                if str(payload.emoji) == "<:yes:855447870466555914>":
                    role = get(guild.roles, name='Member')
                    if role is not None:
                        await member.remove_roles(role)
                        print(f"Removed {role} from {member}.")
                    else:
                        print("ARKANET: DEBUG: role is null")
                else:
                    print("ARKANET: ERROR: Unknown Emoji")
            else:
                print("ARKANET: ERROR: Unknown Channel")
        else:
            print("ARKANET: DEBUG member is null")
    else:
        print("ARKANET: DEBUG: guild is null")


'''@bot.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id == 854826582639640626 and payload.message_id == 855579785408938002:
        if str(payload.emoji) == "<:yes:855447870466555914>":
            message_id = payload.message_id
            guild_id = payload.guild_id
            guild = client.get_guild(guild_id) 
            role = get(payload.member.guild.roles, name='Member')
            if role is not None:
                member = payload.member
                if member is not None:
                    await payload.member.remove_roles(role)
                    print(f"Removed {role} from {member}.")'''
                    
'''if payload.channel_id == 854826582639640626 and payload.message_id == 855579785408938002:
        if str(payload.emoji) == "<:yes:855447870466555914>":
            guild = bot.get_guild(payload.guild_id)
            role = get(guild.roles, name='Member')
            if role is not None:
                print("DEBUG: role is not None")
                member = guild.get_member(payload.user_id)
                if member is not None:
                    print("DEBUG: member is not None")
                    await payload.member.remove_roles(role)
                    print(f"Removed {role} from {member}.")'''


#await payload.member.remove_roles(role)
bot.run(TOKEN)