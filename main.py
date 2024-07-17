import os
import discord
import asyncio
from random import randint
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

async def main():
    load_dotenv()
    token = os.getenv("discord_token")
    await bot.start(token)

@bot.event
async def on_ready():
    print('Holy Roller online')

@bot.hybrid_command()
async def sync(ctx):
    await ctx.send('commands synced')
    await bot.tree.sync()

class dice(commands.Converter):
    async def roll():
        result = randint(1,100)
        if result == 69:
            response =("you rolled a 69 ... Nice")
        else:
            response =("You rolled a", result)
        return response


@bot.hybrid_command()
async def roll(ctx):
    await ctx.send("you rolled a", )

asyncio.run(main())