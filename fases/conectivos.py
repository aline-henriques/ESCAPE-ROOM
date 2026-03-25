# Fase 1 - Conectivos

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
        titulo    = "MÓDULO 1 — FASE 1  |  CONECTIVOS",
        narrativa = [
            "  O painel de acesso da primeira porta está bloqueado.",
            "  Resolva a operação lógica para continuar.",
        ],
        enunciado = [
            "  Dados:  P = Verdadeiro  |  Q = Falso",
            "",
            "  Qual o valor de  ( P ∧ Q ) ?",
            "  (lembre-se: ∧ significa E lógico)",
        ],
        opcoes    = {"A": "Verdadeiro", "B": "Falso", "C": "Indeterminado"},
        correta   = "B",
        dica      = "P ∧ Q (E) só é V quando AMBOS são V.",
    )


def fase2() -> bool:
    return _rodar(
        titulo    = "MÓDULO 1 — FASE 2  |  CONECTIVOS",
        narrativa = [
            "  O segundo bloqueio exige conhecimento sobre disjunção.",
            "  Analise a expressão com cuidado.",
        ],
        enunciado = [
            "  Dados:  P = Falso  |  Q = Falso  |  R = Verdadeiro",
            "",
            "  Qual o valor de  ( P ∨ Q ) ∧ R  ?",
            "  (∨ = OU lógico  |  ∧ = E lógico)",
        ],
        opcoes    = {"A": "Verdadeiro", "B": "Falso", "C": "Nenhuma das alternativas"},
        correta   = "B",
        dica      = "P∨Q = F∨F = F. Então F∧R = F∧V = F.",
    )