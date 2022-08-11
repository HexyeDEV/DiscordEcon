from discord.ext import commands
from discord.ext.commands import is_owner
import discord
from user import User
from job import Job
from item import Item

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="change_balance", help="Change the balance of an user")
    @is_owner()
    async def change_balance(self, ctx: commands.Context, user: discord.User, changement: int):
        user_obj = User(user.id)
        new = user_obj.change_balance(changement)
        await ctx.send(f"Balance of {user.mention} changed to {new}")
    
    @commands.command(name="set_balance", help="Set the balance of an user")
    @is_owner()
    async def set_balance(self, ctx: commands.Context, user: discord.User, balance: int):
        user_obj = User(user.id)
        new = user_obj.set_balance(balance)
        await ctx.send(f"Balance of {user.mention} changed to {new}")
    
    @commands.command(name="get_balance", help="Get the balance of an user")
    @is_owner()
    async def get_balance(self, ctx: commands.Context, user: discord.User):
        user_obj = User(user.id)
        await ctx.send(f"Balance of {user.mention} is {user_obj.balance}")
    
    @commands.command(name="create_job", help="Create a new job")
    @is_owner()
    async def create_job(self, ctx: commands.Context, name: str, reward: int, timeout: int):
        Job(name, reward, timeout)
        
        await ctx.send(f"A new job was created with the name: {name}")
    
    @commands.command(name="toggle_job", description="Open or Close a job")
    @is_owner()
    async def toggle_job(self, ctx: commands.Context, name: str):
        job = Job(name, 0, 0)
        if job.opened == True:
            job.opened = False
            await ctx.send("Job succefully Closed.")
        elif job.opened == False:
            job.opened = True
            await ctx.send("Job succesfully Opened.")
    
    @commands.command(name="create_item", help="Create a new item")
    @is_owner()
    async def create_item(self, ctx: commands.Context, type: str, name: str, description: str, cost: int):
        Item(type, name, description, cost)
        await ctx.send(f"A new item was created with the name: {name}")
    
    @commands.command(name="set_cost", description="Set the cost of an item")
    @is_owner()
    async def set_cost(self, ctx: commands.Context, name: str, cost: int):
        item = Item("0", name, "0", 0)
        item.set_cost(cost)
        await ctx.send(f"Set cost of item {name} to {cost}")
    
    @commands.command(name="toggle_item", help="Make an item buyable or unbuyable")
    @is_owner()
    async def toggle_item(self, ctx: commands.Context, name: str):
        item = Item("0", name, "0", 0)
        if item.buyable == False:
            item.buyable_status(True)
            await ctx.send(f"The item ```{name}``` is now buyable")
        elif item.buyable == True:
            item.buyable_status(False)
            await ctx.send(f"The item ```{name}``` is now not buyable")



    
def setup(client):
    client.add_cog(admin(client))
