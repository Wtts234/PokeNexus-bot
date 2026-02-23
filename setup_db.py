import sqlite3

# Conectar ao banco de cartas
conn = sqlite3.connect("pokemon.db")
c = conn.cursor()

# Criar tabela de cartas
c.execute("""
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    tipo TEXT,
    hp INTEGER,
    estagio_evolucao TEXT,
    raridade TEXT,
    colecao TEXT,
    valor INTEGER,
    imagem TEXT,
    ataque1_nome TEXT,
    ataque1_dano INTEGER,
    ataque1_custo TEXT,
    ataque2_nome TEXT,
    ataque2_dano INTEGER,
    ataque2_custo TEXT,
    ataque3_nome TEXT,
    ataque3_dano INTEGER,
    ataque3_custo TEXT
)
""")
conn.commit()

# Inserir cartas de exemplo
cartas_exemplo = [
    (
        "Pikachu", "Elétrico", 70, "Básico", "Comum", "Base Set", 100,
        "https://imgur.com/2WtC2Ew",
        "Rosnadura", 30, "⚡",
        "Relampagochu", 30, "⚡⚡",
        None, None, None
    ),
    (
        "Charmander", "Fogo", 70, "Básico, "Comum", "Base Set", 100,
        "https://imgur.com/7tBvbG9",
        "Hálito de fogo constante", 30, "🔥🔥"
    ),
    (
        "Bulbasaur", "Planta", 90, "Básico", "Comum", "Base Set", 90,
        "https://imgur.com/aB685CK",
        "Aprisionamento", 10, "🍃",
        None, None, None,
        None, None, None
    )
]

c.executemany("""
INSERT INTO pokemon (
    nome, tipo, hp, estagio_evolucao, raridade, colecao, valor, imagem,
    ataque1_nome, ataque1_dano, ataque1_custo,
    ataque2_nome, ataque2_dano, ataque2_custo,
    ataque3_nome, ataque3_dano, ataque3_custo
) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
""", cartas_exemplo)
conn.commit()
conn.close()

# Criar banco de usuários
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    saldo INTEGER DEFAULT 100,
    inventario TEXT DEFAULT '',
    decks TEXT DEFAULT ''
)
""")
conn.commit()
conn.close()

print("Bancos criados com todas as informações!")
