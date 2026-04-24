# ============================================================
#  MÓDULO 3 — Implicação Lógica  |  Banco de perguntas
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
        "titulo":   "MÓDULO 3  |  IMPLICAÇÃO LÓGICA",
        "narrativa": ["  A IA apresenta um argumento. Identifique se é VÁLIDO."],
        "enunciado": ['  "Se chove, então a rua fica molhada."',
                      '  "Está chovendo."',
                      '  "Logo: a rua está molhada."', "",
                      "  Esse argumento é logicamente válido?"],
        "opcoes":   {"A": "Sim — é válido (Modus Ponens)",
                     "B": "Não — é inválido (falácia)"},
        "correta":  "A",
        "dica":     "P→Q, P. Logo Q. Isso é Modus Ponens — válido.",
    },
    {
        "titulo":   "MÓDULO 3  |  IMPLICAÇÃO LÓGICA",
        "narrativa": ["  A IA tenta enganar você com um argumento parecido."],
        "enunciado": ['  "Se o alarme está LIGADO, então há invasão."',
                      '  "O alarme está DESLIGADO."',
                      '  "Logo: NÃO há invasão."', "",
                      "  Esse argumento é logicamente válido?"],
        "opcoes":   {"A": "Sim — é válido",
                     "B": "Não — é inválido (falácia da negação do antecedente)"},
        "correta":  "B",
        "dica":     "P→Q, ¬P. NÃO podemos concluir ¬Q. Isso é uma falácia.",
    },
    {
        "titulo":   "MÓDULO 3  |  IMPLICAÇÃO LÓGICA",
        "narrativa": ["  Argumento em cadeia. Analise cada passo."],
        "enunciado": ['  "Se há falha no reator (P), a pressão sobe (Q)."',
                      '  "Se a pressão sobe (Q), o alarme dispara (R)."',
                      '  "O alarme NÃO disparou (¬R)."', "",
                      "  O que podemos concluir?"],
        "opcoes":   {"A": "Há falha no reator (P é verdadeiro)",
                     "B": "Não há falha no reator (¬P) — Modus Tollens",
                     "C": "Não podemos concluir nada",
                     "D": "A pressão subiu mesmo assim"},
        "correta":  "B",
        "dica":     "P→Q, Q→R, ¬R. Modus Tollens: ¬R→¬Q→¬P.",
    },
    {
        "titulo":   "MÓDULO 3  |  IMPLICAÇÃO LÓGICA",
        "narrativa": ["  A IA afirma o consequente. Cuidado!"],
        "enunciado": ['  "Se o sistema está infectado (P), há lentidão (Q)."',
                      '  "Há lentidão (Q)."',
                      '  "Logo: o sistema está infectado (P)."', "",
                      "  Esse argumento é logicamente válido?"],
        "opcoes":   {"A": "Sim — é válido",
                     "B": "Não — é inválido (falácia da afirmação do consequente)"},
        "correta":  "B",
        "dica":     "P→Q, Q. NÃO podemos concluir P. Há outras causas para Q.",
    },
    {
        "titulo":   "MÓDULO 3  |  IMPLICAÇÃO LÓGICA",
        "narrativa": ["  Avalie o Modus Tollens."],
        "enunciado": ['  "Se a senha está correta (P), o acesso é liberado (Q)."',
                      '  "O acesso NÃO foi liberado (¬Q)."',
                      '  "Logo: a senha está incorreta (¬P)."', "",
                      "  Esse argumento é logicamente válido?"],
        "opcoes":   {"A": "Sim — é válido (Modus Tollens)",
                     "B": "Não — é inválido (falácia)"},
        "correta":  "A",
        "dica":     "P→Q, ¬Q. Logo ¬P. Isso é Modus Tollens — válido.",
    },
    {
        "titulo":   "MÓDULO 3  |  IMPLICAÇÃO LÓGICA",
        "narrativa": ["  Analise o argumento com cuidado."],
        "enunciado": ['  "Se há energia (P), as luzes acendem (Q)."',
                      '  "As luzes NÃO acenderam (¬Q)."',
                      '  "Logo: não há energia (¬P)."', "",
                      "  Esse argumento é logicamente válido?"],
        "opcoes":   {"A": "Sim — é válido (Modus Tollens)",
                     "B": "Não — é inválido"},
        "correta":  "A",
        "dica":     "P→Q, ¬Q → ¬P. Modus Tollens válido.",
    },
    {
        "titulo":   "MÓDULO 3  |  IMPLICAÇÃO LÓGICA",
        "narrativa": ["  Identifique a falácia neste argumento."],
        "enunciado": ['  "Se treino muito (P), fico em forma (Q)."',
                      '  "Não treino muito (¬P)."',
                      '  "Logo: não fico em forma (¬Q)."', "",
                      "  Esse argumento é logicamente válido?"],
        "opcoes":   {"A": "Sim — é válido",
                     "B": "Não — é inválido (negação do antecedente)"},
        "correta":  "B",
        "dica":     "Pode-se ficar em forma por outros meios. ¬P não implica ¬Q.",
    },
    {
        "titulo":   "MÓDULO 3  |  IMPLICAÇÃO LÓGICA",
        "narrativa": ["  Avalie o argumento hipotético encadeado."],
        "enunciado": ['  "Se estudo (P), passo na prova (Q)."',
                      '  "Se passo na prova (Q), me formo (R)."',
                      '  "Estudo (P)."', "",
                      "  O que podemos concluir?"],
        "opcoes":   {"A": "Me formo (R) — argumento válido",
                     "B": "Passo na prova (Q) apenas",
                     "C": "Não podemos concluir nada",
                     "D": "O argumento é inválido"},
        "correta":  "A",
        "dica":     "P→Q, Q→R, P. Por Modus Ponens encadeado: R.",
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