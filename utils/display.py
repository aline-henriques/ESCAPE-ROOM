# Funções de exibição

import sys
import time
from config import TYPING_SPEED


def escrever(texto: str, velocidade: float = TYPING_SPEED) -> None:
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()


def imprimir_cabecalho(titulo: str, subtitulo: str = "") -> None:
    linha = "═" * 56
    print(f"\n{linha}")
    print(f"  🚀  {titulo}")
    if subtitulo:
        print(f"       {subtitulo}")
    print(f"{linha}\n")


def imprimir_separador() -> None:
    print("─" * 56)


def imprimir_sucesso() -> None:
    print()
    escrever("  ✅  ACESSO CONCEDIDO — PORTA DESBLOQUEADA!")
    escrever("       Sistema liberado. Avançando...\n")
    time.sleep(0.6)


def imprimir_falha(tentativa: int, max_tentativas: int) -> None:
    restantes = max_tentativas - tentativa
    print()
    escrever("  ❌  ERRO DE LÓGICA DETECTADO")
    if restantes > 0:
        escrever(f"       Tentativas restantes: {restantes}\n")
    else:
        escrever("       Nenhuma tentativa restante.\n")


def imprimir_fim_de_jogo() -> None:
    print()
    escrever("  💀  SISTEMA TRAVADO — PROTOCOLO DE AUTODESTRUIÇÃO INICIADO")
    escrever("       A nave foi perdida. Tente novamente.\n")
    time.sleep(1)


def imprimir_vitoria() -> None:
    linha = "★" * 56
    print(f"\n{linha}")
    escrever("  🎉  TODOS OS SISTEMAS LIBERADOS!")
    escrever("  🛸  BEM-VINDO À LIBERDADE, TRIPULANTE.")
    print(f"{linha}\n")


def imprimir_banner_assunto(nome: str) -> None:
    print("\n" + "▓" * 56)
    print(f"  📡  MÓDULO: {nome.upper()}")
    print("▓" * 56 + "\n")
    time.sleep(0.4)


def perguntar_multipla_escolha(opcoes: dict[str, str]) -> str:
    print()
    for chave, texto in opcoes.items():
        print(f"  [{chave}] {texto}")
    print()
    while True:
        resposta = input("  > Sua resposta: ").strip().upper()
        if resposta in opcoes:
            return resposta
        print(f"  ⚠  Opção inválida. Escolha entre: {', '.join(opcoes.keys())}")


def perguntar_verdadeiro_falso(prompt: str = "") -> str:
    if prompt:
        escrever(prompt)
    while True:
        resposta = input("  > (V / F): ").strip().upper()
        if resposta in ("V", "F"):
            return resposta
        print("  ⚠  Digite V (Verdadeiro) ou F (Falso).")