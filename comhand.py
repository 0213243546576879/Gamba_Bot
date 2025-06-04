import os
import discord
import json
import types

class CrackComm:
	def __init__(self, name, desc):
		pass
	
	def Comm_Func():
		pass
async def command_handle(message):
	commands = (OptIn, Test2)
	isValid = False

	content = message.content
	parsed_command = content[content.find(">") + 2:]
	split_command = parsed_command.split(" ")
	for x in commands:
		if x.__name__ == split_command[0]:
			split_command.pop(0)
			exit_code = x(message, com_args = split_command)
			isValid = True
			break
	if(not isValid):
		await message.channel.send("Invalid Command :(     If this doesn't seem right, contact the developer because line 35 is probably screwed up or something")
	else:
		await exit_handler(message, exit_code)
        
async def exit_handler(message, exit_code):
	print(exit_code)
	match exit_code:
		case 0:
			pass
		case 1:
			await message.channel.send("Error: Apple      If you have already opted in, you could have gotten this, if not, please contact the dumbass that made this bot because they broke something")
		case _:
			await message.channel.send("Error: Caffeine      ... I don't really know what went wrong :/")
            
def OptIn(message, **kwargs):
	user = message.author.display_name
	path = "user_data/" + user + ".json"
	if(os.path.isfile(path)):
		return 1
	else:
		file = open(path, "x")
		data = {"user": user, "cryptoe": 100}
		json.dump(data, file)
		file.close()
		return 0

def Test2(args):
	print(f"Test2 args: {args}")

def crackComm(func):
	def wrapper():
		x = CrackComm(func.__name__, "")
		x.CommFunc = types.MethodType(func, x)