import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

Client = discord.Client()
bot = commands.Bot(command_prefix="!")



@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------------------------")
    

@bot.event
async def on_message(message):
    if message.content.upper().startswith("HELLO"):
        await bot.delete_message(message)
        await bot.send_message(message.channel, "안녕하세요! {}".format(message.author.mention))
        await bot.send_message(message.channel, "Annyeonghaseyo! {}".format(message.author.mention))
    if message.content.upper().startswith("SAY"):
        await bot.delete_message(message)
        sungjae = message.content.split(" ")
        #sungjae[0] = SAY
        #sungjae[1] = Hi
        #sunjae[1:] = hi there
        await bot.send_message(message.channel, "%s" % (" ".join(sungjae[1:])))
    if message.content.upper().startswith('TEASE'):
        await bot.delete_message(message)
        sungjae = message.content.split(" ")
        #sungjae[0] = SAY
        #sungjae[1] = Hi
        #sunjae[1:] = hi there
        for text in range (5):
            await bot.send_message(message.channel, "%s" % (" ".join(sungjae[1:])))
    if message.content.upper().startswith('COMMANDS'):
        embed = discord.Embed(title= 'Commands: ', description= 'Commands you can use to trigger events', color=0x00ff00)
        embed.add_field(name='Say (Your message here)', value='Allows to repeat message', inline=False)
        embed.add_field(name='Tease (Your message here)', value='Allows to repeat message 5x', inline=False)
        embed.add_field(name='Dice', value='Allows to play roll dice game', inline=False)
        await bot.send_message(message.channel, 'So far these are all the commands we have for now: ', embed = embed)
        
    if message.content.upper().startswith('DICE'):
        embed = discord.Embed(title='Dice Game Rules', description='Whoever guessed the number closest to mine wins.', color=0x00ff00)
        embed.add_field(name='RollDice', value='reply with rolldice to begin', inline=False)
        await bot.send_message(message.channel, embed = embed)
                            
        
    if message.content.upper().startswith('ROLLDICE'):
        await bot.send_message(message.channel, '{} requested the Dice game. Guess a number from 1 to 6.'.format(message.author.mention))
                                                               
        def guess_check(m):
            return m.content.isdigit()

        guess = await bot.wait_for_message(timeout=30.0, author=message.author, check=guess_check)
        answer = random.randint(1, 6)
        if guess is None:
            await bot.send_message(message.channel, 'The game has been cancelled.')
            return
        if int(guess.content) == answer:
            await bot.send_message(message.channel, 'Dangsin-i olbaleunji(You are Correct :joy: :joy: )!')
        else:
            await bot.send_message(message.channel, 'Joesonghabnida(Sorry :sob: ). It is actually {}.'.format(answer))


          


bot.run("NDA2NTUxMzU0MDU2NzY5NTM3.DU0mWg.RMqqk4gZO9efVXLrfo6y0C0mJYc")




