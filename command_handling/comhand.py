import discord


async def command_handle(message):
	commands = (OptIn, Test2)

	content = message.content
	parsed_command = content[content.find(">") + 2:]
	split_command = parsed_command.split(" ")
	for x in commands:
		if x.__name__ == split_command[0]:
			split_command.pop(0)
			exit_code = x(message = message, com_args = split_command)
	if(not exit_code):
		await message.channel.send("Invalid Command :(     If this doesn't seem right, contact the developer because line 35 is probably screwed up or something")
	else:
		exit_handler(message, exit_code)
        
async def exit_handler(message, exit_code):
	match exit_code:
		case 0:
			pass
		case 1:
			await message.channel.send("Error: Apple      If you have already opted in, you could have gotten this, if not, please contact the dumbass that made this bot because they broke something")
		case _:
			await message.channel.send("Error: Caffeine      ... I don't really know what went wrong :/")