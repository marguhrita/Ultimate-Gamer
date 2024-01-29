from discord.ext import commands
import discord


class Helper(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):    
        if message.author == self.client.user:
            return
        
        if message.channel == self.client.get_channel(1201558800000368694):
            if message.content == "I have read the rules":
                role = await self.get_role(message.guild, 1201619683204399134)
                await self.assign_role(message.author, role)
                


    @commands.command()
    async def assign_role(self, member: discord.Member, role: discord.Role):
        await member.add_roles(role)


    @commands.command()
    async def get_role(self, guild: discord.Guild, roleId: int) -> discord.Role:

        for role in guild.roles:
            if role.id == roleId:
                return role
            
        print("no role found :(")
        return None
  




def setup(client):
    client.add_cog(Helper(client))