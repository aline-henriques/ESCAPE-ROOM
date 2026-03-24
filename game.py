# Fluxo, tentativas e estado

import time
from utils.display import (
    escrever, imprimir_separador, imprimir_vitoria,
    imprimir_banner_assunto, perguntar_multipla_escolha,
)
from fases import conectivos, tabela_verdade, implicacao, equivalencia, tautologia

MODULOS = [
    {
        "nome":  "Conectivos Lógicos",
        "fases": [
            ("Fase 1 — Fácil",   conectivos.fase1),
            ("Fase 2 — Médio",   conectivos.fase2),
            ("Fase 3 — Difícil", conectivos.fase3),
        ],
    },
    {
        "nome":  "Tabela-Verdade",
        "fases": [
            ("Fase 1 — Fácil",   tabela_verdade.fase1),
            ("Fase 2 — Médio",   tabela_verdade.fase2),
            ("Fase 3 — Difícil", tabela_verdade.fase3),
        ],
    },
    {
        "nome":  "Implicação Lógica",
        "fases": [
            ("Fase 1 — Fácil",   implicacao.fase1),
            ("Fase 2 — Médio",   implicacao.fase2),
            ("Fase 3 — Difícil", implicacao.fase3),
        ],
    },
    {
        "nome":  "Equivalência Lógica",
        "fases": [
            ("Fase 1 — Fácil",   equivalencia.fase1),
            ("Fase 2 — Médio",   equivalencia.fase2),
            ("Fase 3 — Difícil", equivalencia.fase3),
        ],
    },
    {
        "nome":  "Tautologia / Contradição / Contingência",
        "fases": [
            ("Fase 1 — Fácil",   tautologia.fase1),
            ("Fase 2 — Médio",   tautologia.fase2),
            ("Fase 3 — Difícil", tautologia.fase3),
        ],
    },
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
    escrever("  Cada módulo tem 3 desafios: fácil, médio e difícil.")
    escrever("  Resolva todos os 15 desafios para libertar a nave!\n")
    escrever("  Você tem 3 tentativas por desafio.")
    escrever("  Erre demais e a nave se autodestruirá.\n")
    time.sleep(0.5)
    _teste_entrada()
    print()
    input("  [ Pressione ENTER para iniciar a missão ] ")
    print()


def _transicao_fase(proxima_nome: str) -> None:
    print()
    imprimir_separador()
    escrever(f"  🔓  Próximo desafio: {proxima_nome}...")
    time.sleep(0.8)


def _transicao_modulo(proximo_modulo: str) -> None:
    print()
    escrever("  ✨  MÓDULO COMPLETO! Avançando para o próximo...")
    time.sleep(1)
    imprimir_banner_assunto(proximo_modulo)


def _derrota(fase_nome: str) -> None:
    print()
    escrever(f"  💥  Falha em: {fase_nome}")
    escrever("  A nave entrou em colapso. Missão encerrada.")
    print()


def iniciar() -> None:
    _introducao()

    total_fases = sum(len(m["fases"]) for m in MODULOS)
    fases_ok    = 0

    for i, modulo in enumerate(MODULOS):
        imprimir_banner_assunto(modulo["nome"])

        for j, (nome_fase, executar_fase) in enumerate(modulo["fases"]):
            passou = executar_fase()

            if not passou:
                _derrota(f"{modulo['nome']} — {nome_fase}")
                return

            fases_ok += 1
            escrever(f"  📊  Progresso: {fases_ok}/{total_fases} desafios concluídos.")

            if j + 1 < len(modulo["fases"]):
                proxima = modulo["fases"][j + 1][0]
                _transicao_fase(proxima)

        if i + 1 < len(MODULOS):
            _transicao_modulo(MODULOS[i + 1]["nome"])

    imprimir_vitoria()