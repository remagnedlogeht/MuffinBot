import discord
from discord.ext import commands
import random
import datetime
import time
import aiohttp
import psutil
import io
from hurry.filesize import size
from utils.HelpPaginator import HelpPaginator, CannotPaginate

start_time = time.time()
randomcolor = random.choice([discord.Color.red(), discord.Color.blue(), discord.Color.green(), discord.Color.purple(), discord.Color.magenta(), discord.Color.gold()])

mysystem = [ 
    (1024 ** 2, ' MB'), 
    (1024 ** 1, ' KB'),
    (1024 ** 0, ' B'),
    ]

class Utility(commands.Cog):
    """I mean information"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases= ["whois", "uinfo", "playerinfo", "user-info", "memberinfo", "member-info", "info-user"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userinfo(self, ctx, member: discord.Member=None):
        """Who are you? :thinking:"""
        if member is None:
            member = (ctx.author)
        if member.bot is True:
            a = "Yes, he's a bot! :robot:"
        if member.bot is False:
            a = "No, he's not a bot! :grinning:"
        if member.status.name == 'online':
            b = "<:online:536240817602560010> Online"
        if member.status.name == 'idle':
            b = "<:idle:536240817522868224> Idle"
        if member.status.name == 'dnd':
            b = "<:dnd:536240817531125760> DND"
        if member.status.name == 'offline':
            b = "<:offline:536240817552228385> Offline"
        if member.activity is None:
            c = 'This user is not playing yet'
        if member.activity is not None:
            c = member.activity.name
        if not member.is_on_mobile():
            d = "No"
        if member.is_on_mobile():
            d = "Yes"
        e = member.created_at
        f = ctx.message.created_at
        h = f-e
        i = member.joined_at
        j = f-i
        joinages = j.days
        ages = h.days
        try:
            embed = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
            embed.set_author(name="Who is?")
            embed.add_field(name="Name", value=member.name)
            embed.add_field(name="Is this a bot?", value=a)
            embed.add_field(name="Status", value=b)
            embed.add_field(name="Playing", value=c)
            embed.add_field(name="User is on mobile?", value=d)
            embed.add_field(name="Tag", value=member.discriminator)
            embed.add_field(name="Top Role", value=member.top_role)
            embed.add_field(name="Nick", value=member.nick)
            embed.add_field(name="Joined", value=f"{i.strftime('%A, %B %d %Y @ %H:%M:%S %p')} ({joinages} days)")
            embed.add_field(name="Created at", value=f"{e.strftime('%A, %B %d %Y @ %H:%M:%S %p')} ({ages} days)")
            embed.add_field(name="Roles", value=', '.join(g.name for g in member.roles))
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f'ID: {member.id}')
            embed.timestamp = datetime.datetime.utcnow()
        except discord.HTTPException:
            embed = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
            embed.set_author(name="Who is?")
            embed.add_field(name="Name", value=member.name)
            embed.add_field(name="Is this a bot?", value=a)
            embed.add_field(name="Status", value=b)
            embed.add_field(name="Playing", value=c)
            embed.add_field(name="User is on mobile?", value=d)
            embed.add_field(name="Tag", value=member.discriminator)
            embed.add_field(name="Top Role", value=member.top_role)
            embed.add_field(name="Nick", value=member.nick)
            embed.add_field(name="Joined", value=f"{i.strftime('%A, %B %d %Y @ %H:%M:%S %p')} ({joinages} days)")
            embed.add_field(name="Created at", value=f"{e.strftime('%A, %B %d %Y @ %H:%M:%S %p')} ({ages} days)")
            embed.add_field(name="Roles", value="This user's roles is too many.")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f'ID: {member.id}')
            embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


        
    @commands.command(aliases=["guildinfo", "guild-info", "server-info"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def serverinfo(self, ctx):
            """Information about this server!"""
            regions = {
                "brazil": ":flag_br:  Brazil",
                "eu-central": ":flag_eu: EU Central",
                "eu-west": ":flag_eu: EU West",
                "hongkong": ":flag_hk: Hong Kong",
                "india": ":flag_in: India",
                "japan": ":flag_jp: Japan",
                "russia": ":flag_ru: Russia",
                "southafrica": ":flag_za: South Africa",
                "us-central": ":flag_us: US Central",
                "us-south": ":flag_us: US South",
                "us-west": "flag_us: US West"
                }
            verify = {
                "none": "None (ᴗ ͜ʖ ᴗ)",
                "low": "Low ( ͝° ͜ʖ͡°)",
                "medium": "Medium ( ͡° _ʖ ͡°)",
                "high": "HIGH (╯°□°）╯︵ ┻━┻",
                "extreme": "**EXTREME** (ﾉ °益°)ﾉ 彡 ┻━┻"
                }
            c = 0
            a = 0
            g = 0
            online = 0
            idle = 0
            dnd = 0
            n = ctx.guild.member_count
            for i in ctx.guild.members:
             if i.bot is True:
              c+=1
            for i in ctx.guild.members:
             if i.bot is False:
              a+=1
            for i in ctx.guild.members:
              if i.status.name == 'online':
                  online += 1
              if i.status.name == 'idle':
                  idle += 1
              if i.status.name == 'dnd':
                  dnd += 1
              g = online + idle + dnd
            m = ctx.guild.created_at
            sugi = ctx.message.created_at
            o = sugi-m
            em = discord.Embed(color=randomcolor)
            em.add_field(name='Name', value=f'{ctx.author.guild.name}', inline=True)
            em.add_field(name='Owner', value=f'{ctx.author.guild.owner.name} [{ctx.author.guild.owner.id}]', inline=True)
            em.add_field(name='Verification level', value=verify[str(ctx.guild.verification_level)], inline=True)
            em.add_field(name="Server Booster", value=f"Level `{ctx.guild.premium_tier}` | `{ctx.guild.premium_subscription_count}` boosters")
            em.add_field(name="Limits", value=f"Emoji: `{ctx.guild.emoji_limit}`\nAudio bitrate: `{ctx.guild.bitrate_limit/1000}kbps`\nFile size: `{size(ctx.guild.filesize_limit, system=mysystem)}`")
            stat = f"""
**Roles:** {len(ctx.guild.roles):,d}
**Members:** {n:,d} (People: {a:,d} | Bots: {c:,d})
**Total Channels:** {len(ctx.guild.channels):,d} (Category: {len(ctx.guild.categories):,d} | Text: {len(ctx.guild.text_channels):,d} | Voice: {len(ctx.guild.voice_channels):,d})
**Online:** {g:,d}"""
            em.add_field(name="Stats", value=stat)
            em.add_field(name='Created at', value=f'{m.strftime("%A, %B %d %Y %H:%M:%S")} ({o.days} days ago)', inline=True)
            try:
                em.add_field(name='Region', value=regions[str(ctx.guild.region)], inline=True)
            except:
                em.add_field(name='Region', value=ctx.guild.region, inline=True)
            em.set_thumbnail(url=ctx.guild.icon_url)
            if ctx.guild.banner == None and ctx.guild.splash != None:
                em.set_image(url=ctx.guild.splash_url)
            elif ctx.guild.banner != None and ctx.guild.splash == None:
                em.set_image(url=ctx.guild.banner_url)
            elif ctx.guild.banner == None and ctx.guild.splash == None:
                pass
            else:
                em.add_field(name="Splash URL", value=f"[Click here]({ctx.guild.splash_url})")
                em.set_image(url=ctx.guild.banner_url)
            em.set_footer(text=f'ID: {ctx.guild.id}')
            em.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=em)
            
    @commands.command(aliases=["bige", "big"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def emoji(self, ctx, emoji: discord.Emoji):
        """View emoji"""
        async with aiohttp.ClientSession() as session:
            async with session.get(str(emoji.url)) as resp:
                data = io.BytesIO(await resp.read())
                if emoji.animated is True:
                    s = "gif"
                else:
                    s = "png"
                await ctx.send(file=discord.File(data, f"emoji.{s}"))


    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ping(self, ctx):
        """Pong!"""
        a = await ctx.send("**Pong!**")
        b = ctx.message.created_at
        c = a.created_at - b
        await a.edit(content=f'**Pong!** API response: `{ctx.bot.latency * 1000:,.0f}ms`, Response time: `{c}`')

    @commands.command(aliases=['bot-info', 'info'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def botinfo(self, ctx):
        """About this bot!"""
        bot = self.bot
        bruh = await bot.fetch_user(390540063609454593)
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        e = discord.Embed(title="Bot Info", color=randomcolor)
        e.add_field(name="Created At", value=ctx.me.created_at.strftime("%A, %B %d %Y %H:%M:%S"), inline=True)
        e.add_field(name="Owner Bot", value=bruh)
        e.add_field(name="Shards", value=f"{ctx.guild.shard_id} [total: {bot.shard_count}]")
        e.add_field(name="Uptime", value=text)
        e.add_field(name="Guilds", value=len(bot.guilds))
        e.add_field(name="Users", value=len(bot.users))
        e.add_field(name="CPU usage", value=f"{psutil.cpu_percent()}%")
        e.add_field(name="RAM usage", value=f"{size(psutil.virtual_memory().used, system=mysystem)} ({psutil.virtual_memory().percent}%)")
        e.add_field(name="Library", value=f"discord.py v{discord.__version__}")
        e.set_thumbnail(url=ctx.me.avatar_url)
        e.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def invite(self, ctx):
        """Invite this bot to your server!"""
        e = "https://discordapp.com/oauth2/authorize?client_id=569845238089121793&permissions=21469588398&scope=bot"
        em = discord.Embed(title="Invite to your server!", description="WARNING: This bot is in BETA", color=randomcolor)
        em.add_field(name="Click", value=f"[here]({e})")
        await ctx.send(embed=em)

    @commands.command(aliases=['av'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member=None):
        """Get an user's avatar"""
        if member is None:
            member = ctx.author
        em = discord.Embed(description=f'{member.mention}\'s [avatar]({member.avatar_url})', color=randomcolor)
        em.set_image(url=member.avatar_url)
        await ctx.send(embed=em)

    @commands.command(usage='<args | args2 | args3 | ...>')
    async def choose(self, ctx, *, args=None):
        """Result with chose"""
        if args is None:
            return await ctx.send(f"**Use `{ctx.prefix}choose <args | args2 | args3 | ...>`**")
        result = args.split(" | ")
        await ctx.send(random.choice(result))
		
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def help(self, ctx, *, command: str = None):
        """Shows help about a command or the bot"""
        try:
            if command is None:
                p = await HelpPaginator.from_bot(ctx)
            else:
                entity = self.bot.get_cog(command) or self.bot.get_command(command)

                if entity is None:
                    clean = command.replace('@', '@\u200b')
                    return await ctx.send(f'Command or category "{clean}" not found.')
                elif isinstance(entity, commands.Command):
                    p = await HelpPaginator.from_command(ctx, entity)
                else:
                    p = await HelpPaginator.from_cog(ctx, entity)

            await p.paginate()
        except Exception as e:
            await ctx.send(e)

    @commands.command(aliases=['emoji_info', 'emoji info', 'emojinfo'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def emojiinfo(self, ctx, emoji: discord.Emoji):
        a = emoji.created_at
        b = ctx.message.created_at
        c = b-a
        await ctx.send(f'`Name:` {emoji.name}\n`ID:` {emoji.id}\n`Guild with this emoji:` {emoji.guild}\n`Preview:` {emoji} (`{emoji}`)\n`URL:` {emoji.url}\n`Created at:` {a.strftime("%A, %B %d %Y @ %H:%M:%S %p")} ({c.days} days ago)')


def setup(bot):
        bot.add_cog(Utility(bot))
