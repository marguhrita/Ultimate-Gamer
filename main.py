from discord.ext import commands
import discord, os


class MyClient(commands.Bot):

  async def on_ready(self):
    print(f'We have logged in as {client.user}')
    await client.get_channel(1201558800000368694).send("I AM AWOKEN")


    #load cogs found in "cogs" directory
    for extension in os.listdir("./cogs/"):
      
      if extension.endswith(".py"):
        print(f"loading cog {extension}")
        self.load_extension(f"cogs.{extension[:-3]}")

  async def on_message(self, message):

    #allows us to use commands as well as the on_message event
    await client.process_commands(message)


with open("token.txt", "r") as f:
  token = f.read().rstrip()

  intents = discord.Intents.all()
  client = MyClient(command_prefix='#', intents = intents, activity=discord.Game("Gaming Ultimately (cutely)"))
  print("running")
  client.run(token)