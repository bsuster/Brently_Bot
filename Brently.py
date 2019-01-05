import discord
from discord.ext import commands
import random
import webCrawler
import asyncio
import Wiki

bot = commands.Bot(command_prefix='!')

server = discord.Server(id='530909195873026051')


@bot.event
async def on_message(message):

 # we do not want the bot to reply to itself
    if message.author == bot.user:

        return

# greeting message
    if message.content.upper().startswith('!HELLO'):

        msg = 'You have much wang! {0.author.mention}'.format(message)

        await bot.send_message(message.channel, msg)

# kick user command
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
# ban hammer
    if message.content.upper().startswith('!BAN'):
        ban_membs = bot.get_all_members()
        print(message.content)
        for ban_mem in ban_membs:
            print(ban_mem.name)
            print(message.content[5:])
            if ban_mem.name == message.content[5:]:
                try:
                    await bot.ban(ban_mem)
                    await bot.say('I will bring down the mighty BANHAMMER upon them my lord!')
                except:
                    pass

    # unban command
    if message.content.upper().startswith('!UNBAN'):
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

bot.run('NTMxMTg1NDAxMjU2MjE0NTMx.DxKRew.aPN0QaQujKS9mS794NKXCry0kwc')