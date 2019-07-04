import discord
from discord.ext import commands
import random
import aiohttp

sadness = 'https://media0.giphy.com/media/OPU6wzx8JrHna/giphy.gif'

randomcolor = random.choice([discord.Color.red(), discord.Color.blue(), discord.Color.green(), discord.Color.purple(), discord.Color.magenta(), discord.Color.gold()])

class Action(commands.Cog):
    """I like this category"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member=None):
        """Hugs like a good boi :3"""
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}hug <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/animu/hug') as r:
                res = await r.json()
                e = discord.Embed(title=f"**{member.name}**, you got a hug by **{ctx.author.name}**!", color=randomcolor)
                e.set_image(url=res['link'])
                return await ctx.send(embed=e)

    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member=None):
        """\U0001f633"""
        kisses = [
            "https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865", "https://media.giphy.com/media/ZRSGWtBJG4Tza/giphy.gif", "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif", "https://media.tenor.com/images/8cf98d92c54ee938e1c6617ad8c0e167/tenor.gif", "https://media.giphy.com/media/kU586ictpGb0Q/giphy.gif", "https://media.giphy.com/media/JYpVJEcNrDAWc/giphy.gif",
"https://24.media.tumblr.com/5d51b3bbd64ccf1627dc87157a38e59f/tumblr_n5rfnvvj7H1t62gxao1_500.gif", "https://media.giphy.com/media/KH1CTZtw1iP3W/giphy.gif", "https://uploads.disquscdn.com/images/964bd0189d1674220997816c271470bf5f2c32860ee5bcf63d50031fbc82a0cd.gif", "https://media.giphy.com/media/Gj8bn4pgTocog/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media.tenor.com/images/12b26e30f1d526db62847bede9bbd414/tenor.gif",
"https://media.giphy.com/media/ONq87vZz4626k/giphy.gif", "https://media.giphy.com/media/BaEE3QOfm2rf2/giphy.gif", "https://media.tenor.com/images/de18124ebe36764446ee2dbf54a672bf/tenor.gif", "https://media.giphy.com/media/KmeIYo9IGBoGY/giphy.gif", "https://media.giphy.com/media/4gVv2ERASSYYo/giphy.gif", "https://media.giphy.com/media/vUrwEOLtBUnJe/giphy.gif", "https://i.pinimg.com/originals/f5/34/19/f53419e78c719c313b64378168fa94cc.gif",
"https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif", "https://thumbs.gfycat.com/NeatMinorAnglerfish-small.gif", "https://media.giphy.com/media/ll5leTSPh4ocE/giphy.gif", "https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657", "https://media.giphy.com/media/JFmIDQodMScJW/giphy.gif"
            ]
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}kiss <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        e = discord.Embed(title=f"**{member.name}**, you got a kiss by **{ctx.author.name}**!", color=randomcolor)
        e.set_image(url=random.choice(kisses))
        return await ctx.send(embed=e)

    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lick(self, ctx, member: discord.Member=None):
        """Lick? OwO"""
        licks = ["https://media1.giphy.com/media/12MEJ2ArZc23cY/source.gif", "https://media0.giphy.com/media/3t2KgMgBgMfwA/source.gif", "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727"]
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}lick <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        e = discord.Embed(title=f"**{member.name}**, you got a lick by **{ctx.author.name}**!", color=randomcolor)
        e.set_image(url=random.choice(licks))
        return await ctx.send(embed=e)

    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member=None):
        """Pats a member :3"""
        pats = ["https://media1.tenor.com/images/68d981347bf6ee8c7d6b78f8a7fe3ccb/tenor.gif?itemid=5155410", "https://i.imgur.com/2lacG7l.gif", "https://media1.tenor.com/images/70960e87fb9454df6a1d15c96c9ad955/tenor.gif?itemid=10092582", "https://thumbs.gfycat.com/AgileHeavyGecko-max-1mb.gif", "https://i.imgur.com/4ssddEQ.gif", "https://media.giphy.com/media/ARSp9T7wwxNcs/giphy.gif"]
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}lick <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        e = discord.Embed(title=f"**{member.name}**, you got a pat by **{ctx.author.name}**!", color=randomcolor)
        e.set_image(url=random.choice(pats))
        return await ctx.send(embed=e)
    
    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member=None):
        """Slaps a bad boi >:("""
        slaps = ["https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif", "https://media1.tenor.com/images/1cf84bf514d2abd2810588caf7d9fd08/tenor.gif?itemid=7679403", "https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943", "https://media.giphy.com/media/9U5J7JpaYBr68/giphy.gif"]
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}lick <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        e = discord.Embed(title=f"**{member.name}**, you got a pat by **{ctx.author.name}**!", color=randomcolor)
        e.set_image(url=random.choice(slaps))
        return await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Action(bot))
