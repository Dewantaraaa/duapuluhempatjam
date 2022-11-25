from discord.ext import commands
from myserver import server_on

TOKEN = "MTA0MzYyMzUyMDI5MjMyNzU3NA.GbcvFJ.zxG6OOiF723qKarpXRnZmbOhePxtTEy0IXfAuY" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Online'.format(ctx.author.name.title()))

server_on()
bot.run(TOKEN)
