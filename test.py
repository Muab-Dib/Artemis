import discord # import discord.py
from discord.ext import commands # import commands from discord.ext

# the class called Test takes Cog commands. Cogs are like organized collections of commands, listeners, and some states in a class.
# think of it like tracks on a vinyl.
class Test(commands.Cog): # the test class here is a cog, just to test things out.
    def __init__(self, bot): # here's a init method
        self.bot = bot # bot is instantiated

    # this is a listener, this listens in on events that are taking place, and allows it to respond when its detected
    @commands.Cog.listener()
    # here, its listening for the cog event to go online. If it is, then we execute the event which prints in the console, confirming
    # if our event is online
    async def on_ready(self):
        print(f"{__name__} is online!")

    # these are cog commands, which are essentially commands which are executed when called (so calling .ping will do a ping)
    @commands.command()
    # this is a ping, not a discord @mention, but a latency ping.
    async def ping(self, ctx):
        # We create an embed that'll hold all the info
        pingCmd = discord.Embed(title="Ping", description="Latency in ms", color=discord.Color.pink())
        # we add a field which refers to the bot's username (Artemis), and the latency.
        pingCmd.add_field(name=f"{self.bot.user.name}'s latency (ms)",value=f"{round(self.bot.latency * 1000)}ms.",inline=False)
        # set the footer, which gets the name and icon of the person who issued the command
        pingCmd.set_footer(text=f"Requested by {ctx.author.name}.", icon_url=ctx.author.avatar)
        # we wait until we finish executing other stuff.
        await ctx.send(embed=pingCmd)

# setup the bot
async def setup(bot):
    # execute the bot and pass it in the Test class, which instantiates the bot, and allows it to be referred to by the self parameter.
    await bot.add_cog(Test(bot))