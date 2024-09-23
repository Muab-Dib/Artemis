import discord # import discord.py
from discord.ext import commands # import commands from discord.ext
import random as rand
import re
#import asyncpraw

# dice roller class for cogs
class DiceRoller(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # bot is instantiated
		self.res = 0 # global variable for bot
	# Listener event
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{__name__} is online!")
	# This rolls the dice
	def roll_die(self, quant, dieType):
		roll_result = 0
		dieType = int(dieType)
		quant = int(quant)
		for i in range(int(quant)):
			roll_result += rand.randrange(1, dieType+1)
		return roll_result
	
	# format: .roll [quant][prefix][dieType][arith]*{modifiers}* (optional)
	# {modifiers} = roll (recursion), repeating infinitely or 0 times
	# Example: .roll 1d20+5. quant=1, prefix=d, dieType=20,airth=+,modifiers=5
	@commands.command()
	async def roll(self, ctx, arg):
		print(f"Received!")
		reg_die = re.compile("(\d*(d{1}\d+)+)")
		multiple_die_rolls = re.findall(reg_die, arg) # I plan on using this in the future to
		# find dice within dice (aka, if someone did 1d20 + 1d20, it'll see the second d20 and run this command again)
		# though idk if I can do recursion on a commands.command() like that so easily.
		print(multiple_die_rolls) # prints them in the console
		if not reg_die.match(arg): # if the command input doesn't match with the regex, we tell them its wrong.
			await ctx.send(f'Command format is wrong! Your format was {arg}')
			return
		# TODO: Rolling works now, but I can't have it do recursion yet, nor can it do arithmetic
		# I did get it to do arithmetic earlier, but I rolled without modifiers, the bot won't send the result.
		# So I'm gonna work on that later.
		print(f"Arg is: {arg}") # check the command format
		cmd_split = re.split(r"(\D+)",arg) # split it by number. NOTE: THIS IS PROBABLY TEMPORARY!
		print(f"Split command is: {cmd_split}")
		quant = cmd_split[0] # these are hard coded values for where we expect to find the quantity and dieType
		dieType = cmd_split[2]
		self.res = self.roll_die(quant, dieType) # we store the roll die's result in the bot's res variable
		print(self.res) # print for debugging
		# send the message via an embed
		output_cmd = discord.Embed(title="Roll", description="Your die result!", color=discord.Color.pink())
		output_cmd.add_field(name=f"{ctx.author.name}'s result is ",value=f"{self.res}",inline=False)
		await ctx.send(embed=output_cmd)

async def setup(bot):
	await bot.add_cog(DiceRoller(bot))