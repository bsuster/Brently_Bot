import discord
from discord.ext import commands
import random
import datetime
import webCrawler
import asyncio
players = []
all_members = []
bot = commands.Bot(command_prefix='!')
token = 'U AINT GETTING THE TOKEN THIS TIME'


class player:
    def __init__(self,name,  time_joined = datetime.datetime.now(), time_leave = None):
        self.name = name
        self.time_joined = time_joined
        self.time_leave = time_leave

@bot.event
async def on_message(message):

    # we do not want the bot to reply to itself
    if message.author == bot.user:

        return

    if message.content.upper().startswith('!HELLO'):


        msg = 'Screw you! {0.author.mention}'.format(message)

        await bot.send_message(message.channel, msg)

    if message.content.upper().startswith('!KICK'):
        membs = bot.get_all_members()
        print(message.content)
        for mem in membs:
            print(mem.name)
            print(message.content[6:])
            if mem.name == message.content[6:]:
                print("attempting to kick")
                await bot.kick(mem)
                break
    if message.content.upper().startswith('!leave'):
        msg = 'Bye! Im outta here!'.format(message)
        await bot.send_message(message.channel, msg)
        await bot.close()
    if message.content.upper().startswith('!SLAP'):
        members_all = bot.get_all_members
        author = str(message.author.name)
        await bot.send_message(message.channel, author + " has slapped " + message.content[6:])

    if message.content.upper().startswith('!LOG'):
        members_all = bot.get_all_members()

        msg = message.content[5:] + ' has been online for '
        offline_msg = message.content[5:] + ' logged off at '
        playername = message.content[5:]
        for z in players:
            if z.name == playername:
                break
                
                ##print(message.content[5:])
        for i in members_all:
            if playername == i.name:
                if i.status == discord.Status.online:
                    time_on = str(datetime.datetime.now() - z.time_joined)
                    await bot.send_message(message.channel, msg + time_on[0:7])
                if i.status == discord.Status.offline:
                    time_left = z.time_leave
                    await bot.send_message(message.channel, offline_msg + str(time_left))

    if message.content.upper().startswith('!BAN'):
        ban_membs = bot.get_all_members()
        print(message.content)
        for ban_mem in ban_membs:
            print(ban_mem.name)
            print(message.content[5:])
            if ban_mem.name == message.content[5:]:
                await bot.ban(ban_mem)
                msg = 'I will bring down the mighty BANHAMMER upon them my lord!'.format(message)
                await bot.send_message(message.channel, msg)
                break
    if message.content.upper().startswith('!clearall'):
        print("steeee")


    #adding command for meme
    if message.content.upper().startswith("!MEME"):
        meme = webCrawler.get_meme()
        await bot.send_message(message.channel, meme)

@bot.event
async def on_ready():

    print('Logged in as')

    print(bot.user.name)

    print(bot.user.id)

    print('------')

    members_all = bot.get_all_members()

    for i in members_all:
        if i.status == discord.Status.online:
            print(i.name)
            p = player(str(i.name))
            players.append(p)
    
        

        




bot.run(token)

@bot.event
@asyncio.coroutine
async def on_member_update(before, after):
   if before.status != after.status:
       if before.status == discord.Status.offline and after.status == discord.Status.online:
           p = player(after.name)
           players.append(p)
       if before.status == discord.Status.online and after.status == discord.Status.offline:
            for i in players:
                if i.name == after.name:
                    time_leave = datetime.datetime.now()
                    i.time_leave = time_leave 


