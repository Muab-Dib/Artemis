import discord # import discord.py
from discord.ext import commands # import commands from discord.ext
import random as rand
import re
#import asyncpraw

class DiceRoller(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{__name__} is online!")

	async def roll_die(self, quant, dieType):
		res = 0
		for i in quant:
			res += rand.randint(1, dieType)
		print(f'{self.res}')
		return int(self.res)
	
	# format: .roll [quant][prefix][dieType][arith]*{modifiers}* (optional)
	# {modifiers} = roll (recursion), repeating infinitely or 0 times
	# Example: .roll 1d20+5. quant=1, prefix=d, dieType=20,airth=+,modifiers=5
	@commands.command()
	async def roll(self, ctx, quant: int, prefix, dieType: int): #, *arith=None, *modifiers=0):
		print(f"Received!")

		str_com = str(quant) + prefix + str(dieType)
		reg_die = re.compile("(\d*(d{1}\d+)+)")
		if not reg_die.match(str_com):
			await ctx.send(f'Command format is wrong! Your format was {str_com}')
		"""
		if prefix.lower() != "d":
			await ctx.send(f'Command is invalid as you entered {prefix}')
		if type(quant) is not int and type(dieType) is not int:
			await ctx.send(f'Command has invalid types')
		"""
		"""
		if arith is None:
			arith = {}
			modifiers = {}
		if modifiers is None:
			modifiers = {}
		"""
		# TODO: Figure out how to get the arguments implemented properly.
		res = self.roll_die(quant, dieType)
		print(res)
		output_cmd = discord.Embed(title="Roll", description="Your die result!", color=discord.Color.pink())
		output_cmd.add_field(name=f"{ctx.author.name}'s result is ",value=f"{res}",inline=False)
		await ctx.send(embed=output_cmd)

async def setup(bot):
	await bot.add_cog(DiceRoller(bot))