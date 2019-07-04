import discord
from discord.ext import commands
import random
import json
import asyncio
import io
import aiohttp
from discord import Webhook, RequestsWebhookAdapter
import requests

colors = ([discord.Color.red(), discord.Color.blue(),
            discord.Color.green(), discord.Color.purple(),
            discord.Color.orange(), discord.Color.blurple(),
            discord.Color.magenta()])

def weeb(text):
        text = text.lower().replace('o', 'ow')
        text = text.lower().replace('v', 'w')
        text = text.lower().replace('i', 'wi')
        text = text.lower().replace('y', 'i')
        text = text.lower().replace('OwO', 'UwU')
        text = text.lower().replace('a', 'o')
        text = text.lower().replace('r', 'rw')
        text = text.lower().replace('e', 'we')
        text = text.lower().replace('t', 'ht')
        text = text.lower().replace('c', 'ch')
        text = text.lower().replace('u', 'uw')
        owo = random.choice(['OwO!', ':3', 'uwu', 'oWo, whats this?', 'uw- OwO!', ''])
        return f"{text} {owo}"

class Fun(commands.Cog):
    """Party Time."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=bot.loop)

    """
    @commands.command(aliases=['swearfy'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def swearify(self, ctx, *, msg=None):
        ""Convert to gramatica de calitatea""
        if msg is None:
            msg = "sa-mi bag pula-n ma-ta"
        a = msg.replace('-', '')
        a = a.replace('mata', 'mota')
        a = a.replace('fmm', 'fututi mortii matii')
        a = a.replace('mama ta', 'mata')
        a = a.replace('pula', 'puta')
        a = a.replace('pizda', 'pizdo')
        a = a.replace('muie', 'muje')
        a = a.replace('cur', 'kur')
        a = a.replace('coaie', 'coe')
        b = random.choice(["Ma copile, ", "Tus ceapa matii, ", ""])
        await ctx.send(f"{b}{a}")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def budgie(self, ctx, *, msg=None):
        ""Convert to budgie's message""
        if msg is None:
            msg = "=====))))))))))))))))"
        a = msg.replace('-', '')
        a = a.lower().replace('c', 'k')
        a = a.replace('=)))', '=======)))))))))')
        a = a.lower().replace('lol', 'loam')
        a = a.lower().replace('pula', 'puta')
        a = a.lower().replace('pizda', 'pizdo')
        a = a.lower().replace('muie', 'muje')
        a = a.lower().replace('cur', 'kur')
        a = a.lower().replace('coaie', 'cuaie')
        a = a.lower().replace('ma-ta', 'mo-ta')
        a = a.lower().replace('mata', 'mota')
        b = random.choice(["am nitro sarakilor, ", "salkf, ", "=)) "])
        await ctx.send(f"{b}{a}")
    """

    @commands.command(aliases=['8ball'], usage='<question>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ask(self, ctx, question=None):
        """Ask me!"""
        if question is None:
            return await ctx.send("**Ask me!**")
        else:
            asked = random.choice([
                "Yes.", "No.", "Don't ask me!",
                "Are you sure?", "Haha no!", "I'm interesing",
                "Why do you ask me?", "Nope.", "Haha",
                "Well yes, but no."])
            await ctx.send(f"**{asked}**")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def catfact(self, ctx):
        """Nice information about cats!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/cat") as r:
                res = await r.json()
                await ctx.send(f"**:cat: Did you know?**\n{res['fact']}")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dogfact(self, ctx):
        """Nice information about dogs!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/dog") as r:
                res = await r.json()
                await ctx.send(f"**:dog: Did you know?**\n{res['fact']}")


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def say(self, ctx, *, message):
        """Say whatever you want!"""
        await ctx.send(message)
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sayd(self, ctx, *, message):
        """Same as say, but delete the command."""
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(usage='<text>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clone(self, ctx, *, idea=None):
        """Same as say, but clone into webhook"""
        member = ctx.author
        if idea is None:
            return await ctx.send(f"**Use `{ctx.prefix}clone <your message>`!**")
        try:
            web = await ctx.channel.create_webhook(name="test")
            webhook = Webhook.partial(web.id, web.token, adapter=RequestsWebhookAdapter())
            webhook.send(idea, username=member.name, avatar_url=member.avatar_url)
            webhook.delete()
        except:
            return await ctx.send(idea)
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def meme(self, ctx):
        """Send as memes"""
        memes = random.choice([
            'dankmemes', 'memes', 'MemeEconomy', 'wholesomememes',
            'meirl', 'me_irl', 'i_irl', 'bikinibottomtwitter',
            'starterpacks', 'dankchristianmemes',
            'youdontsurf', 'im14andthisisdeep', 'ComedyCemetery',
            'deepfried', 'okbuddyretard'])
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.imgur.com/3/gallery/r/{memes}/time/week", headers={'Authorization': 'Client-ID API'}) as r:
                res = await r.json()
                ran = random.randint(1, 40)
                try:
                    for i in res['data'][:ran]:
                        if i['nsfw'] is True:
                            continue
                        bruh = i
                except:
                    return await ctx.send("**Ops... I got an error! Try again!**")
                e = discord.Embed(title=i['title'], color=random.choice(colors))
                e.description = f"Not working? Check in **[this link]({i['link']})**"
                e.set_image(url=i['link'])
                e.set_footer(text=f"\U0001f44d {i['score']}")
                await ctx.send(embed=e)
                
                
    @commands.command(aliases=['uwu'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def owo(self, ctx):
        """Whats this?"""
        owo = "owo"
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.imgur.com/3/gallery/r/{owo}/time/week", headers={'Authorization': 'Client-ID API'}) as r:
                res = await r.json()
                ran = random.randint(1, 50)
                try:
                    for i in res['data'][:ran]:
                        if i['nsfw'] is True:
                            pass
                        bruh = i
                except:
                    return await ctx.send("**Ops... I got an error! Try again!**")
                await ctx.send(i['link'])


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kill(self, ctx, member: discord.Member=None):
        """Kills someone"""
        if member is None:
            return await ctx.send("You are a dead!")
        await ctx.send(f"**{member.name}** died")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def weebify(self, ctx, *, text):
        """Thwis wis o rwwesuwlht uwu"""
        await ctx.send(weeb(text))

def setup(bot):
    bot.add_cog(Fun(bot))
