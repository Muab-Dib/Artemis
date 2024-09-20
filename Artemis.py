#!/usr/bin/env python
# Line above tells us where the python environment is located
"""
Author: Luna Stephenson
Credits: Credits to Paradoxical's YouTube series on how to program a Discord bot in Python for inspiration. 
This project is not meant for commercial use. I made this so I can brush up on Python, and learn how to make a Discord bot.
Overtime, I will make my own adjustments to it and implement my own unique features for it. But as of this initial posting, this is
for learning purposes. 
"""
import discord # import the discord.py library
from discord.ext import commands, tasks # Import commands from discord.ext
import os # import os
import asyncio # import asyncio
import io # importing io
import aiohttp # importing aiohttp
from itertools import cycle

bot = commands.Bot(command_prefix=".",intents=discord.Intents.all()) # all of our bot's commmands has the "." prefix.

botStatList = cycle(["Believe in yourself!", "You're worth it!", "Do, there is no try.", "Magic is real, you just gotta believe",
	"Made by Luna with <3", "Trans rights"])

@tasks.loop(seconds=5)
async def change_status():
	await bot.change_presence(activity=discord.Game(next(botStatList)))

@bot.event # bot event for when the bot is launched
async def on_ready(): # whenever our bot is online, we print this to the console to verify our bot is indeed active
	print("Artimus is now running!")
	change_status.start()

# For security purposes, our bot token is read from a private file
with open("token") as file:
	tkn = file.read()

async def load():
	for filename in os.listdir("./cogs"): # this opens up each file within the ./cogs directory
		if filename.endswith(".py"): # looks for python files
			await bot.load_extension(f"cogs.{filename[:-3]}") # waits while the bot loads the cogs files.
# set up the main method
async def main():
	async with bot: # sync up with the bot
		await load() # wait for it to load
		await bot.start(tkn) # run the bot's token

asyncio.run(main())
#bot.run(tkn)