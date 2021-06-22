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


clear_()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
activity = discord.Activity(name='TCP', type=discord.ActivityType.watching)
bot = Bot(command_prefix="$", intents=intents, activity=activity)
client = discord.Client(intents=intents)
channel_sudo = client.get_channel(856434834900254731)

print("ARKANET: Configuration loaded")
print("ARKANET: Awaiting Action")

#listener on on_ready
@bot.event
async def on_ready():
    channel_sudo = bot.get_channel(856434834900254731)
    await channel_sudo.send(f"ARKANET: Successfully Booted")

#listener on_message
@bot.event
async def on_message(message):
    channel_sudo = bot.get_channel(856434834900254731)
    #member reaction embed
    if message.channel.id == 854826582639640626:
        if message.content.startswith('$Roles'):
            embedvar = discord.Embed(title="React to this Emoji!",
                                     description="Click the corresponding emoji to accept the rules.\n<:yes:855447870466555914> "
                                                    "- Member", color=0x00ff00)
            await message.channel.send(embed=embedvar)
            print("Changed message embed color.")
        #member reaction embed update    
        elif message.content.startswith('update'):
            embedvar2 = discord.Embed(title="React to this Emoji!",
                                      description="Click the corresponding emoji to accept the rules. \n<:yes:855447870466555914> "
                                                    "- Member", color=0x00ff00)
            channel = client.get_channel(854826582639640626)
            msg = await channel.fetch_message(855579785408938002)
            await msg.edit(embed=embedvar2)
            print("Updated: Embed Role Message")
            await message.channel.send("Updated: Embed Role Message")
    #self role continetal         
    elif message.channel.id == 855963293997989888:
        if message.content.startswith('$rolemenu'):
            embedvar = discord.Embed(title="React to this message to get your roles!",
                                     description="Click the corresponding emoji to receive your role.\n<:europeanunionflag:855972418915663912>"
                                                    "- Europe\n<:america:855972648109735936> "
                                                    "- America\n<:asia:855966897349722122> "
                                                    "- Asia", color=0x00ff00)
            await message.channel.send(embed=embedvar)
            print("Changed message embed color.")
        #self fole continental update    
        elif message.content.startswith('$refresh'):
            embedvar2 = discord.Embed(title="React to this message to get your roles!",
                                     description="Click the corresponding emoji to receive your role.\n<:europeanunionflag:855972418915663912> "
                                                    "- Europe\n<:america:855972648109735936> "
                                                    "- America\n<:asia:855966897349722122> "
                                                    "- Asia", color=0x00ff00)
            channel = client.get_channel(855963293997989888)
            msg = await channel.fetch_message(855973402459373579)
            await msg.edit(embed=embedvar2)
            print("ARKANET: Updated!")
        #role message
        elif message.content.startswith('$su roles custom'):
            await message.channel.send("Click on the corresponding emoji to receive your role. \n"
                                        "<:python:855966141083680798> - Python"
                                        "<:exe:855966140717989899> - Script Kiddie"
                                        "<:3225_kali:855904540154134539> - Kali Linux"
                                        "<:java:855966141092331530> - Java")
            await channel_sudo.send("ARKANET: display su roles custom in channel <855963293997989888>")
        else:
            print("ARKANET: DEBUG: Wrong Context")
            
    elif message.channel.id == 856434834900254731:
        if message.content == "su help":
            embedhelp = discord.Embed(title ='ARKANET $ ~su help',
                                      description = "🔍COMMANDS  |  'cmd list'\n"
                                                            "📁 FILESYSTEM  |  'ls -a '\n"
                                                            "♻️ REBOOT  |  'self reboot'",  color=0x00ff00)
            await channel_sudo.send(embed=embedhelp)
            
        elif message.content == "su cmd list":
            embedcmd = discord.Embed(title ='ARKANET $ ~su cmd list',
                                     description = "🔍 IP WHOIS | whois [ip]", color=0x00ff00)
            await channel_sudo.send(embed=embedcmd)
           
        elif message.content == "su self reboot":
            print("ARKANET: REBOOTING")
            await channel_sudo.send(f"ARKANET: REBOOTING")
            os.system("python3 reboot.py")
            
        elif message.content.startswith('su'):
            await channel_sudo.send(f"ARKANET: ~ su [arg1] example: help")
            
        else:
            pass
    else:
        pass
    
#on_raw_reaction_add 
@bot.event
async def on_raw_reaction_add(payload):
    channel_sudo = bot.get_channel(856434834900254731)
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
                    await channel_sudo.send(f"ARKANET: Added {role} to {member}.")
                    print(f"ARKANET: Added {role} to {member}.")
                    
                else:
                    print("ARKANET: DEBUG: member is null")
                    await channel_sudo.send(f"ARKANET: DEBUG: member is null")
                    pass
            else:
                print("ARKANET: DEBUG: role is null")
                await channel_sudo.send(f"ARKANET: DEBUG: role is null")
                pass
        else:
            print("ARKANET: DEBUG: not yes emoji")
            await channel_sudo.send(f"ARKANET: DEBUG: not yes emoji")
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
                    print(f"ARKANET: Added {role} to {member}.")
                    await channel_sudo.send(f"ARKANET: Added {role} to {member}.") 
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
                    print(f"ARKANET: Added {role} to {member}.")
                    await channel_sudo.send(f"ARKANET: Added {role} to {member}.")            
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
                    await channel_sudo.send(f"ARKANET: Added {role} to {member}.")
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
         await channel_sudo.send(f"ARKANET: ERROR: No Statement")
         pass  

#on_raw_reaction_remove 
@bot.event
async def on_raw_reaction_remove(payload):
    channel_sudo = bot.get_channel(856434834900254731)
    guild = bot.get_guild(payload.guild_id)
    if guild is not None:
        member = get(guild.members, id=payload.user_id)
        if member is not None:
            if payload.channel_id == 854826582639640626 and payload.message_id == 855579785408938002:
                if str(payload.emoji) == "<:yes:855447870466555914>":
                    role = get(guild.roles, name='Member')
                    if role is not None:
                        await member.remove_roles(role)
                        print(f"Removed {role} from {member}.")
                        await channel_sudo.send(f"ARKANET: Removed {role} from {member}.")
                    else:
                        print("ARKANET: DEBUG: role is null")
                else:
                    print("ARKANET: ERROR: Unknown Emoji")
            elif  payload.channel_id == 855963293997989888 and payload.message_id == 855973402459373579:
                if str(payload.emoji) == "<:europeanunionflag:855972418915663912>":
                    role = get(guild.roles, name='Europe')
                    if role is not None:
                        await member.remove_roles(role)
                        print(f"Removed {role} from {member}.")
                        await channel_sudo.send(f"ARKANET: Removed {role} from {member}.")
                    else:
                        print("ARKANET: DEBUG: role is null")
                elif str(payload.emoji) == "<:america:855972648109735936>":
                    role = get(guild.roles, name='America')
                    if role is not None:
                        await member.remove_roles(role)
                        print(f"Removed {role} from {member}.")
                        await channel_sudo.send(f"ARKANET: Removed {role} from {member}.")
                    else:
                        print("ARKANET: DEBUG: role is null")
                elif str(payload.emoji) == "<:asia:855966897349722122>":
                    role = get(guild.roles, name='Asia')
                    if role is not None:
                        await member.remove_roles(role)
                        print(f"Removed {role} from {member}.")
                        await channel_sudo.send(f"ARKANET: Removed {role} from {member}.")
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

bot.run(TOKEN)
