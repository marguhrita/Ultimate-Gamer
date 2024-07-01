from discord.ext import commands
import discord
from discord import app_commands
import json


class RoleManager(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener("on_ready")
    async def cog_ready(self):
        print(f"Role Manager Cog Loaded")

    @commands.command(name = "avatar")
    async def getAvatar(self, ctx):
        avatarUrl = ctx.author.avatar
        await ctx.send(avatarUrl)

    @commands.command(name="save_roles")
    @commands.has_permissions(administrator=True)
    async def save_roles(self, ctx):
        print("Saving roles...")
        roles = {}
        for role in ctx.guild.roles:
            roles[role.name] = role.id

        with open(f"roles_{ctx.guild.name}.json", "w") as f:
                json.dump(roles, f)

    @app_commands.command(name="get_role", description="Choose the role you would like")
    async def get_role(self, interaction : discord.Interaction, chosen_role : str):
        guild = interaction.guild
        with open(f"roles_{guild.name}.json") as f:
            roles = json.load(f)
        role : discord.Role  = guild.get_role(roles[chosen_role])
        await interaction.user.add_roles(role)  
        await interaction.response.send_message(f"Role {chosen_role} added >///<", ephemeral = True)

    @app_commands.command(name = "test", description="testing slash commands")
    async def test(self, interaction : discord.Interaction, name : str):
        await interaction.response.send_message(f"hi {name}")



async def setup(client):
    await client.add_cog(RoleManager(client))
    "guilds=[discord.Object(id=1201558800000368690)]"