import discord
from discord.ext import commands
import os
import datetime
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')
load_dotenv()
client = discord.Client()
currentTime = datetime.datetime.now()
formatDate = currentTime.strftime("%x")

def save_reminders(reminder):
  if "reminders" in db.keys():
    reminders = db["reminders"]
    reminders.append(reminders)
    db["reminders"] = reminders
  else:
    db["reminders"] = [reminders]

def get_local_date():
    currentDate = datetime.datetime.now()
    localDate = currentDate.strftime("%x")
    uk_date = datetime.datetime.strptime(localDate, '%m/%d/%y').strftime('%d/%m/%y')
    return uk_date

def get_local_time():
    currentTime = datetime.datetime.now()
    localTime = currentTime.strftime("%X")
    return localTime

@client.event
async def on_ready():
  print("You have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("!CurrentDate"):
    await message.channel.send(get_local_date())

  if message.content.startswith("!CurrentTime"):
    await message.channel.send(get_local_time())

  if message.content.startswith("!FullTime"):
    await message.channel.send(f"{get_local_date()} {get_local_time()}")

@bot.command()
async def command_test(ctx, arg):
    await ctx.send(arg)

TOKEN = os.getenv('TOKEN')



