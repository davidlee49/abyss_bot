import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)



async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


asyncio.run(main())



