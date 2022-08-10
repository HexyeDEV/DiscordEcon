from discord.ext import commands
import discord
from user import User
from job import Job
from item import Item
import sqlite3

class users(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command(name="inventory", help="See your inventory")
    async def inventory(self, ctx: commands.Context):
        user = User(ctx.author.id)
        inventory = user.inventory
        embed = discord.Embed(title="INVENTORY", description="Your Inventory", color=0x73d216)
        for item in inventory:
            embed.add_field(name=item.name, value=f"```{item.description}```", inline=True)
        embed.set_footer(text="<a href='https://google.com.com'>Support Us</a> - <a href='https://google.com.com'>Leave a Feedback</a> - <a href='https://github.com/HexyeDEV/DiscordEcon'>Contribute to the Project</a>")
        await ctx.send(embed)
    
    @commands.command(name="shop", help="Open the Shop")
    async def shop(self, ctx: commands.Context, item_name: str = None):
        db = sqlite3.connect("DiscordEcon.db")
        c = db.cursor()
        if not item_name:
            user = User(ctx.author.id)
            balance = user.balance
            embed = discord.Embed(title="Shop", description=f"You have {balance} coins")
            items = c.execute("SELECT * FROM").fetchall()
            for item in items:
                item_obj = Item("0", item[1], "0", 0)
                embed.add_field(name=item_obj.name, value=f"```{item_obj.description}```\nPrice: {item_obj.cost}\nSold: {item_obj.bought}")
            embed.set_footer(text="To buy an item time de!shop <item name>")
            await ctx.send(embed=embed)
        else:
            item = Item("0", item_name, "0", 0)
            if item.type == "0" and item.description == "0":
                await ctx.send(f"No item found with the name ```{item_name}```")
            else:
                user = User(ctx.author.id)
                balance = user.balance
                if user.balance >= item.cost:
                    user.change_balance(-item.cost)
                    item.buy()
                    user.add_item(item.name)
                    await ctx.send(f"You have succesfully bought ```{item.name}``` with ```{item.cost}``` coins")
                else:
                    await ctx.send(f"You do not have enough coins to buy {item.name}\nYour coins: {balance} coins needed: {item.cost}")


    
def setup(client):
    client.add_cog(users(client))
