import discord, aiosqlite, datetime, json
from discord.ext import commands
from discord import app_commands

class simple_bot_cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def hi(self, ctx: commands.Context, name: str = None):
        name = name or ctx.author.name
        await ctx.send(f"Hello! {name}") #If you want to reply to the message you can do ctx.reply
        
    @app_commands.command(description="Say hello!")
    async def hello(self, interaction: discord.Interaction, name: str = None):
        name = name or interaction.user.name
        await interaction.response.send_message(f"Hello! {name}")
        
           
async def setup(bot):
  await bot.add_cog(Config(bot))
