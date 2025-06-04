import os
import json
import discord
import discord.ext
from discord.ext import commands

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
		await command_handle(message)





def OptIn(**kwargs):
	user = message.author.display_name
	path = "/user_data/" + user
	if(os.path.isfile(path)):
		return 1
	else:
		with open(path, "w") as file:
			data = {"user": user, "cryptoe": 100}
			json.dump(data, file)
		

def Test2(args):
	print(f"Test2 args: {args}")


with open("config.json", "r") as file:
    token = json.load(file)[TOKEN]
    bot.run(json.load(file)["TOKEN"])