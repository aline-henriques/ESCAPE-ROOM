# Fase 3 - Implicações Lógicas

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
        titulo    = "MÓDULO 3 — FASE 1  |  IMPLICAÇÃO LÓGICA",
        subtitulo = "Nível: Fácil",
        narrativa = [
            "  A IA de bordo apresenta um argumento.",
            "  Você precisa identificar se ele é VÁLIDO.",
        ],
        enunciado = [
            '  "Se chove, então a rua fica molhada."',
            '  "Está chovendo."',
            '  "Logo: a rua está molhada."',
            "",
            "  Esse argumento é logicamente válido?",
        ],
        opcoes    = {
            "A": "Sim — é válido (Modus Ponens)",
            "B": "Não — é inválido (falácia)",
        },
        correta   = "A",
        dica      = "P→Q, P. Logo Q. Isso é Modus Ponens — argumento válido.",
    )


def fase2() -> bool:
    return _rodar(
        titulo    = "MÓDULO 3 — FASE 2  |  IMPLICAÇÃO LÓGICA",
        subtitulo = "Nível: Médio",
        narrativa = [
            "  A IA tenta enganar você com um argumento parecido.",
            "  Cuidado: nem todo raciocínio aparentemente correto é válido.",
        ],
        enunciado = [
            '  "Se o alarme está LIGADO, então há invasão."',
            '  "O alarme está DESLIGADO."',
            '  "Logo: NÃO há invasão."',
            "",
            "  Esse argumento é logicamente válido?",
        ],
        opcoes    = {
            "A": "Sim — é válido",
            "B": "Não — é inválido (falácia da negação do antecedente)",
        },
        correta   = "B",
        dica      = "P→Q, ¬P. NÃO podemos concluir ¬Q. Isso é uma falácia.",
    )


def fase3() -> bool:
    return _rodar(
        titulo    = "MÓDULO 3 — FASE 3  |  IMPLICAÇÃO LÓGICA",
        subtitulo = "Nível: Difícil",
        narrativa = [
            "  O sistema de segurança usa um argumento em cadeia.",
            "  Analise cada passo antes de responder.",
        ],
        enunciado = [
            '  "Se há falha no reator (P), então a pressão sobe (Q)."',
            '  "Se a pressão sobe (Q), então o alarme dispara (R)."',
            '  "O alarme NÃO disparou (¬R)."',
            "",
            "  O que podemos concluir?",
        ],
        opcoes    = {
            "A": "Há falha no reator (P é verdadeiro)",
            "B": "Não há falha no reator (¬P) — Modus Tollens",
            "C": "Não podemos concluir nada",
            "D": "A pressão subiu mesmo assim",
        },
        correta   = "B",
        dica      = "P→Q, Q→R, ¬R. Modus Tollens: ¬R→¬Q→¬P. Logo ¬P.",
    )