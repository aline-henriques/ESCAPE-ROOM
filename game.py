import time
import sys
from rich.console import Console
from rich.table import Table
from utils.audio import iniciar_musica, tocar_sfx
from utils.display import (
    escrever, imprimir_separador, imprimir_vitoria,
    imprimir_banner_assunto, imprimir_cabecalho, imprimir_fim_de_jogo
)
from utils.banco import inicializar_banco, salvar_progresso, carregar_jogador, obter_ranking
from fases import conectivos, tabela_verdade, implicacao, equivalencia, tautologia

console = Console()

MODULOS = [
    {"nome": "Conectivos Lógicos", "modulo": conectivos},
    {"nome": "Tabela-Verdade", "modulo": tabela_verdade},
    {"nome": "Implicação Lógica", "modulo": implicacao},
    {"nome": "Equivalência Lógica", "modulo": equivalencia},
    {"nome": "Tautologia / Contradição / Contingência", "modulo": tautologia},
]

def exibir_menu_inicial():
    console.clear()
    imprimir_cabecalho("NAVE INTERESTELAR X-17", "SISTEMA DE SEGURANÇA LÓGICA")
    console.print("  [1] [bold green]INICIAR NOVA MISSÃO[/bold green]")
    console.print("  [2] [bold blue]CONTINUAR MISSÃO (LOAD)[/bold blue]")
    console.print("  [3] [bold magenta]RANKING DE PILOTOS[/bold magenta]")
    console.print("  [4] [bold red]SAIR DO SISTEMA[/bold red]")
    console.print("\n" + "─" * 56)
    return input("  > Selecione uma opção: ")

def exibir_ranking_pilotos():
    ranking = obter_ranking()
    console.clear()
    table = Table(title="🏆 TOP PILOTOS", style="magenta", border_style="cyan")
    table.add_column("Pos", justify="center")
    table.add_column("Piloto", style="bold white")
    table.add_column("Pontos", justify="right", style="green")

    if not ranking:
        table.add_row("-", "Nenhum dado", "0")
    else:
        for i, (nome, pontos) in enumerate(ranking, 1):
            table.add_row(str(i), nome, str(pontos))
    console.print(table)
    input("\n  Pressione ENTER para retornar...")

def _teste_entrada() -> None:
    escrever("  Antes de iniciar, prove que você merece entrar na nave...")
    time.sleep(0.5)
    escrever("\n  📋 TESTE DE ADMISSÃO:")
    imprimir_separador()
    escrever("  Considere as proposições:\n     P: Se eu estudar\n     Q: Vou conseguir passar na prova do professor Lucas")
    escrever("\n  Questão: Traduza ( P → Q ) para linguagem natural.")
    imprimir_separador()

    respostas_aceitas = [
        "se eu estudar, vou conseguir passar na prova do professor lucas",
        "se eu estudar vou conseguir passar na prova do professor lucas",
        "se eu estudar, então vou conseguir passar na prova do professor lucas",
        "se eu estudar então vou conseguir passar na prova do professor lucas",
        "Se eu estudar, então vou conseguir passar na prova do professor Lucas.",
        "Se eu estudar, vou conseguir passar na prova do professor Lucas",
        "se eu estudar, vou conseguir passar na prova do professor lucas"
    ]

    while True:
        resposta = input("\n  > Digite a tradução: ").strip().lower()
        if any(aceita in resposta for aceita in respostas_aceitas):
            escrever("\n  ✅ Admissão aprovada! Sistema liberado.")
            time.sleep(0.8)
            break
        else:
            escrever("  ❌ Tente novamente. Dica: Use 'Se P, então Q'.")

def _introducao() -> None:
    console.clear()
    console.print("\n" + "═" * 56, style="cyan")
    escrever("  🛸 NAVE INTERESTELAR X-17 - SISTEMA DE SEGURANÇA")
    console.print("═" * 56 + "\n", style="cyan")
    escrever("  Ano 2157. Sua nave foi capturada por um vírus lógico.")
    escrever("  Restaure os 5 módulos para sobreviver.")
    _teste_entrada()
    input("\n  [ Pressione ENTER para iniciar ]")

def jogar(nome, pontos_iniciais=0, modulo_inicio=0):
    pontuacao = pontos_iniciais
    total_perguntas = len(MODULOS) * 3
    concluidos = modulo_inicio * 3

    if modulo_inicio == 0:
        _introducao()

    for i in range(modulo_inicio, len(MODULOS)):
        item = MODULOS[i]
        tocar_sfx("porta")
        imprimir_banner_assunto(item["nome"])
        
        perguntas = item["modulo"].sortear(3)

        for pergunta in perguntas:
            passou = item["modulo"]._rodar(pergunta)

            if passou:
                pontuacao += 100
                concluidos += 1
                console.print(f"\n[bold green]📊 Progresso: {concluidos}/{total_perguntas} sistemas restaurados.[/bold green]")
                imprimir_separador()
            else:
                imprimir_fim_de_jogo()
                return 

        salvar_progresso(nome, pontuacao, i + 1)
        escrever(f"\n  💾 Progresso salvo: Módulo {item['nome']} concluído!")
        time.sleep(1)

    imprimir_vitoria()
    escrever(f"  PONTUAÇÃO FINAL DO PILOTO {nome}: {pontuacao} PONTOS")
    input("\n  Pressione ENTER para voltar ao menu...")

def iniciar() -> None:
    inicializar_banco()
    iniciar_musica()
    
    while True:
        opcao = exibir_menu_inicial()
        if opcao == "1":
            nome = input("  > Nome do Piloto: ").strip().upper()
            if nome: jogar(nome, 0, 0)
        elif opcao == "2":
            nome = input("  > Digite seu Nome: ").strip().upper()
            dados = carregar_jogador(nome)
            if dados:
                jogar(nome, dados[0], dados[1])
            else:
                escrever("  ❌ Piloto não encontrado.")
                time.sleep(1)
        elif opcao == "3":
            exibir_ranking_pilotos()
        elif opcao == "4":
            sys.exit()