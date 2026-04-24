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
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "A",
        "dica":     "P→Q só é F quando P=V e Q=F.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  A tabela está quase completa — falta apenas uma linha."],
        "enunciado": ["  Qual o valor de P → Q quando P=F e Q=F?", "",
                      "  Lembre-se da regra da Condicional."],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Impossível determinar"},
        "correta":  "A",
        "dica":     "Se a premissa (P) é falsa, a implicação é sempre V.",
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
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Analise a Disjunção Exclusiva (XOR)."],
        "enunciado": ["  Expressão: P ⊕ Q", "",
                      "  P = Verdadeiro  |  Q = Verdadeiro", "",
                      "  Qual o valor de P ⊕ Q?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "No OU exclusivo, valores iguais resultam em Falso.",
    },
    {
        "titulo":   "MÓDULO 2  |  TABELA-VERDADE",
        "narrativa": ["  Verificando o sensor de negação dupla."],
        "enunciado": ["  Se P = Falso, qual o valor de ¬(¬P)?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "A negação da negação volta ao valor original.",
    }
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
            print(f"  💡 Dica: {pergunta['dica']}")

    if timer: timer.parar()
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