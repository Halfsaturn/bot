import discord
from bot_logic import gen_pass
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f'Entrando como {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send("hi")

@bot.command()
async def bye(ctx):
    await ctx.send("😒")

@bot.command()
async def pasword(ctx, longitud: int):
    await ctx.send(gen_pass(longitud))

@bot.command()
async def comoestas(ctx):
    await ctx.send("Bien y tu")

@bot.command()
async def tambien(ctx):
    await ctx.send("😁👍")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)





bot.run("TU TOKEN")
