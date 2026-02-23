import discord
from discord.ext import commands
import os

# Importa os cogs
import packs
import inventory
import economy
import decks
import battle
import trades
import admin

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"𝐏oké𝐍exus está online como {bot.user}")

# Carregar cogs
bot.add_cog(packs.Packs(bot))
bot.add_cog(inventory.Inventory(bot))
bot.add_cog(economy.Economy(bot))
bot.add_cog(decks.Decks(bot))
bot.add_cog(battle.Battle(bot))
bot.add_cog(trades.Trades(bot))
bot.add_cog(admin.Admin(bot))

bot.run(TOKEN)
