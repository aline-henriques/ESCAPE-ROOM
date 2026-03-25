# Fase 5 - Tautologias, Contradições e Contingências

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
        titulo    = "MÓDULO 5 — FASE 1  |  TAUTOLOGIA / CONTRADIÇÃO",
        narrativa = [
            "  O sistema de autodestruição analisa expressões lógicas.",
            "  Classifique corretamente para desarmá-lo.",
        ],
        enunciado = [
            "  Expressão:  P ∨ ¬P",
            "",
            "  Essa expressão é:",
        ],
        opcoes    = {
            "A": "Tautologia  (sempre Verdadeira)",
            "B": "Contradição (sempre Falsa)",
            "C": "Contingência (às vezes V, às vezes F)",
        },
        correta   = "A",
        dica      = "P∨¬P: se P=V→V; se P=F→¬P=V→V. Sempre V = tautologia.",
    )


def fase2() -> bool:
    return _rodar(
        titulo    = "MÓDULO 5 — FASE 2  |  TAUTOLOGIA / CONTRADIÇÃO",
        narrativa = [
            "  O segundo código de desarmamento envolve uma contradição.",
            "  Identifique a expressão que nunca pode ser verdadeira.",
        ],
        enunciado = [
            "  Expressão:  P ∧ ¬P",
            "",
            "  Essa expressão é:",
        ],
        opcoes    = {
            "A": "Tautologia  (sempre Verdadeira)",
            "B": "Contradição (sempre Falsa)",
            "C": "Contingência (às vezes V, às vezes F)",
        },
        correta   = "B",
        dica      = "P∧¬P: P e ¬P nunca têm o mesmo valor. Sempre F = contradição.",
    )