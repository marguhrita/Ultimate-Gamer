from discord.ext import commands
import discord


class Helper(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        if "raven" in message.content:
            await message.channel.send("r-r-raven? I heard shes a cutie pie uwu")



def setup(client):
    client.add_cog(Helper(client))