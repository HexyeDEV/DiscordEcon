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
    
    @commands.command(name="shop", help="Open the Shop or buy an Item")
    async def shop(self, ctx: commands.Context, item_name: str = None):
        db = sqlite3.connect("DiscordEcon.db")
        c = db.cursor()
        if item_name == None:
            user = User(ctx.author.id)
            balance = user.balance
            embed = discord.Embed(title="Shop", description=f"You have {balance} coins")
            items = c.execute("SELECT * FROM").fetchall()
            for item in items:
                item_obj = Item("0", item[1], "0", 0)
                embed.add_field(name=item_obj.name, value=f"```{item_obj.description}```\nPrice: {item_obj.cost}\nSold: {item_obj.bought}")
            embed.set_footer(text="To buy an item type de!shop <item name>")
            await ctx.send(embed=embed)
        else:
            item = Item("0", item_name, "0", 0)
            if item.type == "0" and item.description == "0":
                await ctx.send(f"No item found with the name ```{item_name}```")
            else:
                if item.buyable == True:
                    user = User(ctx.author.id)
                    balance = user.balance
                    if user.balance >= item.cost:
                        user.change_balance(-item.cost)
                        item.buy()
                        user.add_item(item.name)
                        await ctx.send(f"You have succesfully bought ```{item.name}``` with ```{item.cost}``` coins")
                    else:
                        await ctx.send(f"You do not have enough coins to buy {item.name}\nYour coins: {balance} coins needed: {item.cost}")
                else:
                    await ctx.send("This item is currently not buyable.")
    
    @commands.command(name="job", help="See the list of Jobs or select a Job")
    async def job(self, ctx: commands.Context, job_name: str = None):
        db = sqlite3.connect("DiscordEcon.db")
        c = db.cursor()
        if job_name == None:
            jobs = c.execute("SELECT * FROM jobs").fetchall()
            embed = discord.Embed(title="Jobs", description="This is the list of jobs")
            for job in jobs:
                job_obj = Job(job[0], 0, 0)
                embed.add_field(name=job_obj.name, value=f"Timeout between work: ```{job_obj.timeout}```")
            embed.set_footer("To apply for a job type de!job <job name>")
        else:
            job = Job(job[0], 0, 0)
            if job.reward == 0 and job.timeout == 0:
                await ctx.send(f"There are no jobs with the name {job_name}")
            else:
                user = User(ctx.author.id)
                user.set_job(job.name)
                job.users_count += 1
                await ctx.send(f"You have succesfully applied for {job.name} you can work every {job.timeout} seconds and you will be rewarded with {job.reward}")

    
def setup(client):
    client.add_cog(users(client))
