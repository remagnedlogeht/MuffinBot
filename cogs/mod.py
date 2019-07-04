import discord
from discord.ext import commands
import datetime
import asyncio


class Moderation(commands.Cog):
    """Psst. Don't be retard or ban."""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban a member!"""
        if not member:
            return await ctx.send("**Use `>ban <user> [reason]`!**")
        if member.guild_permissions.administrator is True:
            return await ctx.send("I don't ban that user because **user has administrator permission**")
        if member == ctx.author:
            return await ctx.send("I don't ban you ;-;")
        if member == ctx.guild.owner:
            return await ctx.send("I can't ban the owner of this server!")
        else:
            try:
               if reason is None:
                   await member.ban(reason=f"by {ctx.author}")
                   await ctx.send(f"**{member} has been banned!**")
               else:
                   await member.ban(reason=f"by {ctx.author} | {reason}")
                   await ctx.send(f"**{member} has been banned!**\nReason: {reason}")
            except:
                return await ctx.send("I can't ban that user! Did you mean? Missing Permission...")

    @commands.command(aliases=['blacklist', 'hack-ban', 'hack_ban'], usage='<user ID>')
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hackban(self, ctx, member: int, *, reason=None):
        """Same as ban, but the member isn't in this server"""
        user = discord.Object(member)
        User = await self.bot.fetch_user(user)
        tag = User.discriminator
        name = User.name
        bruh = name + '#' + tag
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"**{bruh} has been banned!**")        

    @commands.command(usage='<user ID>')
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def unban(self, ctx, member: int=None):
        """Unban an user!"""
        bot = self.bot
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}unban <user ID>`!**")
        banned_users = await ctx.guild.bans()
        ID = await self.bot.fetch_user(member)
        for i in banned_users:
            bruh = i.user.id
            if member == bruh:
                await ctx.guild.unban(i.user)
                await ctx.send(f"**{i.user} has been unbanned!**")
                return
            else:
                return await ctx.send(f"**{ID} is not found in server ban list.**")
                
                
    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick a member!"""
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}kick <user> [reason]`!**")
        if member.guild_permissions.administrator is True:
            return await ctx.send("I don't kick that user because **user has administrator permission**")
        if member == ctx.author:
            return await ctx.send("I don't kick you ;-;")
        if member == ctx.guild.owner:
            return await ctx.send("I can't kick the owner of this server!")
        else:
            try:
               if reason is None:
                   await member.kick(reason=f"by {ctx.author}")
                   await ctx.send(f"**{member} has been kicked!**")
               else:
                   await member.kick(reason=f"by {ctx.author} | {reason}")
                   await ctx.send(f"**{member} has been kicked!**\nReason: {reason}")
            except:
                return await ctx.send("I can't kick that user! Did you mean? Missing Permission...")
            
    @commands.command(usage='<member>')
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def mute(self, ctx, member: discord.Member=None):
        """Mute an user!"""
        if member is None:
            return await ctx.send(f"**Please use `{ctx.prefix}mute <member>`**")
        if member == ctx.author:
            return await ctx.send("**I don't mute you ;-;**")
        if member == ctx.guild.owner:
            return await ctx.send("**I don't mute the owner ;-;**")
        if member.guild_permissions.administrator is True:
            return await ctx.send("**I can't mute that user because user has administrator access**")
        for i in member.roles:
            if i.name == 'Muted':
                return await ctx.send(f"**This user has already muted. Use `{ctx.prefix}unmute <user>` for unmute!**")
            else:
                try:
                    bruh = discord.util.get(ctx.guild.roles, name='Muted')
                    await member.add_roles(bruh)
                    await ctx.send(f"**`{ctx.author}` has been muted!**")
                except:
                    return await ctx.send("**Ops... `Muted` role is not found in this server or I don't have access to add roles!**")

    @commands.command(aliases=['locked'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lock(self, ctx, reason=None):
        """Lock a channel! This command is used for stop spamming"""
        for i in ctx.channel.overwrites:
            if i.name == "@everyone":
                if ctx.channel.overwrites_for(i).send_messages is False:
                    return await ctx.send("**Already locked!**")
        if reason is None:
            reason = "no reason"
        perm = discord.PermissionOverwrite()
        perm.send_messages = False
        perm.read_messages = True
        perm.add_reactions = False
        bruh = discord.utils.get(ctx.guild.roles, name="@everyone")
        await ctx.channel.set_permissions(target=bruh, overwrite=perm, reason=f"locked a channel for {reason}")
        await ctx.send(f"{ctx.channel.mention} has been locked for **{reason}**!")

    @commands.command(aliases=['unlocked'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unlock(self, ctx):
        """Unlock a channel!"""
        for i in ctx.channel.overwrites:
            if i.name == "@everyone":
                if ctx.channel.overwrites_for(i).send_messages is True:
                    return await ctx.send("**Already unlocked!**")
        perm = discord.PermissionOverwrite()
        perm.send_messages = True
        perm.read_messages = True
        perm.add_reactions = True
        bruh = discord.utils.get(ctx.guild.roles, name="@everyone")
        await ctx.channel.set_permissions(target=bruh, overwrite=perm)
        await ctx.send(f"{ctx.channel.mention} has been unlocked!")
        
    @commands.command(usage='<number/off>')
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def slowmode(self, ctx, slowmode=None):
        """Set a slowmode channel"""
        if slowmode is None:
            return await ctx.send(f"**Use `{ctx.prefix}slowmode <number/off>`!**")
        if slowmode == 'off':
            await ctx.channel.edit(slowmode_delay=None)
            await ctx.send(f"**{ctx.channel.mention} is no longer slowmode! :grinning:**")
            return
        try:
            num = int(slowmode)
        except:
            return await ctx.send("**Invalid agrument! Use `{ctx.prefix}slowmode <delay>`!**")
        await ctx.channel.edit(slowmode_delay=num)
        await ctx.send(f"**{ctx.channel.mention} is on slowmode! `{num} seconds` :zipper_mouth:**")
        
    @commands.command(usage='<member>')
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unmute(self, ctx, member: discord.Member=None):
        """Unmute an user!"""
        if member is None:
            return await ctx.send(f"**Please use `{ctx.prefix}unmute <member>`**")
        if member == ctx.author:
            return await ctx.send("**I don't unmute you ;-;**")
        if member == ctx.guild.owner:
            return await ctx.send("**I don't unmute the owner ;-;**")
        if member.guild_permissions.administrator is True:
            return await ctx.send("**I can't unmute that user because user has administrator access**")
        for i in member.roles:
            if i.name == 'Muted':
                try:
                    await member.remove_roles(i)
                    await ctx.send(f"**`{ctx.author}` has been unmuted!**")
                except:
                    return await ctx.send("**Ops... I can't remove `Muted` role from the user.**")
            else:
                return await ctx.send("**That user has already unmuted!**")
  
                    
    @commands.command(aliases=["prune", "clear", "clean"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, number: int, channel: discord.TextChannel=None):
        """Clear up messages!"""
        if channel is None:
            channel = ctx.channel
        try:
            if number > 200:
                return await ctx.send(f"**The number is too much! Try again!** ({number}/200)")
            else:
                await channel.purge(limit=number+1)
        except ValueError:
            return await ctx.send("**Invalid agruments. Use `>purge <number> [channel]`!**")
        except:
            return await ctx.send("I can't delete... Did you know? Missing permissions or...")


            
        
def setup(bot):
    bot.add_cog(Moderation(bot))
    
           
        
            
