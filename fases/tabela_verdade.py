# Fase 2 - Tabelas Verdades

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
        titulo    = "MÓDULO 2 — FASE 1  |  TABELA-VERDADE",
        subtitulo = "Nível: Fácil",
        narrativa = [
            "  O painel exibe uma tabela-verdade com um valor oculto.",
            "  Descubra o resultado para desbloquear o sistema.",
        ],
        enunciado = [
            "  Expressão: P → Q  (Se P, então Q)",
            "",
            "    P = Verdadeiro  |  Q = Verdadeiro",
            "",
            "  Qual o valor de P → Q?",
        ],
        opcoes    = {"A": "Verdadeiro", "B": "Falso", "C": "Depende do contexto"},
        correta   = "A",
        dica      = "P→Q só é F quando P=V e Q=F. Aqui Q=V, então o resultado é V.",
    )


def fase2() -> bool:
    return _rodar(
        titulo    = "MÓDULO 2 — FASE 2  |  TABELA-VERDADE",
        subtitulo = "Nível: Médio",
        narrativa = [
            "  A tabela está quase completa — falta apenas uma linha.",
            "  Analise com atenção o caso em que a premissa é falsa.",
        ],
        enunciado = [
            "  Expressão: P → Q",
            "",
            "    ┌───────┬───────┬─────────┐",
            "    │   P   │   Q   │  P → Q  │",
            "    ├───────┼───────┼─────────┤",
            "    │   V   │   V   │    V    │",
            "    │   V   │   F   │    F    │",
            "    │   F   │   V   │    V    │",
            "    │   F   │   F   │   ???   │",
            "    └───────┴───────┴─────────┘",
            "",
            "  Qual o valor de P → Q quando P=F e Q=F?",
        ],
        opcoes    = {"A": "Verdadeiro", "B": "Falso", "C": "Impossível determinar"},
        correta   = "A",
        dica      = "Premissa falsa torna a implicação automaticamente V.",
    )


def fase3() -> bool:
    return _rodar(
        titulo    = "MÓDULO 2 — FASE 3  |  TABELA-VERDADE",
        subtitulo = "Nível: Difícil",
        narrativa = [
            "  O sistema exige a análise de uma expressão composta.",
            "  Monte a tabela-verdade mentalmente antes de responder.",
        ],
        enunciado = [
            "  Expressão:  (P ∧ Q) → (P ∨ R)",
            "",
            "  Para quantas linhas da tabela-verdade completa",
            "  (P, Q, R com todos os valores possíveis)",
            "  essa expressão é FALSA?",
        ],
        opcoes    = {
            "A": "0 linhas — é sempre verdadeira (tautologia)",
            "B": "1 linha",
            "C": "2 linhas",
            "D": "4 linhas",
        },
        correta   = "A",
        dica      = "Se P∧Q=V então P=V, logo P∨R=V. A implicação nunca é falsa.",
    )