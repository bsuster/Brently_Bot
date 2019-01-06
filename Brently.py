import discord
from discord.ext import commands
import random
import webCrawler
import asyncio
import Wiki
import datetime

players = []
all_members = []
bot = commands.Bot(command_prefix='!')
server = discord.Server(id='530909195873026051')


class player:
    def __init__(self,name,  time_joined = datetime.datetime.now(), time_leave=None):
        self.name = name
        self.time_joined = time_joined
        self.time_leave = time_leave


@bot.event
async def on_message(message):

 # we do not want the bot to reply to itself
    x = random.randint(1, 10)
    if x == 5:
        print('Nowlin Encouragement')
        y = random.randint(1, 5)
        if y == 1:
            await bot.send_message(message.channel, 'Why are you using Python you moron?')
        if y == 2:
            await bot.send_message(message.channel, 'How about you use code that actually works?')
        if y == 3:
            await bot.send_message(message.channel, 'YOU SHOULD USE ASSEMBLY!')
        if y == 4:
            await bot.send_message(message.channel, 'You are a disgrace to humanity for even thinking of using Python')
        if y == 5:
            await bot.send_message(message.channel, 'WHYY?!?!?!?!')
        return

    if message.author == bot.user:

        return

# greeting message
    if message.content.upper().startswith('!HELLO'):

        msg = 'You have much wang! {0.author.mention}'.format(message)

        await bot.send_message(message.channel, msg)

# kick user command
    if message.content.upper().startswith('!KICK') and message.author.permissions_in(message.channel).administrator:
        membs = bot.get_all_members()
        print(message.content)
        for mem in membs:
            print(mem.name)
            print(message.content[6:])
            if mem.name == message.content[6:]:
                print("attempting to kick")
                await bot.kick(mem)
                break
# ban hammer
    if message.content.upper().startswith('!BAN') and message.author.permissions_in(message.channel).administrator:
        ban_membs = bot.get_all_members()
        print(message.content)
        try:
            for ban_mem in ban_membs:
                print(ban_mem.name)
                print(message.content[5:])
                if ban_mem.name == message.content[5:]:
                    await bot.ban(ban_mem)
                    await bot.send_message(message.channel, 'I will bring down the mighty BANHAMMER upon them my lord!')
        except:
            pass

    # unban command
    if message.content.upper().startswith('!UNBAN') and message.author.permissions_in(message.channel).administrator:
        users = await bot.get_bans(server)
        print(users)
        for u in users:
            print(u)
            if u.name == message.content[7:]: # ADD NAME HERE:
                await bot.unban(server, u)

    # meme gen command
    if message.content.upper().startswith('!MEME'):
        meme = webCrawler.get_meme()
        await bot.send_message(message.channel, meme)

        # wiki logic
    if message.content.upper().startswith("!WIKI"):
        msg = await bot.send_message(message.channel, 'Retrieving...')
        command = message.content[6:]
        url = Wiki.search(command)
        await bot.edit_message(msg, url)

    # yt
    if message.content.upper().startswith("!YT"):
        msg = await bot.send_message(message.channel, 'Retrieving...')
        command = message.content[4:]
        url = YouTube.search(command)
        await bot.edit_message(msg, url)

    # log
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


    if message.content.upper().startswith('!THANOS') and message.author.permissions_in(message.channel).administrator:
        members_all = bot.get_all_members()
        await bot.send_message(message.channel, "I don't feel soo good.")
        for z in members_all:
            rand_int = random.randint(0, 1)
            if rand_int == 0:
                continue
            if rand_int == 1:
                await bot.kick(z)

    '''if message.content.upper().startswith('!CLEAR'):
        print('Clearing...')
        await bot.send_message(message.channel, 'Clearing messages...')
        list_size = len(bot.get_all_messages)
        while list_size > 0:
            await bot.delete_messages(msg)
            list_size -= 1'''

    # mute command
    '''if message.content.upper().startswith("!MUTE"):
        mute_members = bot.get_all_members()
        for mute_mem in mute_members:
            print(mute_mem)
            if mute_mem.name == message.content[6:]: #and message.author.server_permissions.administrator:
                await bot.mute(mute_mem)
                return'''
'''@bot.command()
async def mute(ctx, member : discord.Member = None):
    if member is None:
        await ctx.send('Please pass in a valid user')
        return
        await member.add_roles('ADMIN')
        await ctx.send(f'{str(member)} was muted!')'''


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

bot.run('NTMxMTg1NDAxMjU2MjE0NTMx.DxKRew.aPN0QaQujKS9mS794NKXCry0kwc')