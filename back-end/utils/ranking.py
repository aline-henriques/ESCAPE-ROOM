import json, os
from rich.table import Table
from rich.console import Console
def salvar_pontuacao(n, p):
    r = []
    if os.path.exists("ranking.json"):
        with open("ranking.json", "r") as f: r = json.load(f)
    r.append({"nome": n, "pontos": p})
    r = sorted(r, key=lambda x: x["pontos"], reverse=True)[:5]
    with open("ranking.json", "w") as f: json.dump(r, f, indent=4)
def exibir_ranking_final():
    if not os.path.exists("ranking.json"): return
    t = Table(title="🏆 RANKING", style="yellow")
    t.add_column("Piloto")
    t.add_column("Pontos")
    with open("ranking.json", "r") as f:
        for j in json.load(f): t.add_row(j["nome"], str(j["pontos"]))
    Console().print(t)