# ============================================================
#  MÓDULO 1 — Conectivos Lógicos  |  Banco de perguntas
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
        "titulo":   "MÓDULO 1  |  CONECTIVOS LÓGICOS",
        "narrativa": ["  Resolva a operação lógica para desbloquear a porta."],
        "enunciado": ["  Dados:  P = Verdadeiro  |  Q = Falso", "",
                      "  Qual o valor de  ( P ∧ Q ) ?",
                      "  (∧ = E lógico)"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "P ∧ Q só é V quando AMBOS são V.",
    },
    {
        "titulo":   "MÓDULO 1  |  CONECTIVOS LÓGICOS",
        "narrativa": ["  Analise a expressão com disjunção e conjunção."],
        "enunciado": ["  Dados:  P = Falso  |  Q = Falso  |  R = Verdadeiro", "",
                      "  Qual o valor de  ( P ∨ Q ) ∧ R  ?",
                      "  (∨ = OU lógico  |  ∧ = E lógico)"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "P∨Q = F∨F = F. Então F ∧ V = F.",
    },
    {
        "titulo":   "MÓDULO 1  |  CONECTIVOS LÓGICOS",
        "narrativa": ["  Atenção ao operador ¬ aplicado a toda a expressão."],
        "enunciado": ["  Dados:  P = Verdadeiro  |  Q = Verdadeiro", "",
                      "  Qual o valor de  ¬( P ∧ ¬Q )  ?",
                      "  (¬ = negação)"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "A",
        "dica":     "¬Q = F. P ∧ F = F. ¬F = V.",
    },
    {
        "titulo":   "MÓDULO 1  |  CONECTIVOS LÓGICOS",
        "narrativa": ["  Avalie a disjunção com negação."],
        "enunciado": ["  Dados:  P = Falso  |  Q = Verdadeiro", "",
                      "  Qual o valor de  ¬P ∨ Q  ?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "A",
        "dica":     "¬P = V. V ∨ Q = V independente de Q.",
    },
    {
        "titulo":   "MÓDULO 1  |  CONECTIVOS LÓGICOS",
        "narrativa": ["  Expressão com três variáveis."],
        "enunciado": ["  Dados:  P = Verdadeiro  |  Q = Falso  |  R = Falso", "",
                      "  Qual o valor de  P ∧ ( Q ∨ R )  ?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "Q ∨ R = F ∨ F = F. P ∧ F = F.",
    },
    {
        "titulo":   "MÓDULO 1  |  CONECTIVOS LÓGICOS",
        "narrativa": ["  Avalie a expressão com dupla negação."],
        "enunciado": ["  Dados:  P = Falso", "",
                      "  Qual o valor de  ¬(¬P)  ?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "¬P = V. ¬(V) = F. Dupla negação retorna ao original.",
    },
    {
        "titulo":   "MÓDULO 1  |  CONECTIVOS LÓGICOS",
        "narrativa": ["  Analise a expressão composta."],
        "enunciado": ["  Dados:  P = Verdadeiro  |  Q = Verdadeiro  |  R = Falso", "",
                      "  Qual o valor de  ( P ∨ R ) ∧ ( Q ∨ R )  ?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "A",
        "dica":     "P∨R = V. Q∨R = V. V ∧ V = V.",
    },
    {
        "titulo":   "MÓDULO 1  |  CONECTIVOS LÓGICOS",
        "narrativa": ["  Avalie a negação da conjunção."],
        "enunciado": ["  Dados:  P = Verdadeiro  |  Q = Verdadeiro", "",
                      "  Qual o valor de  ¬( P ∧ Q )  ?"],
        "opcoes":   {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        "correta":  "B",
        "dica":     "P ∧ Q = V. ¬V = F.",
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