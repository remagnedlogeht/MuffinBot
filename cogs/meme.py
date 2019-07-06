import discord
from discord.ext import commands
import aiohttp
import io
import typing
import os

API = {
    'Authorization': os.getenv("dmTOKEN")
    }
class Meme(commands.Cog, name="Meme Generator"):
    """You can create your own meme :D"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage='[member] <text>', aliases=['customeme', 'meme-custom', 'custom-meme', 'meme_custom', 'custom_meme'])
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def custommeme(self, ctx, member: typing.Optional[discord.Member]=None, *, text: str=None):
        """Custom meme from your avatar or member's avatar
For get bottom, please use `>custommeme [member] <top | bottom>`
Example: `>customeme @catnowblue My cat is | nice`"""
        if text is None:
            return await ctx.send(f"**Use `{ctx.prefix}customeme [member] <text>`**")
        if member is None:
            member = ctx.message.author
        try:
            bruh = text.split(' | ')
            bruh1 = bruh[0]
            bruh2 = bruh[1]
            if not bruh2:
                bruh2 = ""
        except:
            bruh1 = text
            bruh2 = ""
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/meme?avatar1={member.avatar_url_as(format='png')}&top_text={bruh1}&bottom_text={bruh2}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'meme.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def abandon(self, ctx, *, text=None):
        """Makes the baby an abandon"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}abandon <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/abandon?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'abandon.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def armor(self, ctx, *, text=None):
        """Armor is weak"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}armor <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/armor?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'armor.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def boo(self, ctx, *, text=None):
        """boo is scary!"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}boo <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/boo?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'boo.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def brain(self, ctx, *, text=None):
        """200 IQ be like"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}brain <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/brain?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'brain.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def byemom(self, ctx, *, text=None):
        """Bye your mom tho"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}byemom <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/byemom?text={text}&avatar1={ctx.author.avatar_url_as(format='jpg', size=512)}&username1={ctx.author.name}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'byemom.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def changemymind(self, ctx, *, text=None):
        """Maybe yes, but no"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}changemymind <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/changemymind?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'changemymind.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def cry(self, ctx, *, text=None):
        """I cry"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}cry <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/cry?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'cry.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def excuseme(self, ctx, *, text=None):
        """Excuse me, WTF?"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}excuseme <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/excuseme?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'excuseme.png'))

    @commands.command(aliases=['fact'], usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def facts(self, ctx, *, text=None):
        """and that's a FACT"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}facts <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/excuseme?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'facts.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def floor(self, ctx, *, text=None):
        """The floor is LAVA"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}floor <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/floor?text={text}&avatar1={ctx.author.avatar_url_as(format='jpg', size=512)}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'floor.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def humansgood(self, ctx, *, text=None):
        """Ariel knows the humans is good, but..."""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}humansgood <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/humansgood?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'humansgood.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def master(self, ctx, *, text=None):
        """Master is legendary"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}master <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/master?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'master.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def ohno(self, ctx, *, text=None):
        """I know, the dog is a retard"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}ohno <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/ohno?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ohno.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def presentation(self, ctx, *, text=None):
        """New Simpsons meme"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}presentation <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/presentation?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'presentation.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def shit(self, ctx, *, text=None):
        """Oh Shit"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}shit <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/shit?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'shit.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def vr(self, ctx, *, text=None):
        """Makes the guy cry from vr"""
        if not text:
            return await ctx.send(f"**Use `{ctx.prefix}vr <text>`**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://dankmemer.services/api/vr?text={text}", headers=API) as resp:
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'vr.png'))

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def youtube(self, ctx, *, text=None):
        """Set as your YouTube comment!"""
        if text is None:
            return await ctx.send(f"**Use `{ctx.prefix}youtube <text>`!**")
        member = ctx.author
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading... Please wait!**")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dankmemer.services/api/youtube?avatar1={member.avatar_url_as(format='jpg', size=512)}&username1={member.name}&text={text}", headers=API) as resp:
                 if resp.status != 200:
                    return await msg.edit(content='**Could not download file... Please try again!**')
                 data = io.BytesIO(await resp.read())
                 await msg.delete()
                 await ctx.send(file=discord.File(data, 'youtube.png')) 
def setup(bot):
    bot.add_cog(Meme(bot))
