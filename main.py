import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def activo():
    print(f'Hemos iniciado sesion con el {bot.user}')
    

@bot.command()
async def favoritos(ctx, *, mensaje: str):
    await ctx.send("recomendaciones: cars vs trains, rails unlimited")

@bot.command()
async def resumen(ctx, *, mensaje: str):
    await ctx.send("""Roblox es como una caja de juguetes mágica en una computadora o celular. Pero en vez de solo jugar con juguetes, puedes crear tus propios juegos y mundos dentro de esa caja.

🧒👧 Muchos niños y niñas de todo el mundo entran a Roblox para:

Jugar juegos que hicieron otras personas.

Hacer sus propios juegos como si fueran legos, pero digitales.

Ponerse disfraces y explorar mundos imaginarios.
""")

@bot.command()
async def lego(ctx, *, mensaje: str):
    await ctx.send("https://www.roblox.com/es/users/251696789/profile")
token = 'MTM1MjczODg3Mjc0ODAxOTc4Mg.GcptRW.XOodmLQtcrp5dIamtSzqW5Sdoxr9fhHezcyLj8'

# 🔹 Iniciar el bot
# Esta línea conecta el bot a Discord y lo mantiene en ejecución.
bot.run(token)
