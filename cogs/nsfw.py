import discord
from discord.ext import commands
import random
import asyncio
import aiohttp
import praw

APIi = os.getenv("iTOKEN")

randomcolor = random.choice([discord.Color.red(), discord.Color.blue(), discord.Color.green(), discord.Color.purple(), discord.Color.magenta(), discord.Color.gold()])

class NSFW(commands.Cog):
    """Oh yes, you can do it :D
**YOU CAN USE IT IN NSFW CHANNEL**"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['boob'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def boobs(self, ctx):
        """\U0001f60d"""
        if ctx.channel.is_nsfw() is False:
            return await ctx.send("**This channel has no NSFW...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.imgur.com/3/gallery/r/boob/time/week", headers={'Authorization': f'Client-ID {APIi}'}) as r:
                res = await r.json()
                ran = random.randint(1, 40)
                try:
                    for i in res['data'][:ran]:
                        bruh = i
                    e = discord.Embed(color=randomcolor)
                    e.set_image(url=bruh['link'])
                    await ctx.send(embed=e)
                except:
                    return await ctx.send("**Ops... I got an error! Try again!**")

    @commands.command(aliases=['dick'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def penis(self, ctx):
        """Got a ...? OwO"""
        if ctx.channel.is_nsfw() is False:
            return await ctx.send("**This channel has no NSFW...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.imgur.com/3/gallery/r/penis/time/week", headers={'Authorization': f'Client-ID {APIi}'}) as r:
                res = await r.json()
                ran = random.randint(1, 40)
                try:
                    for i in res['data'][:ran]:
                        bruh = i
                    e = discord.Embed(color=randomcolor)
                    e.set_image(url=bruh['link'])
                    await ctx.send(embed=e)
                except:
                    return await ctx.send("**Ops... I got an error! Try again!**")


    @commands.command(aliases=['animeporn'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hentai(self, ctx):
        """Hentai is awesome :D"""
        if ctx.channel.is_nsfw() is False:
            return await ctx.send("**This channel has no NSFW...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.imgur.com/3/gallery/r/hentai/time/week", headers={'Authorization': f'Client-ID {APIi}'}) as r:
                res = await r.json()
                ran = random.randint(1, 40)
                try:
                    for i in res['data'][:ran]:
                        bruh = i
                    e = discord.Embed(color=randomcolor)
                    e.set_image(url=bruh['link'])
                    await ctx.send(embed=e)
                except:
                    return await ctx.send("**Ops... I got an error! Try again!**")


    @commands.command(aliases=['gayp'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gayporn(self, ctx):
        """You're now gay."""
        if ctx.channel.is_nsfw() is False:
            return await ctx.send("**This channel has no NSFW...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.imgur.com/3/gallery/r/gayporn/time/week", headers={'Authorization': f'Client-ID {APIi}'}) as r:
                res = await r.json()
                ran = random.randint(1, 40)
                try:
                    for i in res['data'][:ran]:
                        bruh = i
                    e = discord.Embed(color=randomcolor)
                    e.set_image(url=bruh['link'])
                    await ctx.send(embed=e)
                except:
                    return await ctx.send("**Ops... I got an error! Try again!**")

    @commands.command(aliases=['butts', 'ass'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def butt(self, ctx):
        """\U0001f351"""
        if ctx.channel.is_nsfw() is False:
            return await ctx.send("**This channel has no NSFW...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.imgur.com/3/gallery/r/ass/time/week", headers={'Authorization': f'Client-ID {APIi}'}) as r:
                res = await r.json()
                ran = random.randint(1, 40)
                try:
                    for i in res['data'][:ran]:
                        bruh = i
                    e = discord.Embed(color=randomcolor)
                    e.set_image(url=bruh['link'])
                    await ctx.send(embed=e)
                except:
                    return await ctx.send("**Ops... I got an error! Try again!**")

    @commands.command(aliases=['shemale'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def traps(self, ctx):
        """Traps aren't gay OwO"""
        if ctx.channel.is_nsfw() is False:
            return await ctx.send("**This channel has no NSFW...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.imgur.com/3/gallery/r/traps/time/week", headers={'Authorization': f'Client-ID {APIi}'}) as r:
                res = await r.json()
                ran = random.randint(1, 40)
                try:
                    for i in res['data'][:ran]:
                        bruh = i
                    e = discord.Embed(color=randomcolor)
                    e.set_image(url=bruh['link'])
                    await ctx.send(embed=e)
                except:
                    return await ctx.send("**Ops... I got an error! Try again!**")


    @commands.command(aliases=['r34'], usage='<tag>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rule34(self, ctx, tag=None):
        """Send as non-real images."""
        if ctx.channel.is_nsfw() is False:
            return await ctx.send("**This channel has no NSFW...**")
        if not tag:
            return await ctx.send(f"**Use `{ctx.prefix}rule34 <tag>`!**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://r34-json-api.herokuapp.com/posts?tags={tag}") as r:
                res = await r.json()
                ran = random.randint(1, 40)
                if not res:
                    return await ctx.send(f"**Ops... I can't find the tag `{tag}`!**")
                for i in res[:ran]:
                    bruh = i
                e = discord.Embed(title=f"Score: {bruh['score']}", color=discord.Color.orange())
                e.set_image(url=bruh['file_url'])
                return await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(NSFW(bot))
