<<<<<<< HEAD
import json
import datetime
from palace import *
  
def parse(inputCommand):
  parseInput = inputCommand.split(" ")
  parseInput_noSpace = [s for s in parseInput if s != '']
  if parseInput_noSpace.pop(0):
    room = Go(parseInput_noSpace)
    return room.exitroom

with open("rooms.json", 'r') as f:
  story = json.load(f)
  
def strike(text):
    return '\u0336'.join(text)

intro = story["story_intro"]
format_intro = intro.replace("magic", strike("magic"))

print(format_intro)
print(story["police_report"])

command = ""
while command != "quit":
  command = input("?: ")
  parse(command)
  
  if command == "look":
    print(story["abyss_look"])
    
  if command == "leave":
    print("Alright, goodbye then. Have it your way.")
    break
    
    
=======
import discord
from API_KEYS import *
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


bot.run(BOT_TOKEN)
>>>>>>> e0cd923c8102028a222c0b553a213ff191f27510
