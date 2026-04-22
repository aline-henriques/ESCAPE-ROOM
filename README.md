```markdown
# 🚀 Escape Room Lógico v2.0

[cite_start]Jogo educativo desenvolvido integralmente em Python, com foco no ensino de conceitos de lógica proposicional de forma interativa, progressiva e gamificada[cite: 8, 14]. [cite_start]O projeto simula uma nave interestelar comprometida por um vírus lógico, onde o jogador assume o papel de tripulante para restaurar os sistemas[cite: 9, 15].

[cite_start]Desenvolvido por **Aline de Albuquerque Henriques** para a disciplina de Lógica para Computação (UNICAP)[cite: 1, 4, 19].

---

## ✨ Implementações e Diferenciais (v2.0)

* **Imersão Sonora**: Integração com a biblioteca `Pygame` para gerenciamento de trilha sonora e efeitos sonoros (SFX) durante acertos, erros e navegação.
* **Persistência de Dados**: Utilização de banco de dados local para salvar o progresso da missão e permitir o carregamento de partidas.
* **Ranking de Pilotos**: Sistema de pontuação acumulada com exibição de um "Top 10" para estimular o valor de replay.
* [cite_start]**Banco de Perguntas Aleatório**: Cada módulo possui 8 questões cadastradas, das quais 3 são sorteadas via `random.sample()` a cada partida, garantindo uma experiência única a cada sessão[cite: 10, 17, 25].

---

## 📁 Estrutura do Projeto

[cite_start]O sistema segue uma arquitetura modular para garantir alta coesão e facilidade de manutenção[cite: 11, 22].

```text
escape_room_logico/
[cite_start]├── main.py                <- Ponto de entrada do sistema [cite: 47]
[cite_start]├── game.py                <- Motor principal e controle de fluxo [cite: 48]
[cite_start]├── config.py              <- Parâmetros globais e constantes [cite: 49, 55]
├── database.db            <- Banco de dados (SQLite) para saves e ranking
[cite_start]├── utils/                 <- Módulos auxiliares de utilidade [cite: 50]
[cite_start]│   ├── display.py         <- Interface narrativa e efeito typewriter [cite: 64, 70]
│   ├── audio.py           <- Gerenciador de som (SFX e Música)
│   ├── banco.py           <- Manipulação do banco de dados (Ranking)
[cite_start]│   └── timer.py           <- Cronômetro em thread paralela [cite: 73]
[cite_start]└── fases/                 <- Conteúdo temático e bancos de perguntas [cite: 51]
    [cite_start]├── conectivos.py      <- Módulo 1: Conectivos Lógicos (∧, ∨, ¬) [cite: 116]
    [cite_start]├── tabela_verdade.py  <- Módulo 2: Tabela-Verdade (→) [cite: 120]
    [cite_start]├── implicacao.py      <- Módulo 3: Implicação Lógica (Argumentos) [cite: 123]
    [cite_start]├── equivalencia.py    <- Módulo 4: Equivalência Lógica (De Morgan) [cite: 126]
    [cite_start]└── tautologia.py      <- Módulo 5: Tautologia e Contradição [cite: 129]
```

---

## ⚙️ Tecnologias Utilizadas

* [cite_start]**Python 3.10+**: Linguagem base do sistema[cite: 8].
* **Rich**: Formatação avançada e cores para interface via terminal.
* **Pygame**: Motor para execução de áudio e efeitos sonoros.
* **SQLite3**: Persistência de dados local.
* [cite_start]**Threading**: Execução de timer em segundo plano[cite: 73].

---

## 🎮 Como Jogar

1.  [cite_start]**Teste de Admissão**: O jogador deve traduzir corretamente uma condicional ($P \rightarrow Q$) para avançar[cite: 138, 160].
2.  [cite_start]**Desafios**: Resolva 3 questões por módulo temático[cite: 139].
3.  **Mecânicas**:
    * [cite_start]**Tentativas**: Cada desafio possui um limite de `MAX_TENTATIVAS`[cite: 57, 164].
    * [cite_start]**Dicas**: Mensagens pedagógicas são exibidas em caso de erro[cite: 165].
    * [cite_start]**Progresso**: Acompanhamento em tempo real (ex: 5/15 sistemas restaurados)[cite: 168].
4.  [cite_start]**Vitória**: A conclusão do 5º módulo libera a nave para o piloto[cite: 141].

---

## 🔮 Evoluções Futuras (Roadmap)

* **Interface TUI**: Implementação de molduras estáticas e layouts fixos para maior imersão visual.
* **Comandos CLI**: Criação de atalhos globais (como `HELP` ou `STATUS`) para auxílio dinâmico durante as perguntas.

---

## ▶️ Execução

Instale as dependências necessárias:
```bash
pip install pygame rich
```

Inicie o jogo:
```bash
python main.py
```
```