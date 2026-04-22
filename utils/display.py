# ============================================================
#  DISPLAY DO JOGO
# ============================================================

import sys
import time
from rich.console import Console
from config import TYPING_SPEED
from utils.audio import tocar_sfx 

console = Console()

def escrever(texto: str, velocidade: float = TYPING_SPEED) -> None:
    texto_limpo = texto.rstrip('\n') 
    for caractere in texto_limpo:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)
    sys.stdout.write("\n")
    sys.stdout.flush()

def imprimir_cabecalho(titulo: str, subtitulo: str = "") -> None:
    linha = "═" * 56
    console.print(f"\n[cyan]{linha}[/cyan]")
    console.print(f"  🚀  [bold white]{titulo}[/bold white]")
    if subtitulo:
        console.print(f"       [italic]{subtitulo}[/italic]")
    console.print(f"[cyan]{linha}[/cyan]\n")

def imprimir_separador() -> None:
    console.print("[blue]─[/blue]" * 56)

def imprimir_sucesso() -> None:
    tocar_sfx("acerto")
    print()
    console.print("  ✅  [bold green]ACESSO CONCEDIDO — PORTA DESBLOQUEADA![/bold green]")
    escrever("      Sistema liberado. Avançando...")
    print()
    time.sleep(0.6)

def imprimir_falha(tentativa: int, max_tentativas: int) -> None:
    tocar_sfx("erro") 
    restantes = max_tentativas - tentativa
    print()
    console.print("  ❌  [bold red]ERRO DE LÓGICA DETECTADO[/bold red]")
    if restantes > 0:
        escrever(f"      Tentativas restantes: {restantes}")
    else:
        escrever("      Nenhuma tentativa restante.")
    print()

def imprimir_fim_de_jogo() -> None:
    tocar_sfx("erro")
    print()
    console.print("  💀  [bold white on red] SISTEMA TRAVADO — PROTOCOLO DE AUTODESTRUIÇÃO [/bold white on red]")
    escrever("      A nave foi perdida. Tente novamente.")
    print()
    time.sleep(1)

def imprimir_vitoria() -> None:
    tocar_sfx("acerto")
    linha = "★" * 56
    console.print(f"\n[yellow]{linha}[/yellow]")
    console.print("  🎉  [bold yellow]TODOS OS SISTEMAS LIBERADOS![/bold yellow]")
    console.print("  🛸  [bold white]BEM-VINDO À LIBERDADE, TRIPULANTE.[/bold white]")
    console.print(f"[yellow]{linha}[/yellow]\n")

def imprimir_banner_assunto(nome: str) -> None:
    print("\n" + "▓" * 56)
    console.print(f"  📡  [bold magenta]MÓDULO: {nome.upper()}[/bold magenta]")
    print("▓" * 56 + "\n")
    time.sleep(0.4)

def perguntar_multipla_escolha(opcoes: dict[str, str]) -> str:
    print()
    for chave, texto in opcoes.items():
        console.print(f"  [[bold yellow]{chave}[/bold yellow]] {texto}")
    print()
    while True:
        resposta = input("  > Sua resposta: ").strip().upper()
        if resposta in opcoes:
            return resposta
        console.print(f"  ⚠  [red]Opção inválida. Escolha entre: {', '.join(opcoes.keys())}[/red]")

def perguntar_verdadeiro_falso(prompt: str = "") -> str:
    if prompt:
        escrever(prompt)
    while True:
        resposta = input("  > (V / F): ").strip().upper()
        if resposta in ("V", "F"):
            return resposta
        console.print("  ⚠  [red]Digite V (Verdadeiro) ou F (Falso).[/red]")