import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('OTMyMDMxMzQ4NDE4NDM3MTQw.YeND1Q.KE5X0wb6GibaKVFSsBe3ugzsMn4')