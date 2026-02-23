import discord
from discord.ext import commands
import os

# -----------------------------
# CONFIGURAÇÕES DE PERMISSÕES
# -----------------------------
intents = discord.Intents.default()
intents.messages = True          # Permite o bot ler mensagens
intents.message_content = True   # Permite acessar o conteúdo das mensagens
intents.guilds = True            # Permite interações no servidor
intents.members = True           # Permite acessar membros (para inventário/decks/etc)

# -----------------------------
# INICIALIZAÇÃO DO BOT
# -----------------------------
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# -----------------------------
# IMPORTAÇÃO DOS COGS
# -----------------------------
# Supondo que você já criou os arquivos packs.py, inventory.py etc na mesma pasta
import packs
import inventory
import economy
import decks
import battle
import trades
import admin

# -----------------------------
# CARREGAR COGS
# -----------------------------
async def load_cogs():
    await bot.add_cog(packs.Packs(bot))

bot.loop.create_task(load_cogs())  # Agenda para rodar antes de ficar online

# -----------------------------
# EVENTO AO LIGAR
# -----------------------------
@bot.event
async def on_ready():
    print(f"🔥 𝐏oké𝐍exus está online como {bot.user}")

# -----------------------------
# COMANDO DE TESTE
# -----------------------------
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 PokéNexus está ativo!")

# -----------------------------
# EXECUTAR BOT
# -----------------------------
TOKEN = os.getenv("DISCORD_TOKEN")  # Sempre use variável de ambiente para segurança
bot.run(TOKEN)
