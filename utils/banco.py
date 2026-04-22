import sqlite3

def conectar():
    return sqlite3.connect("save_game.db")

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
            nome TEXT PRIMARY KEY,
            pontuacao INTEGER DEFAULT 0,
            modulo_atual INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def salvar_progresso(nome, pontos, modulo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jogadores (nome, pontuacao, modulo_atual)
        VALUES (?, ?, ?)
        ON CONFLICT(nome) DO UPDATE SET
            pontuacao = excluded.pontuacao,
            modulo_atual = excluded.modulo_atual
    """, (nome, pontos, modulo))
    conn.commit()
    conn.close()

def obter_ranking():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, pontuacao FROM jogadores ORDER BY pontuacao DESC LIMIT 5")
    ranking = cursor.fetchall()
    conn.close()
    return ranking

def carregar_jogador(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT pontuacao, modulo_atual FROM jogadores WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado