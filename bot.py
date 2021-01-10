from inspect import cleandoc
import os
import discord
from discord.colour import Color

from dotenv import load_dotenv
from wikipedia.wikipedia import summary
import  data
import quotes


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
GUILD_ID = int(os.getenv('GUILD_ID'))
BODA_ID = int(os.getenv('BODA_ID'))
intents = discord.Intents.all()
client = discord.Client(intents = intents)

keywords_boda = ['boda', 'abdelrahman']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    global guild
    guild = client.get_guild(GUILD_ID)
    
    
  


@client.event   
async def on_message(message):
    # doesn't listen to messgaes sent by the bot itself 
    if  message.author.bot == True:
        return

    # # enables bot in test cahnnel only 
    # if message.channel.name != os.getenv('TEST_CHANNEL'):
    #     return

    
    await mention_user(message,guild=guild,member_id=BODA_ID,keywords=keywords_boda)   
    
   
   
   
    if message.content.startswith('$get joke'):
        await message.channel.send(quotes.get_joke())
    elif message.content.startswith('$get dad joke'):
        await message.channel.send(quotes.get_dad_joke())
    elif message.content.startswith('$get quote'):
        await message.channel.send(quotes.get_quote())
    elif message.content.startswith('$wiki'):
        keyword = message.content.split('$wiki',1)[1]
        title,summary,url, image = quotes.get_wiki(keyword)
        
        embed = discord.Embed(title=title, 
        color = discord.Color.dark_purple(),
        description = summary,
        url = url)
        if image is not None:
           embed.set_thumbnail(url = image) 
           

        await message.channel.send(content=None, embed = embed)


async def mention_user(message, guild,member_id, keywords):
    """ mentions a member if he/she is not online.
        You can customize the message as you want!
        @param:
            message: the message 
            guild: guild object 
            member_id: the member id that you want to mention
            keywords: the keywords that refer to the member, if any of them found in the 
                      message, the bot will mention the member
    """
    member = guild.get_member(member_id)
    if member.status != discord.Status.online:
        for x in keywords:
            if x in message.content.lower():
                await message.channel.send(f"I'm not here right now! This is my bot responding on my behalf, I will make sure to mention {member.name} so he gets ur message when he/she is back, Cheers! \n  {message.author.nick} is Mentioning you {member.mention} ")


client.run(TOKEN)