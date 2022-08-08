import discord
from discord.ext import commands
import os, sqlite3
from user import User
from job import Job
from item import Item

client = commands.Bot(prefix="de!", intents=discord.Intents.all)

@client.event
async def on_ready():
    for cog in os.listdir("./cogs"):
        if not cog.endswith(".py"):
            continue
        client.load_extension(f"cogs.{cog.replace('.py', '')}")
        print(f"Loaded cog cogs.{cog.replace('.py', '')}")

    print(f"Logged in as {client.user} (ID: {client.user.id})")