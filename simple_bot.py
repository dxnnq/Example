import discord, os, json
from discord.ext import commands

with open("config.json") as t:
   data = json.load(t)
   TOKEN = data["TOKEN"]

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("!"), #Whatever you want your prefix to be
            intents = discord.Intents.all(),
            help_command = None #Disabling the base help command
)
    async def setup_hook(self):
        print(f"Logged in as {bot.user}")
        cogs_folder = f"{os.path.abspath(os.path.dirname(__file__))}/cogs"
        for filename in os.listdir(cogs_folder):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.tree.sync(guild=discord.Object(id=YOUR_GUILD_ID) #Remove the guild part if you want it to be global
        print("Cogs Loaded")
         
@bot.command()
async def hi(ctx: commands.Context, name: str = None):
   name = name or ctx.author.name
   await ctx.send(f"Hello! {name}")
   
@bot.tree.command(description="Say hello!", guild=discord.Object(id=YOUR_GUILD_ID) #Remove the guild part if its global
async def hello(interaction: discord.Interaction, name: str = None):
   name = name or interaction.user.name
   await interaction.response.send_message(f"Hello! {name}") #If you want the message to be hidden to just the command author pass in an ephemeral (f"Hello!", ephemeral=True)

                  
bot.run(TOKEN)

#In your config.json file
{
    "TOKEN": "YOUR_BOT_TOKEN"
}
