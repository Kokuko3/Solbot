import os
import re
import pandas as pd

import discord
from discord.ext import commands
from discord import app_commands
from discord import Client


async def setup(bot: commands.Bot):
    await bot.add_cog(commands(bot))

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sync')
    async def sync(self, ctx):
        await self.bot.tree.sync()
        self.bot.tree.copy_global_to(guild=ctx.guild)

    @app_commands.command(description="Check to see who needs to touch grass")
    async def annoy(self, interaction:discord.Interaction, user_mention:str):
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send("It's done")
        guild = interaction.guild

        try:
            int(user_mention[3:-1])
        except ValueError:
            await interaction.channel.send("The `user_mention` parameter can only take user mentions (i.e. of format `@user`).", ephemeral = True)
            return
        
        user = discord.utils.get(guild.roles, id=int(user_mention[3:-1]))
        if user == None:
            await interaction.channel.send(f"The '{user_mention}' role could not be found. The `role_mention` parameter can only take user mentions (i.e. of format `@user`).", ephemeral = True)
            return
        
        channel = await user.create_dm()
        await channel.send("Yo, get on loser.")
