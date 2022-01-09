# bot.py
import os
import discord
import random
import time
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')


alert_channels=[929095736329666662]
#bot test

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Bot is ready to be used')
   # after it is ready do it
    for guild in bot.guilds:
        print(guild)
        print(guild.id)


@bot.command(name='buy')
@commands.has_role('Local')
async def buy_order(ctx, date, ticker, strike, CoP, price, image=None):
    embed=discord.Embed(title="BTO", description=date+" "+ticker+" "+strike+CoP+" @"+price, color=0x00FF00)
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='Local Alerts')
        for channel in guilds.channels:
            if(channel.id in alert_channels):
            #if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed)
   
@bot.command(name='sell')
@commands.has_role('Local')
async def sell_order(ctx, date, ticker, strike, CoP, price, image=None):
    embed=discord.Embed(title="STC"+ " "+ perc+"%", description=date+" "+ticker+" "+strike+CoP+" @"+price, color=0xFF5733)
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='Local Alerts')
        for channel in guilds.channels:
            if(channel.id in alert_channels):
            #if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed)

@bot.command(name='msg')
@commands.has_role('Local')
async def message(ctx, txt, image=None):
    embed=discord.Embed(description=txt, color=0xFFFFFF)
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='Local Alerts')
        for channel in guilds.channels:
            if(channel.id in alert_channels):
            #if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed)

@bot.command(name='trim')
@commands.has_role('Local')
async def trim(ctx, ticker, price):
    embed=discord.Embed(description="Trim "+ticker+" @"+price, color=0xFF5733)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='Local Alerts')
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                #if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed) 

@bot.command(name='cut')
@commands.has_role('Local')
async def cut(ctx, ticker, price):
    embed=discord.Embed(description="CUT "+ticker+" @"+price, color=0xFF5733)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='Local Alerts')
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                #if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed)

@bot.command(name='out')
@commands.has_role('Local')
async def cut(ctx, ticker, price):
    embed=discord.Embed(description="All out "+ticker+" @"+price, color=0xFF5733)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='Local Alerts')
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                #if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed)
bot.run(TOKEN)