import discord
import asyncio
import random
import commands

client = discord.Client()

standAbilityActivated = False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    #print(client.user.id)
    game = discord.Game("with time")

    await client.change_presence(status = discord.Status.online, activity = game)
    print('------')


@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return;
        #
    #Effectively King Crimson's power
    if standAbilityActivated:
        print("This is the power of my King Crimson")
        await commands.eraseTime(message)
        global standAbilityActivated = False
        await channel.send(file=discord.File('./resources/EraseTime.png'))

    #if the text should be parsed for a command
    if message.content.startswith("!"):
        #Help Command
        if message.content.lower().find("help") > -1:
            await commands.sendHelp(channel)
        #Angery face command
        elif message.content.lower().find("angerykc") > -1:
            await commands.sendKC(channel)
        #Hmm command
        elif message.content.lower().find("hmm") > -1:
            await commands.sendThunk(channel)
        #Erase time command
        elif message.content.lower().find("erase") > -1:
            await commands.eraseTime(message)
            global standAbilityActivated = True

        #Invalid message
        else:
            await channel.send('Invalid command. Type "!help" for a list of commands')


client.run('NTkyODk4NDM0MzQwNzQ5MzEz.XRGYDg.77FbXwZPipf-Q2k_TEcUVz8IPx8')
