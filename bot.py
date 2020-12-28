from inspect import cleandoc
import os
import discord

from dotenv import load_dotenv
import  data
import quotes


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
GUILD_ID = int(os.getenv('GUILD_ID'))
BODA_ID = int(os.getenv('BODA_ID'))
intents = discord.Intents.all()
client = discord.Client(intents = intents)


keywords = ['boda', 'bb']




guil = me = None


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    global guild
    global me
    guild = client.get_guild(GUILD_ID)
    me = client.get_user(BODA_ID)
    
   



# @client.event
# async def on_typing(channel, user, when):
#         if channel.name != os.getenv('TEST_CHANNEL'):
#             return
#         await channel.send(f'I see you typing {user.nick}')



@client.event   
async def on_message(message):
    if  message.author.bot == True:
        return
    # # enables bot in test cahnnel only 
    # if message.channel.name != os.getenv('TEST_CHANNEL'):
    #     return

    
    # if im not online, then send this message and mention me 
    if guild.get_member(BODA_ID).status != discord.Status.online:
        for x in keywords:
            if x in message.content.lower():
                await message.channel.send(f"I'm not here right now! This is my bot responding on my behalf, I will make sure to mention boda so he gets ur message when he is back, Cheers \n  {message.author.nick} is Mentioning you {discord.utils.get(client.get_all_members(), name='Boda').mention} ")   
    
   
   
   
    if message.content.startswith('$get joke'):
        await message.channel.send(quotes.get_joke())
    elif message.content.startswith('$get dad joke'):
        await message.channel.send(quotes.get_dad_joke())
    elif message.content.startswith('$get quote'):
        await message.channel.send(quotes.get_quote())


client.run(TOKEN)