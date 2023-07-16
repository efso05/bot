import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
     print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def gen_emoji(ctx):
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    await ctx.send(random.choice(emoji))

@bot.command()
async def yazı_tura(ctx):
    donme = random.randint(0, 2)
    if donme == 0:
        await ctx.send("tura")
    else:
        await ctx.send("yazı")
    
@bot.command()
async def bay(ctx):
    await ctx.send(f'görüşmek üzere:(')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)       

bot.run("MTEyNzYzOTA3MzYxNjU2NDI5NA.GuKc2w.pJ1-R4IyBKiRMUEKmum2xyMMCuJePQ5VYg6sAU")
