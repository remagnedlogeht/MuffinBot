import discord
from discord.ext import commands
import brawlstats
from random import choice as c
import os
import aiohttp


colors = c([discord.Color.red(), discord.Color.blue(),
            discord.Color.green(), discord.Color.purple(),
            discord.Color.orange(), discord.Color.blurple(),
            discord.Color.magenta()])

class BrawlStars(commands.Cog):
    """I know, the bot has Brawl Stars stats. It works perfect."""

    def __init__(self, bot):
        self.bot = bot
        self.client = brawlstats.Client(os.getenv("bsTOKEN"), is_async=True)

    @commands.command(usage='<tag>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bsprofile(self, ctx, tag: str=None):
        """Get a brawl stars profile"""
        if tag is None:
            return await ctx.send(f"**Use `{ctx.prefix}bsprofile <tag>`!**")
        try:
            tag = tag.replace('#', '')
            player = await self.client.get_profile(tag)
        except brawlstats.RequestError as e:
            return await ctx.send('```\n{}: {}\n```'.format(e.code, e.error))
        brawlers = player.brawlers
        top_brawler = brawlers[0]
        em = discord.Embed(title=f'{player.name} (#{player.tag})', color=colors)
        try:
            em.set_author(name=player.club.name, icon_url=player.club.badge_url)
        except:
            em.set_author(name="No clan")
        em.add_field(name="Level", value=player.exp_level, inline=True)
        em.add_field(name="Total XP", value=player.total_exp, inline=True)
        em.add_field(name="Trophies", value=player.trophies, inline=True)
        em.add_field(name="Best trophies", value=player.highest_trophies, inline=True)
        em.add_field(name="Total Victories", value=player.victories, inline=True)
        em.add_field(name="Solo victories", value=player.solo_showdown_victories, inline=True)
        em.add_field(name="Duo victories", value=player.duo_showdown_victories, inline=True)
        em.add_field(name="Best time as big brawler", value=player.best_time_as_big_brawler, inline=True)
        em.add_field(name="Best robo rumble time", value=player.best_robo_rumble_time, inline=True)
        em.add_field(name="Brawlers collected", value=player.brawlers_unlocked, inline=True)
        em.add_field(name="Best brawler:", value=f"{top_brawler.name} (trophies: {top_brawler.trophies})")
        em.set_thumbnail(url=player.avatar_url)
        await ctx.send(embed=em)
          
    @commands.command(usage='<tag>')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def brawlers(self, ctx, tag: str=None):
        """List brawlers"""
        if tag is None:
            return await ctx.send(f"**Use `{ctx.prefix}brawlers <tag>`!**")
        try:
            player = await self.client.get_profile(tag)
        except brawlstats.RequestError as e:
            return await ctx.send('```\n{}: {}\n```'.format(e.code, e.error))
        brawlers = player.brawlers
        top_brawler = brawlers[0]
        em = discord.Embed(title=f'{player.name}\'s brawers', color=colors)
        em.description = '\n'.join(f"{e.name} - Trophies {e.trophies} - Power {e.power} - Has skin? {e.has_skin}" for e in brawlers)
        em.set_footer(text="True means yes and False means no.", icon_url=player.avatar_url)
        await ctx.send(embed=em)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def leaderboard(self, ctx, types=None):
        """Top 10 best players in the world!"""
        if types is None:
            types = 'players'
        best = await self.client.get_leaderboard(lb_type=types, count=10)
        em = discord.Embed(title=f"Top 10 best {types}", color=colors)
        em.description = "\n".join(f"`{g.position}.` {g.name} ({g.tag}) - Trophies {g.trophies}" for g in best)
        await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(BrawlStars(bot))
