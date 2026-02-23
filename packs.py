import discord
from discord.ext import commands
import sqlite3
import random

class Packs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def abrir(self, ctx):
        """Abre um pack de 3 cartas e mostra em embed"""
        # Conecta ao banco de cartas
        conn = sqlite3.connect("pokemon.db")
        c = conn.cursor()
        c.execute("SELECT * FROM pokemon")
        cartas = c.fetchall()
        conn.close()

        # Escolhe 3 cartas aleatórias
        pack = random.sample(cartas, 3)

        for carta in pack:
            embed = discord.Embed(
                title=f"{carta[1]} ({carta[5]})",  # nome + raridade
                description=f"Estágio: {carta[4]} | Tipo: {carta[2]} | HP: {carta[3]}",
                color=discord.Color.gold() if carta[5]=="Lendário" else
                      discord.Color.blue() if carta[5]=="Raro" else
                      discord.Color.light_grey()
            )
            embed.set_thumbnail(url=carta[8])
            
            # Adiciona ataques
            for i in range(9, 18, 3):
                ataque_nome = carta[i]
                ataque_dano = carta[i+1]
                ataque_custo = carta[i+2]
                if ataque_nome:
                    embed.add_field(
                        name=f"{ataque_nome} ({ataque_custo})",
                        value=f"Dano: {ataque_dano}",
                        inline=False
                    )
            await ctx.send(embed=embed)

            # Atualizar inventário do usuário
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute("SELECT inventario FROM users WHERE user_id=?", (ctx.author.id,))
            resultado = c.fetchone()
            inventario = resultado[0] if resultado else ""
            if inventario:
                inventario += f",{carta[0]}"
            else:
                inventario = str(carta[0])
            if resultado:
                c.execute("UPDATE users SET inventario=? WHERE user_id=?", (inventario, ctx.author.id))
            else:
                c.execute("INSERT INTO users (user_id, inventario) VALUES (?,?)", (ctx.author.id, inventario))
            conn.commit()
            conn.close()

# Para compatibilidade com discord.py 2.x
async def setup(bot):
    await bot.add_cog(Packs(bot))
