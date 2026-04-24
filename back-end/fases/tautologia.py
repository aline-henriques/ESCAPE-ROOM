# ============================================================
#  MÓDULO 5 — Tautologia / Contradição  |  Banco de perguntas
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
        "titulo":   "MÓDULO 5  |  TAUTOLOGIA / CONTRADIÇÃO",
        "narrativa": ["  Classifique a expressão para desarmar o sistema."],
        "enunciado": ["  Expressão:  P ∨ ¬P", "", "  Essa expressão é:"],
        "opcoes":   {"A": "Tautologia  (sempre Verdadeira)",
                     "B": "Contradição (sempre Falsa)",
                     "C": "Contingência (às vezes V, às vezes F)"},
        "correta":  "A",
        "dica":     "P∨¬P: sempre V independente de P.",
    },
    {
        "titulo":   "MÓDULO 5  |  TAUTOLOGIA / CONTRADIÇÃO",
        "narrativa": ["  Identifique a expressão que nunca pode ser verdadeira."],
        "enunciado": ["  Expressão:  P ∧ ¬P", "", "  Essa expressão é:"],
        "opcoes":   {"A": "Tautologia  (sempre Verdadeira)",
                     "B": "Contradição (sempre Falsa)",
                     "C": "Contingência (às vezes V, às vezes F)"},
        "correta":  "B",
        "dica":     "P e ¬P nunca têm o mesmo valor. Sempre F.",
    },
    {
        "titulo":   "MÓDULO 5  |  TAUTOLOGIA / CONTRADIÇÃO",
        "narrativa": ["  ⚠  ALERTA MÁXIMO — NÚCLEO SOBRECARREGADO!"],
        "enunciado": ["  Expressão:  [(P ∧ Q) → R]  ∨  ¬R", "",
                      "  → Se ¬R = V: expressão é V (pelo ∨)",
                      "  → Se R  = V: (P∧Q)→V é sempre V", "",
                      "  Essa expressão é:"],
        "opcoes":   {"A": "Tautologia  (sempre Verdadeira)",
                     "B": "Contradição (sempre Falsa)",
                     "C": "Contingência (às vezes V, às vezes F)"},
        "correta":  "A",
        "dica":     "Em todos os casos a expressão é V. Tautologia.",
    },
    {
        "titulo":   "MÓDULO 5  |  TAUTOLOGIA / CONTRADIÇÃO",
        "narrativa": ["  Classifique a expressão abaixo."],
        "enunciado": ["  Expressão:  P → P", "", "  Essa expressão é:"],
        "opcoes":   {"A": "Tautologia  (sempre Verdadeira)",
                     "B": "Contradição (sempre Falsa)",
                     "C": "Contingência (às vezes V, às vezes F)"},
        "correta":  "A",
        "dica":     "P→P: se P=V→V; se P=F→V. Sempre V.",
    },
    {
        "titulo":   "MÓDULO 5  |  TAUTOLOGIA / CONTRADIÇÃO",
        "narrativa": ["  Identifique a classificação desta expressão."],
        "enunciado": ["  Expressão:  P ∧ Q", "", "  Essa expressão é:"],
        "opcoes":   {"A": "Tautologia  (sempre Verdadeira)",
                     "B": "Contradição (sempre Falsa)",
                     "C": "Contingência (às vezes V, às vezes F)"},
        "correta":  "C",
        "dica":     "P∧Q depende dos valores de P e Q. Não é sempre V nem sempre F.",
    },
    {
        "titulo":   "MÓDULO 5  |  TAUTOLOGIA / CONTRADIÇÃO",
        "narrativa": ["  Classifique a expressão com implicação."],
        "enunciado": ["  Expressão:  (P ∧ ¬P) → Q", "", "  Essa expressão é:"],
        "opcoes":   {"A": "Tautologia  (sempre Verdadeira)",
                     "B": "Contradição (sempre Falsa)",
                     "C": "Contingência (às vezes V, às vezes F)"},
        "correta":  "A",
        "dica":     "P∧¬P = F (contradição). F→Q é sempre V.",
    },
    {
        "titulo":   "MÓDULO 5  |  TAUTOLOGIA / CONTRADIÇÃO",
        "narrativa": ["  Analise a expressão com disjunção."],
        "enunciado": ["  Expressão:  P ∨ Q", "", "  Essa expressão é:"],
        "opcoes":   {"A": "Tautologia  (sempre Verdadeira)",
                     "B": "Contradição (sempre Falsa)",
                     "C": "Contingência (às vezes V, às vezes F)"},
        "correta":  "C",
        "dica":     "P∨Q é F quando P=F e Q=F, e V nos demais casos.",
    },
    {
        "titulo":   "MÓDULO 5  |  TAUTOLOGIA / CONTRADIÇÃO",
        "narrativa": ["  Classifique a expressão com bicondicional."],
        "enunciado": ["  Expressão:  (P → Q) ∧ (¬P → ¬Q)", "", "  Essa expressão é:"],
        "opcoes":   {"A": "Tautologia  (sempre Verdadeira)",
                     "B": "Contradição (sempre Falsa)",
                     "C": "Contingência (às vezes V, às vezes F)"},
        "correta":  "C",
        "dica":     "Essa expressão equivale a P↔Q, que é contingência.",
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