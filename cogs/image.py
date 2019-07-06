import discord
from discord.ext import commands
import random
import json
import random
import asyncio
import io
import aiohttp
from discord import Webhook, RequestsWebhookAdapter
import requests
import os

API = os.getenv("dmTOKEN")
class Images(commands.Cog):
    """Looks like photoshop commands, but I like that"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=bot.loop)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blurple(self, ctx, member: discord.Member=None):
        """Blurple is life"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/beta/blurple?avatar={member.avatar_url_as(format='jpg', size=512)}") as resp:
                if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                data = io.BytesIO(await resp.read())
                await msg.delete()
                await ctx.send(file=discord.File(data, 'blurple.png'))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pixelate(self, ctx, member: discord.Member=None):
        """Your avatar looks like in 1980"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/beta/pixelate?avatar={member.avatar_url_as(format='jpg', size=512)}") as resp:
                if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                data = io.BytesIO(await resp.read())
                await msg.delete()
                await ctx.send(file=discord.File(data, 'pixelate.png'))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def spin(self, ctx, member: discord.Member=None):
        """Move as spin your avatar"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/beta/spin?avatar={member.avatar_url_as(format='jpg', size=512)}") as resp:
                if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                data = io.BytesIO(await resp.read())
                await msg.delete()
                await ctx.send(file=discord.File(data, 'spin.gif'))

    @commands.command(aliases=['trigger'])
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def triggered(self, ctx, member: discord.Member=None):
        """Triggered!!!!"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dankmemer.services/api/trigger?avatar1={member.avatar_url_as(format='jpg', size=512)}", headers={'Authorization': API}) as resp:
                 if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                 data = io.BytesIO(await resp.read())
                 await msg.delete()
                 await ctx.send(file=discord.File(data, 'triggered.gif'))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def deepfry(self, ctx, member: discord.Member=None):
        """bruh"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dankmemer.services/api/deepfry?avatar1={member.avatar_url_as(format='jpg', size=512)}", headers={'Authorization': API}) as resp:
                 if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                 data = io.BytesIO(await resp.read())
                 await msg.delete()
                 await ctx.send(file=discord.File(data, 'deepfry.png'))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def radialblur(self, ctx, member: discord.Member=None):
        """Woooooaaaahhhhhhh"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dankmemer.services/api/radialblur?avatar1={member.avatar_url_as(format='jpg', size=512)}", headers={'Authorization': API}) as resp:
                 if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                 data = io.BytesIO(await resp.read())
                 await msg.delete()
                 await ctx.send(file=discord.File(data, 'radialblur.png'))

    @commands.command(aliases=['ussr'])
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def communism(self, ctx, member: discord.Member=None):
        """Communism flag is awesome!"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dankmemer.services/api/communism?avatar1={member.avatar_url_as(format='jpg', size=512)}", headers={'Authorization': API}) as resp:
                 if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                 data = io.BytesIO(await resp.read())
                 await msg.delete()
                 await ctx.send(file=discord.File(data, 'communism.gif'))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def rip(self, ctx, member: discord.Member=None):
        """Rest in peace ;("""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dankmemer.services/api/rip?avatar1={member.avatar_url_as(format='jpg', size=512)}", headers={'Authorization': API}) as resp:
                 if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                 data = io.BytesIO(await resp.read())
                 await msg.delete()
                 await ctx.send(file=discord.File(data, 'rip.png'))        

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blur(self, ctx, member: discord.Member=None):
        """I can't see your result ;-;"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/beta/blur?avatar={member.avatar_url_as(format='jpg', size=512)}") as resp:
                if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                data = io.BytesIO(await resp.read())
                await msg.delete()
                await ctx.send(file=discord.File(data, 'blur.png'))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invert(self, ctx, member: discord.Member=None):
        """Convert to invert colors (Worked with member, but images or URL is not supported)"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/beta/invert?avatar={member.avatar_url_as(format='jpg', size=512)}") as resp:
                if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                data = io.BytesIO(await resp.read())
                await msg.delete()
                await ctx.send(file=discord.File(data, 'invert.png'))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gay(self, ctx, member: discord.Member=None):
        """Ur gay lol"""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dankmemer.services/api/gay?avatar1={member.avatar_url_as(format='jpg', size=512)}", headers={'Authorization': API}) as resp:
                if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                data = io.BytesIO(await resp.read())
                await msg.delete()
                await ctx.send(file=discord.File(data, 'gay.png'))


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wasted(self, ctx, member: discord.Member=None):
        """Oh no..."""
        if member is None:
            member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/beta/wasted?avatar={member.avatar_url_as(format='jpg', size=512)}") as resp:
                if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                data = io.BytesIO(await resp.read())
                await msg.delete()
                await ctx.send(file=discord.File(data, 'wasted.png'))

    @commands.command(aliases=['minecraft'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def achievement(self, ctx, *text):
        """Minecraft achievement is awesome."""
        if text is None:
            return await ctx.send(f"**Use `{ctx.prefix}achievement <text>`**")
        bruh = '+'.join(a for a in text)
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://minecraftskinstealer.com/achievement/1/Achievement%20get!/{bruh}") as resp:
                if resp.status != 200:
                    return await ctx.send(content='**Could not download file... Please try again!**')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'achievement.png'))
def setup(bot):
    bot.add_cog(Images(bot))
