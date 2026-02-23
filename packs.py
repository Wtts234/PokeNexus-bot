import discord
from discord.ext import commands
import sqlite3
import random

class Packs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def abrir(self, ctx):
        """Abre um pack e adiciona cartas ao inventário"""
        conn = sqlite3.connect("pokemon.db")
        c = conn.cursor()
        c.execute("SELECT * FROM pokemon")
        cartas = c.fetchall()
        conn.close()

        # Escolher 3 cartas aleatórias com raridade
        pack = random.sample(cartas, 3)
        mensagem = "**Seu pack contém:**\n"
        for carta in pack:
            mensagem += f"{carta[1]} ({carta[5]})\n"  # nome e raridade

        # Atualizar inventário do usuário
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT inventario FROM users WHERE user_id=?", (ctx.author.id,))
        resultado = c.fetchone()
        inventario = resultado[0] if resultado else ""
        ids_cartas = ",".join(str(carta[0]) for carta in pack)
        if inventario:
            inventario += "," + ids_cartas
        else:
            inventario = ids_cartas

        if resultado:
            c.execute("UPDATE users SET inventario=? WHERE user_id=?", (inventario, ctx.author.id))
        else:
            c.execute("INSERT INTO users (user_id, inventario) VALUES (?,?)", (ctx.author.id, inventario))
        conn.commit()
        conn.close()

        await ctx.send(mensagem)
