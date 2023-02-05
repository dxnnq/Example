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

#In your main file it should be
    
    async def setup_hook(self):
        print(f"Logged in as {bot.user}")
        cogs_folder = f"{os.path.abspath(os.path.dirname(__file__))}/cogs"
        for filename in os.listdir(cogs_folder):
           if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.tree.sync(guild=discord.Object(id=YOUR_GUILD_ID) #Remove the guild since this is a global command
        print("Cogs Loaded")
