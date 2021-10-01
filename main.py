import discord
from discord.ext import commands
import os
import datetime
from dotenv import load_dotenv
import sqlite3
import db

con = sqlite3.connect("reminders.db")
cur = con.cursor()
bot = commands.Bot(command_prefix='!')
load_dotenv()
currentTime = datetime.datetime.now()
formatDate = currentTime.strftime("%x")

def get_local_date():
    currentDate = datetime.datetime.now()
    localDate = currentDate.strftime("%x")
    uk_date = datetime.datetime.strptime(localDate, '%m/%d/%y').strftime('%d/%m/%y')
    return uk_date

def get_local_time():
    currentTime = datetime.datetime.now()
    localTime = currentTime.strftime("%X")
    return localTime

@bot.command(name="SetReminder")
async def set_reminder(ctx, date, time):
    await ctx.send(f"Set for {date} at {time}")

@bot.command(name="CurrentDate")
async def current_date(ctx):
    await ctx.send(get_local_date())

@bot.command(name="CurrentTime")
async def set_reminder(ctx):
    await ctx.send(get_local_time())

@bot.command(name="FullTime")
async def set_reminder(ctx):
    await ctx.send(f"{get_local_date()} {get_local_time()}")

@bot.event
async def on_ready():
  print("You have logged in as {0.user}".format(bot))

@bot.command()
async def command_test(ctx, arg):
    await ctx.send(arg)

TOKEN = os.getenv('TOKEN')

bot.run(TOKEN)

