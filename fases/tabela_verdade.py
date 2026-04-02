# ============================================================
#  MÓDULO 2 — Tabela-Verdade  |  Banco de perguntas
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
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Descubra o valor da implicação para desbloquear o sistema."],
        "enunciado": ["  Expressão: P → Q", "",
                      "  P = Verdadeiro  |  Q = Verdadeiro", "",
                      "  Qual o valor de P → Q?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Depende do contexto"},
        "correta":  "A",
        "dica":     "P→Q só é F quando P=V e Q=F.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  A tabela está quase completa — falta apenas uma linha."],
        "enunciado": ["  Expressão: P → Q", "",
                      "    ┌───────┬───────┬─────────┐",
                      "    │   P   │   Q   │  P → Q  │",
                      "    ├───────┼───────┼─────────┤",
                      "    │   V   │   V   │    V    │",
                      "    │   V   │   F   │    F    │",
                      "    │   F   │   V   │    V    │",
                      "    │   F   │   F   │   ???   │",
                      "    └───────┴───────┴─────────┘", "",
                      "  Qual o valor quando P=F e Q=F?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Impossível determinar"},
        "correta":  "A",
        "dica":     "Premissa falsa torna a implicação automaticamente V.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Analise a expressão composta e monte a tabela mentalmente."],
        "enunciado": ["  Expressão:  (P ∧ Q) → (P ∨ R)", "",
                      "  Para quantas linhas da tabela-verdade completa",
                      "  essa expressão é FALSA?"],
        "opcoes":   {"A": "0 — é sempre verdadeira (tautologia)",
                     "B": "1 linha", "C": "2 linhas", "D": "4 linhas"},
        "correta":  "A",
        "dica":     "Se P∧Q=V então P=V, logo P∨R=V. Nunca é falsa.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Avalie o bicondicional na tabela-verdade."],
        "enunciado": ["  Expressão: P ↔ Q", "",
                      "  P = Verdadeiro  |  Q = Falso", "",
                      "  Qual o valor de P ↔ Q?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "P↔Q é V somente quando P e Q têm o mesmo valor.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Complete a tabela-verdade da disjunção."],
        "enunciado": ["  Expressão: P ∨ Q", "",
                      "  P = Falso  |  Q = Falso", "",
                      "  Qual o valor de P ∨ Q?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "P∨Q é F somente quando AMBOS são F.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Avalie a expressão com negação na tabela."],
        "enunciado": ["  Expressão: ¬P ∧ Q", "",
                      "  P = Falso  |  Q = Verdadeiro", "",
                      "  Qual o valor de ¬P ∧ Q?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "A",
        "dica":     "¬P = V. V ∧ Q = V ∧ V = V.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Avalie a implicação com premissa falsa."],
        "enunciado": ["  Expressão: P → Q", "",
                      "  P = Falso  |  Q = Verdadeiro", "",
                      "  Qual o valor de P → Q?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "A",
        "dica":     "Quando P=F, P→Q é sempre V independente de Q.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Avalie a conjunção na tabela-verdade."],
        "enunciado": ["  Expressão: P ∧ Q", "",
                      "  P = Verdadeiro  |  Q = Verdadeiro", "",
                      "  Qual o valor de P ∧ Q?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "A",
        "dica":     "P ∧ Q é V somente quando AMBOS são V.",
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


def sortear(n=3):
    return random.sample(BANCO, min(n, len(BANCO)))