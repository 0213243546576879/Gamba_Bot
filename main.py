import json
import discord
import discord.ext
from discord.ext import commands

import comhand

intents = discord.Intents.default()

intents.messages = True
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
	if message.author.bot:
		return

	print("Message Recieved!")
	if bot.user.mentioned_in(message):
		await comhand.command_handle(message)

with open("config.json", "r") as file:
    input = json.loads(file.read())
    print(input["TOKEN"])
    bot.run(input["TOKEN"])