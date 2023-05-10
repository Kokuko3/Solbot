import random

import discord
from discord.ext import commands
from discord import app_commands

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
    async def touchgrass(self, interaction: discord.Interaction):
        userid = 454078409228681216
        await interaction.response.send_message(f"@{userid}, touch grass.")
