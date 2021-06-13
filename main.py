import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')   

#➥ on ready command
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("------------------------------")
##

#➥ Prefix Checker
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('>help'):
        await message.channel.send(f'To bring up detailed help menu type `>help` <:blush:845843091146539008>')
    await bot.process_commands(message)
##

#➥ Ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
##

#➥ Close Bot
@bot.command()
async def quit(ctx):
    if await bot.is_owner(ctx.author):
        await bot.change_presence(status = discord.Status.offline)
        await bot.logout()
    else:
        await ctx.send("You do not have the permissions to use this command!")
##


bot.run('ODUzNzQ0OTE5MzcwMDA2NTQ4.YMZ16g.EFdkz5nCEAR2oSCIRUWmb0KZ7_A')