# ============================================================
#  ESCAPE ROOM LÓGICO — Controlador do Jogo
# ============================================================

import time
from utils.display import (
    escrever, imprimir_separador, imprimir_vitoria,
    imprimir_banner_assunto,
)
from fases import conectivos, tabela_verdade, implicacao, equivalencia, tautologia

MODULOS = [
    {"nome": "Conectivos Lógicos",                    "modulo": conectivos},
    {"nome": "Tabela-Verdade",                        "modulo": tabela_verdade},
    {"nome": "Implicação Lógica",                     "modulo": implicacao},
    {"nome": "Equivalência Lógica",                   "modulo": equivalencia},
    {"nome": "Tautologia / Contradição / Contingência","modulo": tautologia},
]


def _teste_entrada() -> None:
    escrever("  Antes de iniciar, prove que você merece entrar na nave...")
    time.sleep(0.5)
    print()
    escrever("  📋  TESTE DE ADMISSÃO:")
    imprimir_separador()
    print()
    escrever("  Considere as proposições:")
    print()
    escrever("     P: Se eu estudar")
    escrever("     Q: Vou conseguir passar na prova do professor Lucas")
    print()
    escrever("  Questão: Traduza  ( P → Q )  para linguagem natural.")
    print()
    imprimir_separador()

    respostas_aceitas = [
        "se eu estudar, vou conseguir passar na prova do professor lucas",
        "se eu estudar vou conseguir passar na prova do professor lucas",
        "se eu estudar, então vou conseguir passar na prova do professor lucas",
        "se eu estudar então vou conseguir passar na prova do professor lucas",
        "se estudar, vou passar na prova do professor lucas",
        "se estudar vou passar na prova do professor lucas",
        "se eu estudar, passarei na prova do professor lucas",
        "se eu estudar passarei na prova do professor lucas",
        "Se eu estudar, então vou conseguir passar na prova do professor Lucas"
    ]

    while True:
        print()
        resposta = input("  > Digite a tradução: ").strip().lower()
        if resposta in respostas_aceitas:
            escrever("\n  ✅  Admissão aprovada! Você está pronto para a missão.")
            time.sleep(0.8)
            break
        else:
            escrever("  ❌  Não foi dessa vez. Lembre-se: P → Q = 'Se P, então Q'.\n")


def _introducao() -> None:
    print("\n" + "═" * 56)
    escrever("  🛸  NAVE INTERESTELAR X-17")
    escrever("      SISTEMA DE SEGURANÇA ATIVADO")
    print("═" * 56)
    print()
    time.sleep(0.3)
    escrever("  Ano 2157. Sua nave foi capturada por um vírus lógico.")
    escrever("  Todos os 5 módulos de segurança estão bloqueados.")
    escrever("  Cada módulo sorteará 3 perguntas aleatórias do seu banco.")
    escrever("  A cada partida as perguntas serão diferentes!\n")
    escrever("  Você tem  tentativas por desafio.")
    escrever("  Erre demais e a nave se autodestruirá.\n")
    time.sleep(0.5)
    _teste_entrada()
    print()
    input("  [ Pressione ENTER para iniciar a missão ] ")
    print()


def _transicao(proxima: str) -> None:
    print()
    imprimir_separador()
    escrever(f"  🔓  Próximo desafio...")
    time.sleep(0.8)


def _derrota(modulo_nome: str) -> None:
    print()
    escrever(f"  💥  Falha no módulo: {modulo_nome}")
    escrever("  A nave entrou em colapso. Missão encerrada.")
    print()


def iniciar() -> None:
    _introducao()

    total = len(MODULOS) * 3
    concluidos = 0

    for i, item in enumerate(MODULOS):
        imprimir_banner_assunto(item["nome"])

        perguntas = item["modulo"].sortear(3)

        for j, pergunta in enumerate(perguntas):
            passou = item["modulo"]._rodar(pergunta)

            if not passou:
                _derrota(item["nome"])
                return

            concluidos += 1
            escrever(f"  📊  Progresso: {concluidos}/{total} desafios concluídos.")

            if j + 1 < len(perguntas):
                _transicao(item["nome"])

        if i + 1 < len(MODULOS):
            print()
            escrever("  ✨  MÓDULO COMPLETO! Avançando para o próximo...")
            time.sleep(1)
            imprimir_banner_assunto(MODULOS[i + 1]["nome"])

    imprimir_vitoria()