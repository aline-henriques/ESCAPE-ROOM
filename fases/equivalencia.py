# Fase 4 - Equivalências Lógicas

import time
from utils.display import (
    escrever, imprimir_cabecalho, imprimir_separador,
    imprimir_sucesso, imprimir_falha, imprimir_fim_de_jogo,
    perguntar_multipla_escolha,
)
from config import MAX_TENTATIVAS, TIMER_ATIVO, TIMER_SEGUNDOS


def _rodar(titulo, subtitulo, narrativa, enunciado, opcoes, correta, dica):
    imprimir_cabecalho(titulo, subtitulo)
    for linha in narrativa:
        escrever(linha)
    print()
    imprimir_separador()
    for linha in enunciado:
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
        resposta = perguntar_multipla_escolha(opcoes)
        if resposta == correta:
            if timer: timer.parar()
            imprimir_sucesso()
            return True
        else:
            imprimir_falha(tentativa, MAX_TENTATIVAS)

    if timer: timer.parar()
    escrever(f"  💡 Dica: {dica}")
    imprimir_fim_de_jogo()
    return False


def fase1() -> bool:
    return _rodar(
        titulo    = "MÓDULO 4 — FASE 1  |  EQUIVALÊNCIA LÓGICA",
        subtitulo = "Nível: Fácil",
        narrativa = [
            "  O circuito de propulsão precisa de um fio substituto.",
            "  Encontre a expressão equivalente ao circuito original.",
        ],
        enunciado = [
            "  Circuito original:  P → Q",
            "",
            "  Qual expressão é logicamente equivalente?",
        ],
        opcoes    = {
            "A": "¬P ∨ Q",
            "B": "P ∧ ¬Q",
            "C": "¬P ∧ ¬Q",
            "D": "P ∨ Q",
        },
        correta   = "A",
        dica      = "Lei da implicação: P→Q ≡ ¬P∨Q.",
    )


def fase2() -> bool:
    return _rodar(
        titulo    = "MÓDULO 4 — FASE 2  |  EQUIVALÊNCIA LÓGICA",
        subtitulo = "Nível: Médio",
        narrativa = [
            "  O segundo circuito usa uma lei de De Morgan.",
            "  Simplifique a expressão para reconectar o sistema.",
        ],
        enunciado = [
            "  Circuito original:  ¬(P ∨ Q)",
            "",
            "  Qual expressão é logicamente equivalente?",
            "  (Use as Leis de De Morgan)",
        ],
        opcoes    = {
            "A": "¬P ∨ ¬Q",
            "B": "¬P ∧ ¬Q",
            "C": "P ∧ Q",
            "D": "¬P ∨ Q",
        },
        correta   = "B",
        dica      = "De Morgan: ¬(P∨Q) ≡ ¬P∧¬Q.",
    )


def fase3() -> bool:
    return _rodar(
        titulo    = "MÓDULO 4 — FASE 3  |  EQUIVALÊNCIA LÓGICA",
        subtitulo = "Nível: Difícil",
        narrativa = [
            "  O núcleo do sistema exige a contrapositiva.",
            "  Essa é a última trava antes da fase final.",
        ],
        enunciado = [
            "  Circuito original:  P → Q",
            "",
            "  Qual das expressões abaixo é a CONTRAPOSITIVA",
            "  de P → Q e também lhe é equivalente?",
        ],
        opcoes    = {
            "A": "Q → P",
            "B": "¬P → ¬Q",
            "C": "¬Q → ¬P",
            "D": "¬P → Q",
        },
        correta   = "C",
        dica      = "Contrapositiva de P→Q é ¬Q→¬P. Sempre equivalente ao original.",
    )