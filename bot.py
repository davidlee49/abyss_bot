import asyncio
from discord import app_commands
from discord.ext import commands
import discord
import bot_reqs
import responses
import hangman
import reddit


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    TOKEN = bot_reqs.TOKEN

    @bot.command()
    async def play_hangman(ctx):
        game = hangman.HangmanBoard()
        await ctx.send("Game!", view=game)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now running! ")
        await bot.tree.sync()

    @bot.event
    async def on_button_click(self, interaction):
        await interaction.respond("hi")

    @bot.tree.command()
    async def memes(interaction: discord.Interaction):
        await interaction.response.send_message(reddit.get_img())

    @bot.tree.command()
    async def play_hangman(interaction: discord.Interaction):
        game = hangman.HangmanBoard()
        await interaction.response.send_message("You have 5 guesses! Good luck!", view=game)

    bot.run(TOKEN)
