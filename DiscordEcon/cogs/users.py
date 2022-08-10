from discord.ext import commands
import discord
from user import User
from job import Job
from item import Item

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command(name="inventory", help="See your inventory")
    async def inventory(self, ctx: commands.Context):
        user = User(ctx.author.id)
        inventory = user.inventory
        string = ""
        for item in inventory:
            string = string + f"{item.name}: {item.description} [{item.type}]"
            # TODO: make a good embed

    
def setup(client):
    client.add_cog(admin(client))
