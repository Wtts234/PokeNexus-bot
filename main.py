import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

# -----------------------------
# INTENTS
# -----------------------------
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True

# -----------------------------
# BOT
# -----------------------------
class PokeNexusBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self):
        # Carrega todos os cogs automaticamente antes de ligar
        await self.load_extension("packs")

# -----------------------------
# INICIALIZAÇÃO
# -----------------------------
bot = PokeNexusBot()

@bot.event
async def on_ready():
    print(f"🔥 𝐏oké𝐍exus está online como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 PokéNexus está ativo!")

# -----------------------------
# RODAR BOT
# -----------------------------
TOKEN = os.getenv("DISCORD_TOKEN")  # Sempre use variável de ambiente para segurança
bot.run(TOKEN)
