from discord.ext import commands
import discord, os
from discord import app_commands


intents = discord.Intents.all()
client = commands.Bot(command_prefix='#', intents = intents, activity=discord.Game("Gaming Ultimately (cutely)"))
my_guild = discord.Object(id=1201558800000368690)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  await client.get_channel(1201558800000368694).send("meow")
  await load_cogs()

async def load_cogs():
  #load cogs found in "cogs" directory
  for extension in os.listdir("./cogs/"):
    if extension.endswith(".py"):
      print(f"loading cog {extension}")
      await client.load_extension(f"cogs.{extension[:-3]}")

@client.command(name="sync", description="syncs slash commands with discord", hidden=True)
@commands.has_permissions(administrator=True)
async def sync(ctx):
  #Updates slash commands on a specific guild
  ctx.bot.tree.copy_global_to(guild=my_guild)
  synced = await ctx.bot.tree.sync(guild=my_guild)
  print(f"Synced {len(synced)} command(s).")



if __name__ == '__main__':
  with open("token.txt", "r") as f:
    token = f.read().rstrip()
    print(f"Starting bot...")
    client.run(token)