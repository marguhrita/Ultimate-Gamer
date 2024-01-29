from discord.ext import commands
import discord


class Helper(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):    
        if message.author == self.client.user:
            return
        
        if message.channel == self.client.get_channel(849989417942253568):
            if message.content == "I have read the rules":
                await self.assign_role(message.author, self.client.get_role(1201619683204399134))
                await message.channel.send("SAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    @commands.command()
    async def assign_role(member: discord.Member, role: discord.Role):
        await member.add_roles(role)


def setup(client):
    client.add_cog(Helper(client))