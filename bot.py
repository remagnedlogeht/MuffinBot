import discord
from discord.ext import commands
from discord.utils import find
import logging
import json
import asyncio
import wordfilter
import random
import time
import cogs
from asyncio import sleep

bot = commands.AutoShardedBot(case_insensitive=True,
                              command_prefix=commands.when_mentioned_or('>'), 
                              shard_count=2, latency=1.5,
                              shard_ids=[*range(2)])
logging.basicConfig(level='INFO')
cogs = ['admin', 'util', 'mod', 'action', 'image', 'nsfw', 'fun',
        'meme', 'search', 'brawl']
bot.remove_command('help')
for i in cogs:
    bot.load_extension(f"cogs.{i}")

@bot.event
async def on_shard_ready(shard_id):
    print(f"Shard {shard_id} is loaded!")

@bot.event
async def on_ready():
    print("Done!")
    await bot.change_presence(activity=discord.Streaming(
        name=">help",
        url="https://www.twitch.tv/doggeryhdro"
        ))

@bot.event
async def on_disconnect():
    print("The bot is now sleeping... You can fucking restart me")

@bot.event
async def on_resumed():
    print("The bot is now running...")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.CommandOnCooldown):
        return await ctx.send(f'This command is on cooldown... **[{error.retry_after:.2f} seconds]**', delete_after=5)
    if isinstance(error, commands.NotOwner):
        return await ctx.send('**You tried an admin command? Just DON\'T DO IT!**')
    if isinstance(error, commands.MissingPermissions):
        return await ctx.send('**You are missing permission to execute this command!**')
    if isinstance(error, commands.BotMissingPermissions):
        return await ctx.send('**I am missing permission to perform this command!**')
    await ctx.send(error)
         

@bot.event
async def on_guild_join(guild):
        berp = f'**Thanks for adding me! <a:meow:464800509677797379>\nMy prefix is `>` Use `>help` for list commands!**'
        general = find(lambda x: x.name == 'general',  guild.text_channels)
        general2 = find(lambda x: x.name == 'chat',  guild.text_channels)
        general3 = find(lambda x: x.name == 'lounge',  guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            return await general.send(berp)
        elif general2 and general2.permissions_for(guild.me).send_messages:
            return await general.send(berp)
        elif general3 and general3.permissions_for(guild.me).send_messages:
            return await general.send(berp)


        

with open('data/config.json') as f:
    r = json.load(f)
    bot.run(r['token'])
    f.close()
