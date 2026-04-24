# ============================================================
#  MÓDULO 4 — Equivalência Lógica  |  Banco de perguntas
# ============================================================

import random
from utils.display import (
    escrever, imprimir_cabecalho, imprimir_separador,
    imprimir_sucesso, imprimir_falha, imprimir_fim_de_jogo,
    perguntar_multipla_escolha,
)
from config import MAX_TENTATIVAS, TIMER_ATIVO, TIMER_SEGUNDOS

BANCO = [
    {
        "titulo":   "MÓDULO 4  |  EQUIVALÊNCIA LÓGICA",
        "narrativa": ["  Encontre a expressão equivalente ao circuito original."],
        "enunciado": ["  Circuito original:  P → Q", "",
                      "  Qual expressão é logicamente equivalente?"],
        "opcoes":   {"A": "¬P ∨ Q", "B": "P ∧ ¬Q",
                     "C": "¬P ∧ ¬Q", "D": "P ∨ Q"},
        "correta":  "A",
        "dica":     "Lei da implicação: P→Q ≡ ¬P∨Q.",
    },
    {
        "titulo":   "MÓDULO 4  |  EQUIVALÊNCIA LÓGICA",
        "narrativa": ["  Use a Lei de De Morgan para simplificar."],
        "enunciado": ["  Expressão original:  ¬(P ∨ Q)", "",
                      "  Qual expressão é logicamente equivalente?"],
        "opcoes":   {"A": "¬P ∨ ¬Q", "B": "¬P ∧ ¬Q",
                     "C": "P ∧ Q",   "D": "¬P ∨ Q"},
        "correta":  "B",
        "dica":     "De Morgan: ¬(P∨Q) ≡ ¬P∧¬Q.",
    },
    {
        "titulo":   "MÓDULO 4  |  EQUIVALÊNCIA LÓGICA",
        "narrativa": ["  Encontre a contrapositiva da implicação."],
        "enunciado": ["  Expressão original:  P → Q", "",
                      "  Qual é a CONTRAPOSITIVA equivalente?"],
        "opcoes":   {"A": "Q → P", "B": "¬P → ¬Q",
                     "C": "¬Q → ¬P", "D": "¬P → Q"},
        "correta":  "C",
        "dica":     "Contrapositiva de P→Q é ¬Q→¬P. Sempre equivalente.",
    },
    {
        "titulo":   "MÓDULO 4  |  EQUIVALÊNCIA LÓGICA",
        "narrativa": ["  Aplique De Morgan à conjunção."],
        "enunciado": ["  Expressão original:  ¬(P ∧ Q)", "",
                      "  Qual expressão é logicamente equivalente?"],
        "opcoes":   {"A": "¬P ∧ ¬Q", "B": "¬P ∨ ¬Q",
                     "C": "P ∨ Q",   "D": "P ∧ Q"},
        "correta":  "B",
        "dica":     "De Morgan: ¬(P∧Q) ≡ ¬P∨¬Q.",
    },
    {
        "titulo":   "MÓDULO 4  |  EQUIVALÊNCIA LÓGICA",
        "narrativa": ["  Identifique a equivalência do bicondicional."],
        "enunciado": ["  Expressão original:  P ↔ Q", "",
                      "  Qual expressão é logicamente equivalente?"],
        "opcoes":   {"A": "(P → Q) ∧ (Q → P)",
                     "B": "(P ∧ Q) ∨ (¬P ∧ ¬Q)",
                     "C": "As duas anteriores são equivalentes",
                     "D": "Nenhuma das anteriores"},
        "correta":  "C",
        "dica":     "P↔Q ≡ (P→Q)∧(Q→P) ≡ (P∧Q)∨(¬P∧¬Q).",
    },
    {
        "titulo":   "MÓDULO 4  |  EQUIVALÊNCIA LÓGICA",
        "narrativa": ["  Use a lei da implicação para reescrever."],
        "enunciado": ["  Expressão original:  ¬P → Q", "",
                      "  Qual expressão é logicamente equivalente?"],
        "opcoes":   {"A": "P ∨ Q", "B": "P ∧ Q",
                     "C": "¬P ∨ Q", "D": "¬P ∧ ¬Q"},
        "correta":  "A",
        "dica":     "¬P→Q ≡ ¬(¬P)∨Q ≡ P∨Q.",
    },
    {
        "titulo":   "MÓDULO 4  |  EQUIVALÊNCIA LÓGICA",
        "narrativa": ["  Simplifique usando dupla negação e De Morgan."],
        "enunciado": ["  Expressão original:  ¬(¬P ∧ ¬Q)", "",
                      "  Qual expressão é logicamente equivalente?"],
        "opcoes":   {"A": "P ∧ Q", "B": "¬P ∨ ¬Q",
                     "C": "P ∨ Q", "D": "¬P ∧ Q"},
        "correta":  "C",
        "dica":     "De Morgan: ¬(¬P∧¬Q) ≡ ¬(¬P)∨¬(¬Q) ≡ P∨Q.",
    },
    {
        "titulo":   "MÓDULO 4  |  EQUIVALÊNCIA LÓGICA",
        "narrativa": ["  Reescreva a implicação usando negação."],
        "enunciado": ["  Expressão original:  P → ¬Q", "",
                      "  Qual expressão é logicamente equivalente?"],
        "opcoes":   {"A": "¬P ∨ ¬Q", "B": "P ∧ Q",
                     "C": "¬P ∧ Q",  "D": "P ∨ ¬Q"},
        "correta":  "A",
        "dica":     "P→¬Q ≡ ¬P∨¬Q pela lei da implicação.",
    },
]


def _rodar(pergunta):
    imprimir_cabecalho(pergunta["titulo"])
    for linha in pergunta["narrativa"]:
        escrever(linha)
    print()
    imprimir_separador()
    for linha in pergunta["enunciado"]:
        escrever(linha) if linha else print()
    imprimir_separador()

    timer = None
    if TIMER_ATIVO:
        from utils.timer import Timer
        timer = Timer(TIMER_SEGUNDOS)
        timer.iniciar()

    for tentativa in range(1, MAX_TENTATIVAS + 1):
        if timer and timer.expirado:
            imprimir_fim_de_jogo()
            return False
        resposta = perguntar_multipla_escolha(pergunta["opcoes"])
        if resposta == pergunta["correta"]:
            if timer: timer.parar()
            imprimir_sucesso()
            return True
        else:
            imprimir_falha(tentativa, MAX_TENTATIVAS)

    if timer: timer.parar()
    escrever(f"  💡 Dica: {pergunta['dica']}")
    imprimir_fim_de_jogo()
    return False

perguntas_disponiveis = BANCO.copy()

def sortear(n=3):
    global perguntas_disponiveis
    
    quantidade = min(n, len(perguntas_disponiveis))
    
    if quantidade == 0:
        return []

    selecionadas = random.sample(perguntas_disponiveis, quantidade)
    
    for p in selecionadas:
        perguntas_disponiveis.remove(p)
        
    return selecionadas

def resetar_modulo():
    global perguntas_disponiveis
    perguntas_disponiveis = BANCO.copy()