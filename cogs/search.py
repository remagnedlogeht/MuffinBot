import discord
from discord.ext import commands
import random
import aiohttp
import praw

reddit = praw.Reddit(client_id='ID',
                     client_secret='SECRET',
                     user_agent='USER_AGENT')

api_key = "API"

class Search(commands.Cog):
    """Are you lazy to search it? Don't worry!
We have some search commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['imgur'], usage='<search>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def image(self, ctx, *, search=None):
        """Search on Imgur!"""
        default = ['meow', 'dog', 'cat', 'puppy']
        if search is None:
            search = random.choice(default)
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.imgur.com/3/gallery/search/time/all/0?q={search}', headers={'Authorization': 'Client-ID API'}) as r:
                res = await r.json()
                try:
                    if res['success'] is False:
                        return await msg.edit("**Ops... I can't find an image! :cry:**")
                    ints = random.randint(1,  10)
                    for i in res['data'][:ints]:
                        bruh = i
                    await msg.edit(content=f"**Found an image!\n**{bruh['link']}")
                except:
                    return await msg.edit(content=f"**Ops... I can't find an image!**\n`Status: {res['status']} | {res['data']['error']}`")
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def urban(self, ctx, *search):
        """Search on Urban Dictionary!"""
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"http://api.urbandictionary.com/v0/define?term={search}") as r:
                res = await r.json()
                try:
                    for i in res['list'][:1]:
                        bruh = i
                    e = discord.Embed(title=bruh['word'], url=bruh['permalink'], color=discord.Color.blue())
                    e.description = bruh['definition']
                    e.add_field(name="Example", value=bruh['example'])
                    e.set_footer(text=f"\U0001f44d {bruh['thumbs_up']} | \U0001f44e {bruh['thumbs_down']}")
                    await msg.edit(content="Found a word!", embed=e)
                except:
                    return await msg.edit(content="**Ops... I can't find a word!**")

    @commands.command(usage='<search>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gif(self, ctx, *, search=None):
        """Search on Giphy!"""
        if search is None:
            search="cat"
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading...**")
        search = search.replace(" ", "+")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"http://api.giphy.com/v1/gifs/search?q={search}&api_key={api_key}&limit=20") as r:
                res = await r.json()   
                try:
                    af = random.randint(1, 10)
                    for i in res['data'][:af]:
                        bruh = i
                    await msg.edit(content=f"Found a gif!\n{bruh['url']}")
                except:
                    return await msg.edit(content="**Ops... I can't find a gif!**")

    @commands.command(usage='<pokemon\'s name>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pokemon(self, ctx, pokemon=None):
        """Search on Pokedex!"""
        if pokemon is None:
            return await ctx.send(f"**Please use `{ctx.prefix}pokemon <pokemon's name>`!**")
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}") as r:
                try:
                    res = await r.json()
                    abb = ', '.join(g['ability']['name'] for g in res['abilities'])
                    types = ', '.join(g['type']['name'] for g in res['types'])
                    stats = ', '.join(f"{g['stat']['name'].capitalize()}[{g['base_stat']}]" for g in res['stats'])
                    moves = ', '.join(g['move']['name'].capitalize() for g in res['moves'][1:10])
                    e = discord.Embed(title=res['name'].capitalize(), color=discord.Color.red())
                    e.set_author(name="Pokedex", icon_url="https://upload.wikimedia.org/wikipedia/commons/5/51/Pokebola-pokeball-png-0.png")
                    e.add_field(name="Order", value=res['order'])
                    e.add_field(name="Abilities", value=abb)
                    e.add_field(name="Species", value=res['species']['name'].capitalize())
                    e.add_field(name="Height", value=res['height'])
                    e.add_field(name="Weight", value=res['weight'])
                    e.add_field(name="Type", value=types)
                    e.add_field(name="Stats", value=stats)
                    e.add_field(name="Moves", value=moves)
                    if res['sprites']['front_default'] is None:
                        oof = "https://pngimage.net/wp-content/uploads/2018/06/unknown-png.png"
                    else:
                        oof = res['sprites']['front_default']
                    e.set_thumbnail(url=oof)
                    await msg.edit(content="Found a pokemon!", embed=e)
                except:
                    return await msg.edit(content="**Ops... I can't find a pokemon! Try again!**")
                
    @commands.command(aliases=['reddit'], usage="<name>")
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def subreddit(self, ctx, subreddi=None):
        """Search on Reddit!"""
        if subreddi is None:
            return await ctx.send(f"**Use `>subreddit <name>`!**")
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading...**")
        try:
            memes_submissions = reddit.subreddit(subreddi).hot()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
                if submission.over_18 and ctx.channel.is_nsfw() is False:
                    return await msg.edit(content=f"**I think... Your request is a NSFW. So you can use it in NSFW channel.**")
                if submission.is_video:
                    continue
            e = discord.Embed(title=submission.title, description=submission.selftext, color=discord.Color.red())
            try:
                e.set_image(url=submission.url)
            except:
                pass
            try:
                e.description = f"**Not working? Check in the [website]({submission.url})**\n{submission.selftext}"
            except:
                e.description = f"**Not working? Check in the [website]({submission.url})**"
            e.set_footer(text=f"r/{subreddi} | Author: u/{submission.author}", icon_url="https://cdn0.iconfinder.com/data/icons/most-usable-logos/120/Reddit-512.png")
            await msg.edit(content=None, embed=e)
        except:
            return await msg.edit(content=f"**This subreddit is not found or not access to `r/{subreddi}`.**")

    @commands.command(aliases=['giftenor', 'tenorgif'], usage='<search>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tenor(self, ctx, search=None):
        """Search on Tenor!"""
        if not search:
            return await ctx.send(f"**Use `{ctx.prefix}tenor <search>!`**")
        msg = await ctx.send("<a:Loading:465439021514883072> **Loading...**")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.tenor.com/v1/search?q={search}&key=KEY&limit=10&anon_id=ID') as r:
                res = await r.json()
                try:
                    url = res['weburl']
                    for i in res['results'][:random.randint(1, 10)]:
                        for s in i['media']:
                            imageURL = s['gif']['url']
                    e = discord.Embed(color=discord.Color.green())
                    e.set_image(url=imageURL)
                    await msg.edit(content=None, embed=e)
                except:
                    return await msg.edit(content=f"**Ops.. I can't find an GIF! Try again!**")
        

def setup(bot):
    bot.add_cog(Search(bot))
